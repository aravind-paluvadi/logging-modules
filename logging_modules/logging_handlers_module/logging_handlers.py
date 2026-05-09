""" Logging Config with Handlers """
# Standard Imports
import os
import sys
import logging
from datetime import datetime


def logging_with_handlers(
        log_set_level: str = "DEBUG",
        log_directory: str = None,
        log_file_name: str = None
):
    """
    Logging Configuration with Handlers
    Parameters:
    ----------
        log_set_level:
            The logging level to set (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
        log_directory:
            The directory where log files will be stored (default: "my_app/logs")
        log_file_name:
            The base name for the log file (default: "app")
    """
    # Create logs directory if it doesn't exist
    log_dir = log_directory or "my_app/logs"
    os.makedirs(log_dir, exist_ok=True)

    # Create log filename with today's date
    today_date = datetime.now().strftime("%Y%m%d")
    log_filename = f"{log_file_name}_log_{today_date}.txt"
    log_fil_path = os.path.join(log_dir, log_filename)

    # Configure logging to both console and file
    log_format = '[%(asctime)s] %(levelname)s: %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    # Set logging level based on verbose flag
    log_level = logging.DEBUG if log_set_level else logging.INFO

    # Clear any existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Configure logging
    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_fil_path, mode="w"),
            logging.StreamHandler(sys.stdout)
        ]
    )


"""Place this in the another file you want to log the data"""
logger = logging.getLogger(__name__)

logger.info("Test Logging with Handler")
