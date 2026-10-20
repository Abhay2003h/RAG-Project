from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from retriever import retriever
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
    )

prompt = ChatPromptTemplate.from_template(""" 
Answer the question using only the context provided below. 
If the answer is not present in the context, 
say: "I don't know based on the provided document."
 Context: {context} Question: {question} Answer: 
 """)


while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == 'exit':
        break
    retrieved_docs = retriever.invoke(question)
    context = "\n\n".join( doc.page_content for doc in retrieved_docs ) 
    # Generate prompt
    messages = prompt.invoke({ "context": context, "question": question })
     # Generate answer 
    response = llm.invoke(messages)
    print("\nAnswer:", response.content)


