"""
main.py - Command-line interface for text translation using LangChain.

This script allows users to input a target language and English text to translate.
It validates environment variables, logs their presence (with sensitive values masked),
and handles translations using the LangChain model.
"""

from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from utilities import configure_logging, log_loaded_env_vars, validate_env_vars, suppress_library_logs
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Validate environment variables
try:
    validate_env_vars()
except EnvironmentError as e:
    print(f"Configuration Error: {e}")
    exit(1)

# Configure logging
logger = configure_logging()

# Check DEBUG flag from environment
debug_mode = os.getenv("DEBUG", "false").lower() == "true"

# Suppress library logs if debug_mode is False
suppress_library_logs(debug_mode)

# Log loaded environment variables (with sensitive values masked)
if debug_mode:
    log_loaded_env_vars(logger)


# Fetch API key and model dynamically
api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default to gpt-3.5-turbo

# Initialize the Chat LLM
model = ChatOpenAI(model=model_name, temperature=0.7)

# Command-line interface for user interaction
while True:
    # Ask the user for the target language and the text to translate
    language = input("Enter the language you want to translate English to (or 'exit' to quit): ")
    if language.lower() == "exit":
        print("Goodbye!")
        break

    content = input("Enter the English text to translate: ")
    if content.lower() == "exit":
        print("Goodbye!")
        break

    # Prepare the messages
    messages = [
        SystemMessage(content=f"Translate the following from English to {language}:"),
        HumanMessage(content=content),
    ]

    # Generate a response using the LLM
    response = model.invoke(messages)

    # Display the response
    print(f"Translation to {language}: {response.content}")
