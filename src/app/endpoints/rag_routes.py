from fastapi import APIRouter, UploadFile, File, Form
from src.services.pipeline import RAGPipeline
import os
from typing import List

# Initialize the router
router = APIRouter(prefix="/rag", tags=["RAG System"])

# Initialize RAG pipeline
rag_pipeline = RAGPipeline()

# Directory to temporarily store uploaded files
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload/")
async def upload_documents(files: List[UploadFile] = File(...)):
    """
    Upload documents for processing and embedding.

    Args:
        files (List[UploadFile]): List of uploaded files.

    Returns:
        dict: Status of upload and processing.
    """
    file_paths = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        file_paths.append(file_path)

    # Process the uploaded documents
    rag_pipeline.process_documents(file_paths)

    return {"message": "Documents uploaded and processed successfully."}

@router.post("/query/")
async def query_rag_system(query: str = Form(...)):
    """
    Query the RAG system and retrieve summarized results.

    Args:
        query (str): User query.

    Returns:
        dict: Summarized results.
    """
    results = rag_pipeline.query(query)
    return {"query": query, "results": results}
