import os
import logging
from src.utils.logging_config import setup_logger
from llama_index.llms.groq import Groq
from src.config.config import ConfigManager
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.llms.together import TogetherLLM
from llama_index.llms.gemini import Gemini

# Configure logging
logger = setup_logger(__name__, "llm_model.log")

class LLMModel:
    def __init__(self):
        """
        Initializes the LLM model by loading configurations from ConfigManager.
        """
        logging.info("Initializing LLMs")

        try:
            config_manager = ConfigManager()
            llm_config = config_manager.get_llm_config()

            # Initialize Groq LLM
            self.llm_groq = Groq(
                model=llm_config['groq_model'],
                api_key=llm_config['groq_api']
            )
            logging.info("Groq LLM initialized successfully.")

            # Initialize Cohere Embedding
            self.embed_cohere = CohereEmbedding(
                api_key=llm_config["cohere_api"],
                model_name=llm_config["cohere_model"],
                input_type="search_document",
            )
            logging.info("Cohere Embedding initialized successfully.")

            # Initialize Together LLM
            self.llm_together = TogetherLLM(
                model=llm_config["together_model"],
                api_key=llm_config["together_api"],
            )
            logging.info("Together LLM initialized successfully.")

            # # Optionally, initialize Gemini LLM if needed
            # self.llm_gemini = Gemini(
            #     model=llm_config["google_model"],
            #     api_key=llm_config["google_api"]
            # )
            # logging.info("Gemini LLM initialized successfully.")

        except Exception as e:
            logging.exception(f"Error initializing LLMModel: {str(e)}")
            raise

    def get_llm(self, llm_type: str):
        """
        Returns the requested LLM instance based on the type.

        Args:
            llm_type (str): The type of LLM to retrieve. Options: 'groq', 'cohere', 'together', 'gemini'.

        Returns:
            object: The corresponding LLM instance.

        Raises:
            ValueError: If the specified LLM type is not supported.
        """
        try:
            if llm_type == "groq":
                return self.llm_groq
            elif llm_type == "cohere":
                return self.embed_cohere
            elif llm_type == "together":
                return self.llm_together
            # elif llm_type == "gemini":
            #     return self.llm_gemini
            else:
                raise ValueError(f"Unsupported LLM type: {llm_type}")
        except Exception as e:
            logging.exception(f"Error retrieving LLM instance: {str(e)}")
            raise
