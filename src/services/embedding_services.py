from src.model.llm import LLMModel

class EmbeddingService:
    def __init__(self):
        self.llm_model = LLMModel()

    def generate_embeddings(self, documents: list) -> list:
        """
        Generate embeddings for the given documents.

        Args:
            documents (list): List of document content.

        Returns:
            list: List of embeddings.
        """
        embeddings = []
        for doc in documents:
            embedding = self.llm_model.get_llm("cohere").get_text_embedding(doc["content"])
            embeddings.append({"document": doc, "embedding": embedding})
        return embeddings
