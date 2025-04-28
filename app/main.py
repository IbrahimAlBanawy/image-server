from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from app.routes.upload import upload_image  # Import upload route from another file
import os
from pathlib import Path

app = FastAPI()

# Directory where images will be stored
UPLOAD_DIR = Path(__file__).parent / "static" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Mount static directory for serving images
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

# Include the routes for image upload
app.include_router(upload_image)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}
