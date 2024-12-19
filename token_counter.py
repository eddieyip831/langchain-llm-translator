"""
token_counter.py - A utility to count input and output tokens used in OpenAI API requests.

This module calculates the number of tokens in input text using the tiktoken library
and estimates the tokens in the output based on the response length. The model name
is dynamically loaded from environment variables, ensuring flexibility.

Modules:
    - tiktoken: Used for tokenizing text based on the OpenAI model.
    - os: For accessing environment variables.
    - dotenv: To load environment variables from a `.env` file.

Functions:
    - count_tokens: Counts the number of tokens in a given text for the specified model.
    - display_token_usage: Calculates and returns token counts for input and output texts.

Usage Example:
    >>> from token_counter import display_token_usage
    >>> usage = display_token_usage("Hello, world!", "Bonjour le monde!")
    >>> print(usage)
    {'input_tokens': 3, 'output_tokens': 3}
"""

import tiktoken
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the model name from the environment variables
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default to gpt-3.5-turbo

def count_tokens(text, model=MODEL_NAME):
    """
    Counts the number of tokens in the given text for the specified model.

    Args:
        text (str): The input text to encode.
        model (str): The name of the model tokenizer to use (default: loaded from .env).

    Returns:
        int: The number of tokens in the input text.
    """
    # Get the tokenizer for the model
    enc = tiktoken.encoding_for_model(model)
    # Encode the text and count tokens
    return len(enc.encode(text))

def display_token_usage(input_text, output_text, model=MODEL_NAME):
    """
    Displays the token usage for both input and output text.

    Args:
        input_text (str): The input text sent to the model.
        output_text (str): The response text from the model.
        model (str): The name of the model tokenizer to use (default: loaded from .env).

    Returns:
        dict: A dictionary containing input and output token counts.
    """
    input_tokens = count_tokens(input_text, model)
    output_tokens = count_tokens(output_text, model)
    
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens
    }
