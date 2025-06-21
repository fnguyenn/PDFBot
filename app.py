# app.py
# Streamlit web UI for the document Q&A bot with error handling

import streamlit as st
import os
from ocr.ocr_utils import extract_text_from_pdf
from ocr.ocr_utils import extract_text_from_image
from langchain_pipeline.langchain_pipeline import build_qa_chain

st.set_page_config(page_title="PDFBot", layout="centered")
st.title("PDFBot: Ask Questions About Your Document")

# Upload scanned PDF
uploaded_files = st.file_uploader(
    "Upload a scanned PDF or one or more images",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    try:
        all_text = ""

        for file in uploaded_files:
            file_ext = file.name.split(".")[-1].lower()
            file_path = f"data/{file.name}"

            with open(file_path, "wb") as f:
                f.write(file.read())

            if file_ext == "pdf":
                text = extract_text_from_pdf(file_path)

            elif file_ext in ["png", "jpg", "jpeg"]:
                text = extract_text_from_image(file_path)

            else:
                st.warning(f"Unsupported file type: {file.name}")
                text = ""
                continue

            all_text += text + "\n\n"

        if not all_text.strip():
            st.error("No text could be extracted from the uploaded files.")
        else:
            with st.spinner("Building QA chain..."):
                qa_chain = build_qa_chain(all_text)
            st.success("Ready! Ask your question below.")

            query = st.text_input("Ask a question about your document:")
            if query:
                answer = qa_chain.invoke(query)
                st.write("**Answer:**", answer)

    except Exception as e:
        st.error(f"An error occurred: {e}")

for file in uploaded_files:
    try:
        os.remove(f"data/{file.name}")
    except Exception:
        pass  # Silent cleanup failure