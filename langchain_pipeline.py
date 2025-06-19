from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def build_qa_chain(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    llm = ChatOpenAI(model="gpt-4")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever(), return_source_documents=True)
    return qa