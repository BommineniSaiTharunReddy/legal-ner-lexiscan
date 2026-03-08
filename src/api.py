from fastapi import FastAPI, UploadFile, File
import shutil
import os

from src.extract_entities import extract_entities_from_pdf

app = FastAPI()

UPLOAD_FOLDER = "temp_uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/extract")
async def extract_entities(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    entities = extract_entities_from_pdf(file_path)

    return {
        "filename": file.filename,
        "entities": entities
    }