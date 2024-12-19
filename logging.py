import os
import logging

def configure_logging():
    """
    Configures logging for the application.

    Sets up a basic logging configuration with DEBUG level and a standard format 
    that includes timestamps, log levels, and messages.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logging.basicConfig(
        level=logging.DEBUG,  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

def mask_value(value, mask_length=4):
    """
    Masks sensitive values for secure logging.

    For values longer than the specified `mask_length`, masks all characters 
    except for the last `mask_length` characters. If the value is shorter than
    `mask_length`, it returns the value as is.

    Args:
        value (str): The sensitive value to be masked.
        mask_length (int): The number of characters to remain unmasked. Default is 4.

    Returns:
        str: The masked value.
    """
    if len(value) > mask_length:
        return "*" * (len(value) - mask_length) + value[-mask_length:]
    return value

def log_loaded_env_vars(logger):
    """
    Logs all loaded environment variables with sensitive values masked.

    Uses the provided logger to output environment variable names and their values.
    Sensitive values containing 'KEY' or 'SECRET' in their names are masked for security.

    Args:
        logger (logging.Logger): The logger instance used for logging.
    """
    logger.debug("Loaded Environment Variables:")
    for key, value in os.environ.items():
        if "KEY" in key or "SECRET" in key:  # Identify sensitive variables
            masked_value = mask_value(value)
            logger.debug(f"{key}: {masked_value}")
        else:
            logger.debug(f"{key}: {value}")
