# app.py
# Streamlit web UI for the document Q&A bot with error handling

import streamlit as st
from ocr.ocr_utils import extract_text_from_pdf
from ocr.ocr_utils import extract_text_from_image
from langchain_pipeline.langchain_pipeline import build_qa_chain

st.set_page_config(page_title="PDFBot", layout="centered")
st.title("PDFBot: Ask Questions About Your Document")

# Upload scanned PDF
uploaded_file = st.file_uploader("Upload a scanned PDF or image of text", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    try:
        file_ext = uploaded_file.name.split(".")[-1].lower()

        with st.spinner("Processing document..."):
            if file_ext == "pdf":
                # Save and extract text from PDF
                pdf_path = "data/temp.pdf"
                with open(pdf_path, "wb") as f:
                    f.write(uploaded_file.read())
                text = extract_text_from_pdf(pdf_path)

            elif file_ext in ["png", "jpg", "jpeg"]:
                # Save and extract text from image
                image_path = f"data/temp.{file_ext}"
                with open(image_path, "wb") as f:
                    f.write(uploaded_file.read())
                text = extract_text_from_image(image_path)

            else:
                st.error("Unsupported file type.")
                text = ""

        if not text.strip():
            st.error("Could not extract any text from the file.")
        else:
            qa_chain = build_qa_chain(text)
            st.success("Ready! Ask your question below.")
            query = st.text_input("Ask a question about your document:")
            if query:
                answer = qa_chain.invoke(query)
                st.write("**Answer:**", answer)

    except Exception as e:
        st.error(f"An error occurred: {e}")