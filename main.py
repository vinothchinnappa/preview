from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from docx import Document
import uvicorn

app = FastAPI()

@app.post("/preview-docx/", response_class=HTMLResponse)
async def preview_docx(file: UploadFile = File(...)):
    if not file.filename.endswith(".docx"):
        return "<p>Only DOCX files are supported.</p>"

    contents = await file.read()
    with open("/tmp/temp.docx", "wb") as f:
        f.write(contents)

    doc = Document("/tmp/temp.docx")
    html_output = "<div style='font-family: Arial;'>"
    for para in doc.paragraphs:
        html_output += f"<p>{para.text}</p>"
    html_output += "</div>"

    return html_output
