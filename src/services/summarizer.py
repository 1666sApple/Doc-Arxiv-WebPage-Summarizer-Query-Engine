from src.model.llm import LLMModel

class Summarizer:
    def __init__(self):
        self.llm_model = LLMModel()

    def summarize(self, document_content: str) -> str:
        """
        Summarize the content of a document.

        Args:
            document_content (str): Document content.

        Returns:
            str: Summarized content.
        """
        llm = self.llm_model.get_llm("groq")
        summary = llm.complete(prompt=f"Summarize the following document:\n\n{document_content}")
        return summary
