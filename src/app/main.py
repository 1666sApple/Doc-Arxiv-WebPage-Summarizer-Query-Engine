from fastapi import FastAPI
from src.app.endpoints import rag_routes
from src.utils.logging_config import setup_logger

# Initialize FastAPI app
app = FastAPI(
    title="RAG System for Document Summarization",
    description="A Retrieval-Augmented Generation (RAG) system using FastAPI",
    version="1.0.0",
)

# Setup logging
logger = setup_logger(__name__, "app.log")

# Include routes
app.include_router(rag_routes.router)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the RAG System for Document Summarization!"}
