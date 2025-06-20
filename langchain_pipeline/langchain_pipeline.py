# langchain_pipeline.py

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def build_qa_chain(text):
    # Step 1: Split text into documents
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])

    # Step 2: Create vectorstore and retriever
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    # Step 3: Define your prompt
    prompt = PromptTemplate.from_template("""
    You are a helpful assistant. Use the following context to answer the question.
    
    Context:
    {context}

    Question:
    {question}

    Answer:
    """)

    # Step 4: Build the chain with LCEL
    llm = ChatOpenAI(model="gpt-4")

    chain = (
        {"context": retriever | RunnablePassthrough(), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
