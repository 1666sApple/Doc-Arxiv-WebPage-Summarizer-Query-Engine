import os
import logging
from src.utils.logging_config import setup_logger
from dotenv import load_dotenv

logger = setup_logger(__name__, "config.log")

class ConfigManager:
    def __init__(self):
        """
        Initial ConfigManager to load environment variables
        """
        logging.info("Initialize ConfigManager")
        try:
            load_dotenv()
            self.groq_api=os.getenv("GROQ_API_KEY")
            self.cohere_api=os.getenv("COHERE_API_KEY")
            self.rdbms="multiple_rag.db"
            self.qdrant_api=os.getenv("QDRANT_API_KEY")
            self.together_api=os.getenv("TOGETHER_API_KEY")
            self.groq_model=os.getenv("GROQ_MODEL")
            self.cohere_model=os.getenv("COHERE_MODEL")
            self.together_model=os.getenv("TOGETHER_MODEL")
            self.google_api=os.getenv("GOOLGE_API_KEY")
            self.google_model=os.getenv("GOOLGE_MODEL")

            logging.info("Environment Variables loaded successfully!")

        except Exception as e:
            logging.exception("Error retrieving Azure configuration: %s", str(e))

    def get_llm_config(self):
        try:
            llm_config = {
                "groq_api" : self.groq_api,
                "groq_model" : self.groq_model,
                "cohere_api" : self.cohere_api,
                "cohere_model" : self.cohere_model,
                "together_api" : self.together_api,
                "together_model" : self.together_model,
                "google_api" : self.google_api,
                "google_model" : self.google_model
            }

            logging.info("LLM Configurations retrieved.")

            return llm_config

        except Exception as e:
            logging.exception("Error retrieving configuration: %s", str(e))
            return {}
