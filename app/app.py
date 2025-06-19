# app.py
# Streamlit web UI for the document Q&A bot

import streamlit as st
from ocr.ocr_utils import extract_text_from_pdf
from langchain_pipeline.langchain_pipeline import build_qa_chain

# Title for the app
st.title("PDFBot")

# Let user upload a scanned PDF
uploaded_file = st.file_uploader("Upload a scanned PDF", type="pdf")

if uploaded_file:
    # Save uploaded PDF locally
    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Show spinner while OCR and pipeline are running
    with st.spinner("Processing PDF..."):
        text = extract_text_from_pdf("data/temp.pdf")
        qa_chain = build_qa_chain(text)

    # Input box to ask questions
    query = st.text_input("Ask a question about your document:")
    if query:
        answer = qa_chain.run(query)
        st.write("**Answer:**", answer)
