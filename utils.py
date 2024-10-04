import os
from fastapi import UploadFile
from PyPDF2 import PdfReader, PdfWriter

# Directory for storing the processed PDFs
PDF_DIR = "static/filled_pdfs/"

# Save the uploaded PDF to a specific directory
def save_file(directory: str, pdf: UploadFile):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, pdf.filename)
    with open(file_path, "wb") as f:
        f.write(pdf.file.read())
    return file_path

# Process the PDF by reading and modifying it using the knowledge base (simplified example)
async def process_pdf(pdf_path: str) -> str:
    # Read the PDF
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Loop over all pages and copy them to a new writer (for now, a simple pass-through)
    for page in reader.pages:
        writer.add_page(page)

    # Output PDF filename
    output_filename = f"filled_{os.path.basename(pdf_path)}"
    output_path = os.path.join(PDF_DIR, output_filename)

    # Save the output PDF
    with open(output_path, "wb") as f:
        writer.write(f)

    return output_filename
