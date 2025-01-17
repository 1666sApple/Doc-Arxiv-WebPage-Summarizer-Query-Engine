import sqlite3
import logging
from src.utils.logging_config import setup_logger

logger = setup_logger(__name__, "db.log")

class DatabaseManager:
    def __init__(self, db_path="rag.db"):
        self.db_path = db_path
        self.connection = None
        self._connect()

    def _connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self._initialize_tables()
            logger.info("Database connected and initialized.")
        except Exception as e:
            logger.exception(f"Error connecting to database: {str(e)}")

    def _initialize_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY,
                content TEXT,
                metadata TEXT
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS embeddings (
                id INTEGER PRIMARY KEY,
                document_id INTEGER,
                embedding BLOB,
                FOREIGN KEY (document_id) REFERENCES documents (id)
            );
            """)
            self.connection.commit()
            logger.info("Tables initialized successfully.")
        except Exception as e:
            logger.exception(f"Error initializing tables: {str(e)}")

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed.")
