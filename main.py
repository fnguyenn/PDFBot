# main.py
# Command-line interface for uploading a scanned PDF, extracting text, and asking questions

from ocr.ocr_utils import extract_text_from_pdf
from langchain_pipeline.langchain_pipeline import build_qa_chain

if __name__ == "__main__":
    # Path to the PDF you want to analyze
    filepath = "data/sample_doc.pdf"

    # Run OCR to get raw text from the scanned PDF
    text = extract_text_from_pdf(filepath)

    # Build a LangChain QA system from the extracted text
    qa_chain = build_qa_chain(text)

    # Loop to ask questions interactively
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa_chain.invoke(query)
        print("Answer:", answer)
