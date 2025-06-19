import streamlit as st
from ocr.ocr_utils import extract_text_from_pdf
from langchain_pipeline.langchain_pipeline import build_qa_chain

st.title("PDFBot")
uploaded_file = st.file_uploader("Upload a scanned PDF", type="pdf")

if uploaded_file:
    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing PDF..."):
        text = extract_text_from_pdf("data/temp.pdf")
        qa_chain = build_qa_chain(text)

    query = st.text_input("Ask a question about your document:")
    if query:
        answer = qa_chain.run(query)
        st.write("**Answer:**", answer)