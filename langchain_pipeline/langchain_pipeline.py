# langchain_pipeline.py
# Creates a LangChain RetrievalQA pipeline to answer questions about a document

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Build the LangChain pipeline using OpenAI embeddings and GPT-4
def build_qa_chain(text):
    # Break the text into overlapping chunks for better retrieval
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])

    # Convert text chunks into vector embeddings
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    # Use GPT-4 to create a question-answering chain
    llm = ChatOpenAI(model="gpt-4")
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(),
        return_source_documents=True
    )
    return qa
