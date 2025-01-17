from typing import List

class DocumentLoader:
    def __init__(self):
        pass

    def load_documents(self, file_paths: List[str]) -> List[dict]:
        """
        Load documents from file paths.

        Args:
            file_paths (List[str]): List of file paths.

        Returns:
            List[dict]: List of documents with content and metadata.
        """
        documents = []
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                documents.append({"content": content, "metadata": {"file_name": file_path}})
        return documents
