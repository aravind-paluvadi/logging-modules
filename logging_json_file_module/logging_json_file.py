""" Reading a JSON File for Config     """
# Standard Imports
from json import load
from pathlib import Path
import logging.config


def logging_setup() -> None:
    """
    Function with JSON file logging setup
    """
    config_file = Path("logging_json_file_module/logging_config.json")
    with open(config_file) as json_file:
        config_log = load(json_file)
    logging.config.dictConfig(config=config_log)


"""Place this in the another file you want to log the data"""
logger = logging.getLogger(__name__)

logger.info("Test Logging")
