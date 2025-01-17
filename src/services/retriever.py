import numpy as np

class Retriever:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def cosine_similarity(self, vector_a, vector_b):
        return np.dot(vector_a, vector_b) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))

    def retrieve_similar(self, query_embedding, top_k=5):
        cursor = self.db_manager.connection.cursor()
        cursor.execute("SELECT document_id, embedding FROM embeddings")
        results = cursor.fetchall()

        similarities = []
        for doc_id, embedding_blob in results:
            embedding = np.frombuffer(embedding_blob, dtype=np.float32)
            similarity = self.cosine_similarity(query_embedding, embedding)
            similarities.append((doc_id, similarity))

        # Sort by similarity and retrieve top-k
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_documents = similarities[:top_k]
        return top_documents
