from src.db.db import DatabaseManager
from src.services.document_loader import DocumentLoader
from src.services.embedding_services import EmbeddingService
from src.services.retriever import Retriever
from src.services.summarizer import Summarizer

class RAGPipeline:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.document_loader = DocumentLoader()
        self.embedding_service = EmbeddingService()
        self.retriever = Retriever(self.db_manager)
        self.summarizer = Summarizer()

    def process_documents(self, file_paths):
        # Step 1: Load documents
        documents = self.document_loader.load_documents(file_paths)

        # Step 2: Generate embeddings
        embeddings = self.embedding_service.generate_embeddings(documents)

        # Step 3: Store documents and embeddings in the database
        for doc, embedding in zip(documents, embeddings):
            cursor = self.db_manager.connection.cursor()
            cursor.execute("INSERT INTO documents (content, metadata) VALUES (?, ?)",
                           (doc["content"], str(doc["metadata"])))
            document_id = cursor.lastrowid
            cursor.execute("INSERT INTO embeddings (document_id, embedding) VALUES (?, ?)",
                           (document_id, embedding["embedding"].tobytes()))
        self.db_manager.connection.commit()

    def query(self, query_text):
        # Step 1: Generate query embedding
        query_embedding = self.embedding_service.generate_embeddings([{"content": query_text}])[0]["embedding"]

        # Step 2: Retrieve similar documents
        similar_documents = self.retriever.retrieve_similar(query_embedding)

        # Step 3: Summarize similar documents
        summaries = []
        for doc_id, similarity in similar_documents:
            cursor = self.db_manager.connection.cursor()
            cursor.execute("SELECT content FROM documents WHERE id = ?", (doc_id,))
            document = cursor.fetchone()[0]
            summary = self.summarizer.summarize(document)
            summaries.append({"document_id": doc_id, "similarity": similarity, "summary": summary})
        return summaries
