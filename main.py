from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
from uuid import uuid4
import os

app = FastAPI()
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid4())
    filepath = os.path.join(UPLOAD_DIR, file_id + "_" + file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())
    return {"url": f"https://<your-render-subdomain>.onrender.com/file/{file_id}_{file.filename}"}

@app.get("/file/{filename}", response_class=FileResponse)
def get_file(filename: str):
    filepath = os.path.join(UPLOAD_DIR, filename)
    return FileResponse(path=filepath)
