from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(document):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=10
    )

    chunks = text_splitter.split_documents(document)

    return chunks