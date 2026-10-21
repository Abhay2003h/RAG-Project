# RAG_v1.1: Basic Retrieval-Augmented Generation

## Overview

RAG_v1.1 is a basic Retrieval-Augmented Generation (RAG) project built using Python, LangChain, ChromaDB, Hugging Face embeddings, Google Gemini, and Chainlit.

The application loads a PDF document, splits its content into smaller chunks, stores their embeddings in a vector database, retrieves relevant information based on a user's question, and generates an answer using a large language model (LLM).

The project provides an interactive web-based chat interface using Chainlit, allowing users to ask questions and receive answers through a conversational interface instead of interacting only through the terminal.

The purpose of this project is to understand and implement the fundamental components of a RAG pipeline with a web-based user interface.

## Features

* PDF document loading using `PyPDFLoader`.
* Text chunking using `RecursiveCharacterTextSplitter`.
* Text embeddings using Hugging Face.
* Vector storage using ChromaDB.
* Similarity-based document retrieval.
* Answer generation using Google Gemini.
* Interactive chatbot interface using Chainlit.
* Conversational question-answering through a web browser.
* Environment variable management using `python-dotenv`.

## Tech Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Programming language            |
| LangChain             | RAG pipeline components         |
| PyPDF                 | PDF text extraction             |
| Hugging Face          | Text embeddings                 |
| Sentence Transformers | Embedding generation            |
| ChromaDB              | Vector database                 |
| Google Gemini         | Answer generation               |
| Chainlit              | Web-based chatbot interface     |
| python-dotenv         | Environment variable management |

## Project Structure

```text
RAG_v1.1/
├── data/
│   └── machine_learning_rag_test.pdf
├── document_loader.py
├── text_splitter.py
├── vector_store.py
├── retriever.py
├── rag_pipeline.py
├── app.py
├── requirements.txt
└── README.md
```

**Note:** `app.py` represents the Chainlit application entry point. Adjust the filename if your actual entry point is different.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd RAG_v1.1
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure that your `requirements.txt` includes Chainlit and all other dependencies required by your implementation.

If Chainlit is not already included, install it using:

```bash
pip install chainlit
```

### 4. Configure the API Key

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_google_api_key
```

Replace the placeholder with your Google Gemini API key.

Never commit your `.env` file or expose your API key publicly.

### 5. Add Your PDF Document

Place your PDF file inside the `data` folder and ensure the file path in your document loader matches its filename.

### 6. Run the Application

Start the Chainlit application using:

```bash
chainlit run app.py
```

Replace `app.py` with your actual Chainlit entry-point filename if necessary.

Chainlit will start a local web server and provide a URL where you can access the chatbot through your browser.

## How the Application Works

The application follows these steps:

1. **Document Loading:** Extracts text from the PDF.
2. **Chunking:** Divides the document into smaller text segments.
3. **Embedding Generation:** Converts text chunks into numerical vectors.
4. **Vector Storage:** Stores the vectors and associated text in ChromaDB.
5. **Retrieval:** Finds relevant chunks based on the user's query.
6. **Prompt Construction:** Combines the retrieved context with the question.
7. **Answer Generation:** Sends the prompt to Google Gemini.
8. **Response:** Displays the generated answer through the Chainlit chat interface.

## Example Questions

Using a machine learning PDF, you can ask:

* What are the main types of machine learning?
* What is overfitting?
* Which algorithm is used for clustering?
* What is the difference between precision and recall?
* Which metric is commonly used for regression evaluation?

The application is instructed to respond that it does not know when the answer is not present in the supplied context. However, this instruction does not guarantee that every response will be fully grounded.

## Current Limitations

* Basic similarity-based retrieval.
* PDF-focused document ingestion.
* No advanced reranking.
* No hybrid search.
* No formal retrieval evaluation framework.
* No production deployment configuration.
* Limited document management capabilities.

## Future Improvements

Planned improvements for future versions include:

* Source citations and page references.
* Persistent vector database reuse.
* Support for multiple document formats.
* Metadata filtering.
* Query rewriting.
* Hybrid search.
* Reranking.
* Retrieval and answer evaluation.
* Conversation history improvements.
* Multiple PDF uploads through the chat interface.
* Improved error handling.
* Production deployment.

## Learning Objectives

This project demonstrates the fundamental concepts of Retrieval-Augmented Generation, including document processing, text embeddings, vector databases, semantic retrieval, prompt construction, LLM-based answer generation, and integration of a web-based chatbot interface.

## Project Status

**Version:** v1.1

**Status:** Basic RAG implementation with Chainlit frontend.

This project is being developed incrementally, with future versions intended to introduce more advanced RAG techniques.
