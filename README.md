# AI-Based-PDF-Filler-Project-Proposal-WeCommit-SprintProgram

Technical Documentation

Overview
This FastAPI application generates PDF and DOCX files containing company information using data received from API requests. The application utilizes Tortoise ORM for database interactions and ReportLab for PDF generation. The data structure is validated using Pydantic models.

Approaches and Algorithms

1. Frameworks and Libraries Used:
   - **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
   - **Pydantic**: Used for data validation and settings management, ensuring that incoming data adheres to a specified schema.
   - **Tortoise ORM**: An easy-to-use asyncio ORM inspired by Django, used for database interactions.
   - **ReportLab**: A library for creating PDFs, enabling the dynamic generation of PDF documents with custom layouts and styles.
   - **python-docx**: A library for creating and updating Microsoft Word (.docx) files.

2. Data Flow:
   - File Upload: The `/upload/` endpoint handles file uploads. Currently, this is a placeholder for potential future file processing.
   - Generate PDF: The `/generate-pdf/` endpoint takes a JSON object conforming to the `CompanyData` model, processes it, and generates a PDF containing company information.
   - Generate DOCX: The `/generate-docx/` endpoint performs a similar function but outputs a DOCX file based on a template.

3. PDF Generation Logic:
   - The `create_company_info_pdf` function compiles the company data into structured tables and styled paragraphs. ReportLab's `SimpleDocTemplate` is used to define the document layout, while `Table` and `TableStyle` are employed to create formatted tables.

4. DOCX Generation Logic:
   - The `create_template_docx` function generates a DOCX file containing placeholders for company information in a structured format, using `python-docx`.

5. Database Schema:
   - The application uses a simple SQLite database with a `KnowledgeBase` model for potential future extensions. Currently, the model is set up but not fully utilized in the application.

Dependencies
- FastAPI
- Uvicorn
- Tortoise ORM
- ReportLab
- python-docx

---

README File

Project Overview
The FastAPI Knowledge App is a web application designed to generate PDF and DOCX files containing company information based on user-provided data. It features a RESTful API for file generation and uses a combination of modern Python libraries for handling data and document creation.

Features
- Generate PDFs and DOCX files containing detailed company profiles.
- Validates input data with Pydantic.
- Utilizes Tortoise ORM for database management.
- Simple file upload endpoint for future enhancements.

### Installation
1. Clone the repository (if applicable) or create a directory for your project.
2. Navigate to your project directory:
   ```bash
   cd your_project_directory
   ```
3. Create a 'requirements.txt` file** with the following content:
   ```
   fastapi
   uvicorn
   tortoise-orm
   aiofiles
   pytest
   tortoise
   pydantic
   fitz
   PyPDF2
   pytest
   reportlab
   docx
   ```
4. Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

Execution
To run the application, use the following command in your terminal:
```bash
uvicorn main:app --reload
```
The application will be accessible at `http://127.0.0.1:8000`.

API Endpoints
- **Upload File**: `POST /upload/` - Uploads a file (currently a placeholder).
- **Generate PDF**: `POST /generate-pdf/` - Generates a PDF from provided company data.
- **Generate DOCX**: `POST /generate-docx/` - Generates a DOCX from provided company data.

Example Input
The following JSON structure can be used to test the PDF and DOCX generation endpoints:
json
{
    "company_name": "Example Corp",
    "founded": "2001",
    "ceo": "Jane Doe",
    "industry": "Technology",
    "main_products": "Software, Hardware",
    "number_of_employees": "500",
    "headquarters": "New York, NY",
    "website": "www.example.com",
    "revenue": 1000000,
    "operating_income": 200000,
    "net_income": 150000,
    "total_assets": 5000000,
    "total_liabilities": 2000000,
    "total_equity": 3000000,
    "market_capitalization": 4000000,
    "stock_exchange": "NYSE",
    "profit_margin": "15%",
    "return_on_equity": "10%",
    "debt_to_equity_ratio": "0.67",
    "current_ratio": "1.5",
    "pe_ratio": "20",
    "dividend_yield": "2%",
    "revenue_growth": "5%",
    "rd_expenses": 100000,
    "customer_acquisition_cost": 200,
    "customer_lifetime_value": 1000,
    "market_share": "10%",
    "competitors": "Competitor A, Competitor B",
    "future_outlook": "Growth expected in the next quarter.",
    "recent_news": "1. New product launch.<br/>2. Expansion to Europe.<br/>3. Strategic partnership with Company B.",
    "esg_initiatives": "1. Carbon footprint reduction.<br/>2. Community engagement programs."
}
```

---
Test Results Report

Test Cases
| Test Case                | Input                                    | Expected Result                           | Actual Result                             | Status      |
|------------------------- |------------------------------------------|------------------------------------------|------------------------------------------|-------------|
| Generate PDF             | Valid company data                       | PDF file created successfully            | PDF file created successfully            | Pass        |
| Generate DOCX            | Valid company data                       | DOCX file created successfully           | DOCX file created successfully           | Pass        |
| Upload File              | Any file type                           | Success message returned                 | Success message returned                 | Pass        |
| Generate PDF             | Invalid company data (missing fields)   | 422 Unprocessable Entity error           | 422 Unprocessable Entity error           | Pass        |
| Generate DOCX            | Invalid company data (invalid types)    | 422 Unprocessable Entity error           | 422 Unprocessable Entity error           | Pass        |

Summary
All tested functionalities worked as expected, producing the desired output for valid inputs and appropriate errors for invalid inputs.

---

## Output File Examples

1. PDF Example: `Example_Corp_info.pdf`
   - The PDF file includes structured tables and styled text containing company information, financial metrics, and market outlook.

2. DOCX Example: `Example_Corp_template.docx`
   - The DOCX file contains placeholders for company data, structured in a table format.

---

Sample Input and Output Data

Sample Input Data
```json
{
    "company_name": "Tech Innovators Inc.",
    "founded": "2010",
    "ceo": "John Smith",
    "industry": "Software Development",
    "main_products": "Custom Software Solutions",
    "number_of_employees": "250",
    "headquarters": "San Francisco, CA",
    "website": "www.techinnovators.com",
    "revenue": 3000000,
    "operating_income": 800000,
    "net_income": 600000,
    "total_assets": 10000000,
    "total_liabilities": 4000000,
    "total_equity": 6000000,
    "market_capitalization": 8000000,
    "stock_exchange": "NASDAQ",
    "profit_margin": "20%",
    "return_on_equity": "12%",
    "debt_to_equity_ratio": "0.67",
    "current_ratio": "2.0",
    "pe_ratio": "15",
    "dividend_yield": "0%",
    "revenue_growth": "10%",
    "rd_expenses": 500000,
    "customer_acquisition_cost": 150,
    "customer_lifetime_value": 1200,
    "market_share": "5%",
    "competitors": "Innovative Solutions LLC, Future Tech",
    "future_outlook": "Steady growth with expansion plans.",
    "recent_news": "1. Expanded services to Europe.<br/>2. Acquired a startup.<br/>3. Launched a new product line.",
    "esg_initiatives": "1. Implemented green practices.<br/>2. Diversity and inclusion programs."
}
```

Sample Output Data
PDF Output: Contains structured tables with company details:
- Company Name: Tech Innovators Inc.
- Founded: 2010
- CEO: John Smith
- Industry: Software Development
- Main Products: Custom Software Solutions
- Number of Employees: 250
- Headquarters: San Francisco, CA
- Website: www.techinnovators.com
- Financial Metrics: Revenue, Operating Income, Net Income, etc.

DOCX Output: Contains structured sections with placeholders for each data field.

---
