📄 Legal Contract Analyser

An AI-powered Legal Document Analysis application built using Streamlit, LangChain, Groq LLM, FAISS Vector Database, and HuggingFace Embeddings.

This application allows users to upload legal PDF documents such as:

Contracts
NDAs
Loan Agreements
RBI Circulars
Legal Notices
Policies

and ask questions directly from the uploaded document using AI-powered Retrieval-Augmented Generation (RAG).

🚀 Features

✅ Upload legal PDF documents

✅ AI-powered legal question answering

✅ RAG (Retrieval-Augmented Generation)

✅ FAISS vector database integration

✅ Groq LLM integration

✅ Semantic document search

✅ Chat-based interface

✅ Conversation history support

✅ Fast document retrieval

✅ Streamlit interactive UI

🧠 How the Application Works

The application follows the RAG (Retrieval-Augmented Generation) architecture.

Flow of Execution
User uploads a PDF legal document.
PDF is loaded using PyPDFLoader.
Document is split into smaller chunks.
Chunks are converted into vector embeddings.
Embeddings are stored inside FAISS vector database.
User asks a question.
Relevant document chunks are retrieved from FAISS.
Retrieved context is sent to Groq LLM.
AI generates accurate answers based only on uploaded document context.
Final response is shown in Streamlit chat UI.
🏗️ Tech Stack
Technology	Purpose
Python	Backend programming
Streamlit	Web application UI
LangChain	RAG pipeline and orchestration
Groq API	Large Language Model
FAISS	Vector database
HuggingFace Embeddings	Semantic embeddings
PyPDFLoader	PDF text extraction
dotenv	Environment variable management
📂 Project Structure
legal-contract-analyser/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
⚙️ Installation Steps
Step 1: Clone Repository
git clone https://github.com/israinamdar493-ops/legal-contract-analyser.git
cd legal-contract-analyser
Step 2: Create Virtual Environment
Windows
python -m venv venv

Activate environment:

venv\Scripts\activate
Step 3: Install Dependencies
pip install -r requirements.txt
📦 Requirements.txt

Create a file named requirements.txt

streamlit
langchain
langchain-groq
langchain-community
langchain-huggingface
faiss-cpu
sentence-transformers
pypdf
python-dotenv
🔑 API Keys Setup

Create a file named .env

GROQ_API_KEY=your_groq_api_key
🔗 Groq API Key Setup

Website:

Groq Console

Steps:

Login
Create API key
Copy API key
Paste into .env
▶️ Run the Application
streamlit run app.py
🌐 Streamlit App

After running:

Local URL: http://localhost:8501

Open it in browser.

💬 Example Questions
What is the termination clause?
What are the penalties mentioned?
Summarize the agreement.
What is the loan repayment period?
Who are the parties involved in the contract?
🧩 Main Components Explained
1. Streamlit UI

Responsible for:

File upload
Chat interface
Displaying AI responses
User interaction
2. Groq LLM

Used as the Large Language Model.

Benefits:

Very fast inference
Low latency
High-quality reasoning
Fast RAG responses

Model used:

llama-3.3-70b-versatile
3. RAG Pipeline

RAG = Retrieval-Augmented Generation

The system:

Retrieves relevant document chunks
Sends context to LLM
Generates grounded responses

Benefits:

✅ Reduces hallucinations

✅ Context-aware responses

✅ Accurate document QA

4. PyPDFLoader

Used for:

Extracting text from PDF documents
Converting PDF pages into LangChain documents
5. RecursiveCharacterTextSplitter

Splits large documents into smaller chunks.

Benefits:

Better semantic search
Efficient retrieval
Improved LLM performance

Configuration:

chunk_size=1000
chunk_overlap=200
6. HuggingFace Embeddings

Embedding model used:

sentence-transformers/all-MiniLM-L6-v2

Purpose:

Converts text into numerical vectors
Enables semantic similarity search
7. FAISS Vector Database

FAISS stores embeddings for efficient retrieval.

Benefits:

✅ Fast similarity search

✅ Scalable vector storage

✅ Efficient retrieval for RAG

🛡️ Security Notes

Never upload:

.env
API keys
Secret credentials

Create .gitignore

.env
venv/
__pycache__/
📈 Future Improvements

Possible enhancements:

Multi-document support
PDF highlighting
Clause extraction
Legal risk analysis
Contract summarization
Voice assistant
Chat memory
Authentication system
Deployment on cloud
OCR for scanned PDFs
🎯 Benefits of This Project

✅ Real-world GenAI application

✅ Demonstrates RAG architecture

✅ Strong AI/ML portfolio project

✅ Covers vector databases

✅ Demonstrates semantic search

✅ Useful for legal-tech applications

✅ Industry-relevant AI workflow

🧪 Technologies Learned

By building this project, you learn:

RAG pipelines
LangChain
Vector databases
FAISS
Embeddings
LLM integration
PDF processing
Streamlit apps
Semantic search
AI document QA systems
