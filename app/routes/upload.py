from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import os
from pathlib import Path

router = APIRouter()

# Directory where images will be stored
UPLOAD_DIR = Path(__file__).parent.parent / "static" / "uploads"

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Define the file path where the image will be saved
        file_path = UPLOAD_DIR / file.filename

        # Save the file locally
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Return the URL for accessing the uploaded file
        file_url = f"/static/uploads/{file.filename}"
        return JSONResponse(content={"message": "File uploaded successfully", "url": file_url})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
