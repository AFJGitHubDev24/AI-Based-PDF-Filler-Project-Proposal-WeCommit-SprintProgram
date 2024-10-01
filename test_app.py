from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to PDF Knowledge AI Filler"}

def test_create_knowledge_base_item():
    response = client.post("/knowledge/", json={
        "field_name": "Test Field",
        "value": "Test Value"
    })
    assert response.status_code == 200
    assert response.json()["field_name"] == "Test Field"
    assert response.json()["value"] == "Test Value"

def test_upload_pdf():
    with open("tests/Dummy_Questionnaire.pdf", "rb") as pdf_file:
        response = client.post("/pdf/upload/", files={"pdf": ("Dummy_Questionnaire.pdf", pdf_file, "application/pdf")})
        assert response.status_code == 200
        assert "output_file" in response.json()

def test_index_html():
    response = client.get('/')
    assert response.status_code == 200
    assert '<title>FastAPI PDF Web App</title>' in response.text
    assert '<h1>FastAPI PDF Web App</h1>' in response.text

def test_static_css():
    response = client.get('/static/css/styles.css')
    assert response.status_code == 200
    assert 'body {' in response.text  # Check for a specific CSS rule

def test_static_js():
    response = client.get('/static/js/app.js')
    assert response.status_code == 200
    assert 'document.addEventListener' in response.text  # Check for a specific JavaScript function
