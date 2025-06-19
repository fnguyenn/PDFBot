from ocr_utils import extract_text_from_pdf
from langchain_pipeline import build_qa_chain

if __name__ == "__main__":
    filepath = "data/sample_doc.pdf"
    text = extract_text_from_pdf(filepath)

    qa_chain = build_qa_chain(text)

    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa_chain.run(query)
        print("Answer:", answer)