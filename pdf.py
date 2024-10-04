from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from app.utils import process_pdf, save_file
import os

router = APIRouter()

# Directory for storing processed PDFs
PDF_DIR = "static/filled_pdfs/"

@router.post("/upload/", summary="Upload and process a PDF")
async def upload_pdf(pdf: UploadFile = File(...)):
    try:
        # Save uploaded PDF
        pdf_path = save_file(PDF_DIR, pdf)

        # Process the PDF (e.g., fill fields)
        output_pdf_path = await process_pdf(pdf_path)

        return {"message": "PDF processed successfully", "output_file": output_pdf_path}
    except Exception as e:
        print(f"Error: {str(e)}")  # Print or log the error
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")


@router.get("/download/{filename}", summary="Download a processed PDF")
async def download_pdf(filename: str):
    file_path = os.path.join(PDF_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/pdf", filename=filename)
    raise HTTPException(status_code=404, detail="File not found")

