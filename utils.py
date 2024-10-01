import PyPDF2
from PyPDF2.generic import NameObject, TextStringObject
from app.models import KnowledgeBase
import os
import uuid
from fastapi import UploadFile


def save_file(directory: str, file: UploadFile) -> str:
    # Generate a unique file name
    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(directory, unique_filename)

    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Save the file to the directory
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path

async def process_pdf(pdf_path: str) -> str:
    try:
        # Open the PDF file
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            output_pdf_path = pdf_path.replace(".pdf", "_filled.pdf")

            # Loop through pages to find form fields
            if "/AcroForm" in pdf_reader.trailer["/Root"]:
                form = pdf_reader.trailer["/Root"]["/AcroForm"]
                fields = form.get("/Fields")

                # Fill the fields with knowledge base values
                for field in fields:
                    field_obj = field.get_object()
                    field_name = field_obj.get("/T")
                    if field_name:
                        # Query knowledge base for field_name
                        knowledge_item = await KnowledgeBase.get_or_none(field_name=field_name)
                        if knowledge_item:
                            field_value = knowledge_item.value
                            field_obj.update({
                                NameObject("/V"): TextStringObject(field_value)
                            })

            # Save the modified PDF
            with open(output_pdf_path, "wb") as output_pdf_file:
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.write(output_pdf_file)

            return output_pdf_path
    except Exception as e:
        raise RuntimeError(f"Failed to process PDF: {str(e)}")
