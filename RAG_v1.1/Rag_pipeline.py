from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from document_loader import load_document
from text_splitter import split_documents
from vector_store import create_vector_store
from retriever import create_retriever


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


prompt = ChatPromptTemplate.from_template("""
Answer the question using only the context provided below.

If the answer is not present in the context,
say: "I don't know based on the provided document."

Context: {context}

Question: {question}

Answer:
""")


def generate_answer(question, retriever):

    retrieved_docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    messages = prompt.invoke({
        "context": context,
        "question": question
    })

    response = llm.invoke(messages)

    if isinstance(response.content, str):
        return response.content

    return "\n".join(
        block["text"]
        for block in response.content
        if isinstance(block, dict) and block.get("type") == "text"
    )


if __name__ == "__main__":

    pdf_path = (
        Path(__file__).resolve().parent
        / "data"
        / "machine_learning_rag_test.pdf"
    )

    document = load_document(str(pdf_path))

    chunks = split_documents(document)

    vector_store = create_vector_store(chunks)

    retriever = create_retriever(vector_store)

    print("RAG pipeline is ready!")

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        answer = generate_answer(question, retriever)

        print("\nAnswer:", answer)