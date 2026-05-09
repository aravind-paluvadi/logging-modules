"""   Basic Logging Config   """
# Standard Imports
import logging


# Run this function where the project initializes
def setup_logging(log_level) -> None:
    """
    Function with logging setup to initialize logging

    Parameters:
    ----------
        log_level:
            The logging level to set (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
    """
    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s %(levelname)s %(name)s:%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            # filename="basic.log"
        )


"""Place this in the another file you want to log the data"""
logger = logging.getLogger(__name__)

logger.info("Test Basic Logging")
