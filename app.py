import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
import tempfile

load_dotenv()

# Page config
st.set_page_config(
    page_title="Legal Contract Analyser",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Legal Contract Analyser")
st.caption("Upload any legal document — contract, loan agreement, NDA, RBI circular. Ask questions from it.")

# Initialize session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Load LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

# Load embeddings model
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

embeddings = load_embeddings()

# PDF Upload
uploaded_file = st.file_uploader(
    "Upload your document (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    if st.button("Process Document", type="primary"):
        with st.spinner("Reading and processing document..."):

            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            # Step 1: Load PDF
            loader = PyPDFLoader(tmp_path)
            documents = loader.load()

            # Step 2: Split into chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_documents(documents)

            # Step 3: Store in FAISS vector database
            vector_store = FAISS.from_documents(chunks, embeddings)
            st.session_state.vector_store = vector_store

            # Clean up temp file
            os.unlink(tmp_path)

            st.success(f"Document processed. {len(chunks)} chunks stored in vector database.")

# Chat interface
if st.session_state.vector_store is not None:
    st.divider()
    st.subheader("Ask questions from your document")

    # Show chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    question = st.chat_input("Ask anything from the document...")

    if question:
        # Show user question
        with st.chat_message("user"):
            st.write(question)

        # Get answer from FAISS + LLM
        with st.chat_message("assistant"):
            with st.spinner("Searching document..."):

                # Create prompt
                prompt_template = ChatPromptTemplate.from_messages([
                    ("system", """You are a legal document analyst.
Answer the question using ONLY the context provided from the document.
If the answer is not in the context, say: This information is not found in the uploaded document.
Be precise and cite relevant clauses when possible."""),
                    ("human", """Context from document:
{context}

Question: {question}""")
                ])

                # Search FAISS for relevant chunks
                retriever = st.session_state.vector_store.as_retriever(
                    search_kwargs={"k": 4}
                )
                relevant_docs = retriever.invoke(question)
                context = "\n\n".join([doc.page_content for doc in relevant_docs])

                # Get answer
                chain = prompt_template | llm
                response = chain.invoke({
                    "context": context,
                    "question": question
                })

                st.write(response.content)

        # Save to history
        st.session_state.chat_history.append({"role": "user", "content": question})
        st.session_state.chat_history.append({"role": "assistant", "content": response.content})

else:
    st.info("Please upload a PDF document to start analysing.")