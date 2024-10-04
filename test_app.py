from fastapi.testclient import TestClient
from app.main import app
import PyPDF2
# import pytest
# from app.models import KnowledgeBase

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to PDF Knowledge AI Filler"}


def test_upload_pdf():
    pdf_file = ("dummy.pdf", b"%PDF-1.4 example", "application/pdf")
    response = client.post("/pdf/upload/", files={"Dummy_Questionnaire.pdf": pdf_file})
    assert response.status_code == 200
    assert "output_file" in response.json()

def test_pdf_processing(file_path):
    try:
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            print(f"PDF has {len(pdf_reader.pages)} pages")
            # Test AcroForm fields
            if "/AcroForm" in pdf_reader.trailer["/Root"]:
                form = pdf_reader.trailer["/Root"]["/AcroForm"]
                fields = form.get("/Fields")
                if fields:
                    print("PDF has AcroForm fields")
                else:
                    print("No AcroForm fields found")
            else:
                print("No AcroForm found")
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")

# Test with your PDF file
test_pdf_processing("Dummy_Questionnaire.pdf")


def test_create_knowledge_base_item():
    response = client.post("/knowledge/", json={"field_name": "Test Field", "value": "Test Value"})
    assert response.status_code == 200
    assert response.json()["field_name"] == "Test Field"
    assert response.json()["value"] == "Test Value"

def test_get_knowledge_base_items():
    response = client.get("/knowledge/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_knowledge_base_item():
    # Assuming an item exists with ID 1
    response = client.get("/knowledge/1")
    assert response.status_code == 200
    assert "field_name" in response.json()

def test_update_knowledge_base_item():
    response = client.put("/knowledge/1", json={"field_name": "Updated Field", "value": "Updated Value"})
    assert response.status_code == 200
    assert response.json()["field_name"] == "Updated Field"

def test_delete_knowledge_base_item():
    response = client.delete("/knowledge/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}

def test_index_html():
    response = client.get('/')
    assert response.status_code == 200
    assert '<title>FastAPI PDF Web App</title>' in response.text
    assert '<h1>FastAPI PDF Web App</h1>' in response.text

def test_static_css():
    response = client.get('/static/css/styles.css')
    assert response.status_code == 200
    assert 'body {' in response.text

def test_static_js():
    response = client.get('/static/js/app.js')
    assert response.status_code == 200
    assert 'document.addEventListener' in response.text

