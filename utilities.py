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
    Only logs if the DEBUG flag is set to true in the environment.

    Args:
        logger (logging.Logger): The logger instance used for logging.
    """
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"  # Convert to lowercase for safety
    if not debug_mode:
        return

    logger.debug("Loaded Environment Variables:")
    for key, value in os.environ.items():
        if "KEY" in key or "SECRET" in key:  # Identify sensitive variables
            masked_value = mask_value(value)
            logger.debug(f"{key}: {masked_value}")
        else:
            logger.debug(f"{key}: {value}")

def validate_env_vars():
    """
    Validates that all required environment variables are loaded properly.
    Raises an error if any required environment variable is missing.
    """
    required_vars = ["OPENAI_API_KEY", "OPENAI_MODEL"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}. "
            "Ensure these are set in your .env file or system environment."
        )

def suppress_library_logs(debug_mode):
    """
    Suppress excessive logs from libraries like OpenAI, LangChain, and LangSmith
    based on the DEBUG flag.

    Args:
        debug_mode (bool): Whether debugging is enabled (determined by the DEBUG flag).
    """
    if not debug_mode:
        # Suppress debug logs for specific libraries
        logging.getLogger("openai").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("langchain").setLevel(logging.WARNING)
        logging.getLogger("langsmith").setLevel(logging.WARNING)
    else:
        # Ensure debug logs are enabled for your app and libraries
        logging.getLogger("openai").setLevel(logging.DEBUG)
        logging.getLogger("httpcore").setLevel(logging.DEBUG)
        logging.getLogger("httpx").setLevel(logging.DEBUG)
        logging.getLogger("langchain").setLevel(logging.DEBUG)
        logging.getLogger("langsmith").setLevel(logging.DEBUG)
