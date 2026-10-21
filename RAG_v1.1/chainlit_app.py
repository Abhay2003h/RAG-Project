import chainlit as cl

from document_loader import load_document
from text_splitter import split_documents
from vector_store import create_vector_store
from retriever import create_retriever
from Rag_pipeline import generate_answer


@cl.on_chat_start
async def start():

    files = await cl.AskFileMessage(
        content="Upload a PDF to start chatting.",
        accept=["application/pdf"],
        max_size_mb=20,
        timeout=180
    ).send()

    if not files:
        await cl.Message(
            content="No PDF uploaded. Please upload a PDF to continue."
        ).send()
        return

    file_path = files[0].path

    try:

        async with cl.Step(name="Processing PDF") as step:

            step.output = "Loading PDF..."

            document = load_document(file_path)

            if not document or not any(
                doc.page_content.strip() for doc in document
            ):
                step.output = "The PDF contains no extractable text."
                await cl.Message(
                    content="Please upload a PDF containing readable text."
                ).send()
                return

            step.output = "Splitting document into chunks..."

            chunks = split_documents(document)

            if not chunks:
                step.output = "No document chunks were generated."
                return

            step.output = "Creating embeddings and vector store..."

            vector_store = create_vector_store(chunks)

            step.output = "Creating retriever..."

            retriever = create_retriever(vector_store)

            cl.user_session.set("retriever", retriever)

            step.output = "PDF processing completed successfully."

        await cl.Message(
            content=(
                f"PDF uploaded successfully!\n\n"
                f"Pages loaded: {len(document)}\n"
                f"Chunks created: {len(chunks)}\n\n"
                f"You can now ask questions about your PDF."
            )
        ).send()

    except Exception as e:

        await cl.Message(
            content=f"Error processing PDF: {str(e)}"
        ).send()


@cl.on_message
async def answer_question(message: cl.Message):

    retriever = cl.user_session.get("retriever")

    if retriever is None:
        await cl.Message(
            content="Please upload a PDF before asking questions."
        ).send()
        return

    try:

        async with cl.Step(name="Retrieving and generating answer") as step:

            step.output = "Generating answer..."

            answer = await cl.make_async(generate_answer)(
                message.content,
                retriever
            )

            step.output = "Answer generated successfully."

        await cl.Message(
            content=answer
        ).send()

    except Exception as e:

        await cl.Message(
            content=f"Error generating answer: {str(e)}"
        ).send()