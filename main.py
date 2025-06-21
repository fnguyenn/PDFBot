# main.py
# Command-line interface for uploading a scanned PDF, extracting text, and asking questions

from ocr.ocr_utils import extract_text_from_pdf
from ocr.ocr_utils import extract_text_from_image
from langchain_pipeline.langchain_pipeline import build_qa_chain

if __name__ == "__main__":
    # Path to the test pdf
    filepath = "data/image_no_text.jpg"

    # Run OCR to get raw text from the scanned PDF
    text = extract_text_from_image(filepath)

    if not text.strip():
            print("Could not extract any text from the file.")

    '''
    # Build a LangChain QA chain from the extracted text
    qa_chain = build_qa_chain(text)

    # Loop to ask questions interactively
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa_chain.invoke(query)
        print("Answer:", answer)
    '''