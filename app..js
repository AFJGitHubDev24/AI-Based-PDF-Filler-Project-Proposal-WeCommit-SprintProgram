document.addEventListener("DOMContentLoaded", function() {
    const pdfForm = document.getElementById("pdfForm");
    const knowledgeForm = document.getElementById("knowledgeForm");
    const uploadResult = document.getElementById("uploadResult");
    const knowledgeBaseList = document.getElementById("knowledgeBaseList");

    // Handle PDF upload form submission
    pdfForm.addEventListener("submit", async function(event) {
        event.preventDefault();
        const formData = new FormData();
        const pdfFile = document.getElementById("pdfFile").files[0];
        formData.append("pdf", pdfFile);

        try {
    const response = await fetch("/pdf/upload/", {
        method: "POST",
        body: formData
    });
    if (!response.ok) {
        throw new Error("Upload failed");
    }
    const data = await response.json();
    uploadResult.innerHTML = `PDF uploaded: <a href="/pdf/download/${data.output_file}" target="_blank">Download Processed PDF</a>`;
} catch (error) {
    console.error("Error:", error);  // Log the error to the console for more details
    uploadResult.innerHTML = "Error uploading PDF!";
}

    });

    // Handle knowledge base form submission
    knowledgeForm.addEventListener("submit", async function(event) {
        event.preventDefault();
        const fieldName = document.getElementById("field_name").value;
        const value = document.getElementById("value").value;

        try {
            const response = await fetch("/knowledge/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ field_name: fieldName, value: value })
            });
            const data = await response.json();
            addKnowledgeBaseRow(data.field_name, data.value);
        } catch (error) {
            knowledgeBaseList.innerHTML = "Error adding to Knowledge Base!";
        }
    });

    // Function to add a row to the knowledge base table
    function addKnowledgeBaseRow(field_name, value) {
        const tableBody = document.querySelector("#knowledgeTable tbody");
        const row = document.createElement("tr");
        row.innerHTML = `<td>${field_name}</td><td>${value}</td>`;
        tableBody.appendChild(row);
    }

    // Fetch existing knowledge base entries on load
    async function fetchKnowledgeBase() {
        try {
            const response = await fetch("/knowledge/");
            const data = await response.json();
            data.forEach(item => {
                addKnowledgeBaseRow(item.field_name, item.value);
            });
        } catch (error) {
            console.error("Error fetching Knowledge Base:", error);
        }
    }

    fetchKnowledgeBase();
});
