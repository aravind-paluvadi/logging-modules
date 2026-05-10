# Logging Modules

## Overview:
This module provides a simple logging mechanism for applications.
- It allows developers to log messages with different severity levels (e.g., INFO, WARNING, ERROR)
- Supports various output formats (e.g., console, file).

## Lanaguage:
- Python

## Usage:
1. Import the logging module:
   ```python
   import logging
   from logging_modules.basic_logging_module import setup_logging
   ```
2. Configure the logging settings (e.g., log level, output format):
   ```python
   setup_logging(logging.INFO)
   ```
3. Log messages using the appropriate logging methods:
   ```python
   logger = logging.getLogger(__name__)

   logger.info("This is an informational message.")
   logger.warning('This is a warning message.')
   logger.error('This is an error message.')
   ```
Note: 
- The `setup_logging` function is a helper function that configures the logging settings based on the provided log level. 
You can customize it further to include additional handlers or formatters as needed.

## Project Structure:
```
logging_modules/
      ├── logging_modules/   
      │     ├── basic_logging_module      # Module for Basic logging configuration and setup
      │     │     ├── __init__.py
      │     │     └── basic_logging.py      # Basic logging setup and configuration
      │     │
      │     ├── logging_dict_config_module  # Module for Logging configuration using a dictionary
      │     │     ├── __init__.py
      │     │     └── logging_dict_config.py  # Logging configuration using a dictionary
      │     │
      │     ├── logging_handlers_module     # Module for Custom logging handlers (e.g., console, file)
      │     │     ├── __init__.py
      │     │     └── logging_handlers.py     # Custom logging handlers for console and file output
      │     │
      │     └── logging_json_file_module    # Module for Logging configuration using a JSON file
      │           ├── __init__.py
      │           ├── logging_config.py       # Logging configuration using a JSON file
      │           └── logging_json_file.py    # Logging setup using a JSON file
      │
      ├── .gitignore
      └── README.md
```

## Benefits:
- Provides a standardized way to log messages across an application.
- Helps in debugging and monitoring application behavior.
- Can be easily extended to support additional logging handlers (e.g., email, database).

## Conclusion:
- The logging module is an essential tool for developers to track the flow of their applications and identify issues effectively. 
- By using this module, you can ensure that your application logs important information in a consistent and organized manner, 
making it easier to maintain and troubleshoot.
- These modules are just examples and can be further enhanced with additional features such as log rotation, 
asynchronous logging, or integration with external logging services.
