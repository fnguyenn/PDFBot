from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import os

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def extract_images_from_pdf(pdf_path, output_folder="temp_images"):
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)
    image_paths = []
    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        pix = page.get_pixmap()
        image_path = os.path.join(output_folder, f"page_{page_index}.png")
        pix.save(image_path)
        image_paths.append(image_path)
    return image_paths

def extract_text_from_pdf(pdf_path):
    images = extract_images_from_pdf(pdf_path)
    text = "\n".join([extract_text_from_image(img) for img in images])
    return text