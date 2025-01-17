import os
import logging

# Ensure the logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name: str, log_file: str, level=logging.INFO):
    """
    Sets up a logger with the given name, log file, and log level.

    Args:
        name (str): The name of the logger (usually the module name).
        log_file (str): The file where logs will be written.
        level (int): Logging level (e.g., logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler
    file_handler = logging.FileHandler(os.path.join(LOG_DIR, log_file))
    file_handler.setFormatter(formatter)

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Get logger and attach handlers
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # Prevent duplicate logging from multiple handlers
    logger.propagate = False

    return logger
