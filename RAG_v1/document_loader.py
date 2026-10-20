from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("RAG_v1/data/machine_learning_rag_test.pdf")
document  = loader.load()