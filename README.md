# AI-Based-PDF-Filler-Project-Proposal-WeCommit-SprintProgram 🤖📝

**Technical Documentation**

_Overview
_This FastAPI application generates PDF and DOCX files containing company information using data received from API requests. The application utilizes Tortoise ORM for database interactions and ReportLab for PDF generation. The data structure is validated using Pydantic models.

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
```cmd
python -m uvicorn main:app --reload --host localhost --port 8080
```
The application will be accessible at `http://localhost:8080/`.

API Endpoints
- Upload File: `POST /upload/` - Uploads a file (currently a placeholder).
- Generate PDF: `POST /generate-pdf/` - Generates a PDF from provided company data.
- Generate DOCX: `POST /generate-docx/` - Generates a DOCX from provided company data.

Sure! Here’s the updated version with the new sample input and output data structured as you requested. I've rephrased and summarized the information accordingly.

---

Example Input
The following JSON structure can be used to test the PDF and DOCX generation endpoints:

```json
{
    "company_name": "WECOMMIT dummy Inc.",
    "founded": "2005-03-15",
    "industry": "Information Technology",
    "net_income": 52000000,
    "financial_ratios": {
        "profit_margin": "11.56%",
        "current_ratio": 2.5,
        "debt_to_equity_ratio": 0.60
    },
    "future_outlook": [
        "Asian market expansion next fiscal year",
        "Focus on sustainable tech",
        "20% growth expected in cloud services"
    ],
    "main_products": "Cloud Computing Services, AI Solutions, Data Analytics Tools",
    "customer_lifetime_value": 50000,
    "carbon_neutrality": {
        "target_year": "2030",
        "goal": "Achieve net-zero carbon emissions across all operations and supply chain"
    },
    "board_representation": {
        "women_on_board": {
            "number": 40,
            "percentage": "40%"
        },
        "women_in_leadership": "Data not provided"
    },
    "cloud_services_growth_rate": "20%",
    "years_since_founded": 19
}
```

---

Sample Output Data

PDF Output: The generated PDF contains structured tables and styled text with the following details:

- Company Name: WECOMMIT dummy Inc.
- Founded: 2005-03-15
- Industry: Information Technology
- Net Income: $52,000,000

Financial Ratios:
1. Profit Margin**: 11.56%
2. Current Ratio: 2.5
3. Debt to Equity Ratio: 0.60

Future Outlook Summary:
1. Asian market expansion next fiscal year
2. Focus on sustainable tech
3. 20% growth expected in cloud services

Main Products: Cloud Computing Services, AI Solutions, Data Analytics Tools  
Customer Lifetime Value: $50,000  

---

### FAQs in Output

- Q: What is WECOMMIT dummy Inc.'s specific target year for achieving carbon neutrality, and what does this goal entail?  
  A: 
  - Target Year: By the end of 2030  
  - Goal: Achieve net-zero carbon emissions across all operations and supply chain  

- Q: How many women are on the board of directors of WECOMMIT dummy Inc., and what percentage of the board does this represent? Additionally, what is the representation of women in executive leadership positions?  
  A: Based solely on the statement "40% of board members are women," we cannot provide complete answers to the questions asked.  

- Q: What is the projected growth rate for WECOMMIT dummy Inc.'s cloud services division in the upcoming fiscal year?  
  A: 20%  

- Q: How many years has it been since WECOMMIT dummy Inc. was founded from now?  
  A: 19 years  

---

DOCX Output
The generated DOCX file includes structured sections with placeholders for each data field and summarizes the information presented in the PDF format.

---

# LICENSE
This project is licensed under the **Creative Commons Zero v1.0 Universal**
The Creative Commons CC0 Public Domain Dedication waives copyright interest in a work you've created and dedicates it to the world-wide public domain. Use CC0 to opt out of copyright entirely and ensure your work has the widest reach. As with the Unlicense and typical software licenses, CC0 disclaims warranties. CC0 is very similar to the Unlicense.

---
