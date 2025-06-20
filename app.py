# app.py
# Streamlit web UI for the document Q&A bot (LCEL-compatible)

import streamlit as st
from ocr.ocr_utils import extract_text_from_pdf
from langchain_pipeline.langchain_pipeline import build_qa_chain

# Title for the app
st.title("📄 PDFBot: Ask Questions About Your Document")

# Upload scanned PDF
uploaded_file = st.file_uploader("Upload a scanned PDF", type="pdf")

if uploaded_file:
    # Save uploaded file
    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Process file with OCR and LangChain
    with st.spinner("Processing PDF..."):
        text = extract_text_from_pdf("data/temp.pdf")
        qa_chain = build_qa_chain(text)

    # Input for user questions
    query = st.text_input("Ask a question about your document:")
    if query:
        # Use LCEL's .invoke() method
        answer = qa_chain.invoke(query)
        st.write("**Answer:**", answer)