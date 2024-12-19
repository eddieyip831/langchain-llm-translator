"""
app.py - Streamlit frontend for text translation using LangChain.

This app allows users to input a target language and English text to translate.
It provides an easy-to-use interface for interacting with the LangChain AI model.
"""

import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from utilities import configure_logging, log_loaded_env_vars, validate_env_vars
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Validate environment variables
try:
    validate_env_vars()
except EnvironmentError as e:
    st.error(f"Configuration Error: {e}")
    st.stop()

# Configure logging
logger = configure_logging()

# Log loaded environment variables (with sensitive values masked)
log_loaded_env_vars(logger)

# Disable LangSmith tracing to avoid unnecessary API calls
os.environ["LANGCHAIN_TRACING_V2"] = "false"

# Fetch API key and model dynamically
api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default to gpt-3.5-turbo

# Initialize the Chat LLM
model = ChatOpenAI(model=model_name, temperature=0.7)

# Streamlit frontend setup
st.title("English to Target Language Translator")
st.write("Provide the target language and English text to translate.")

# Input fields for the target language and English text
language = st.text_input("Target Language (e.g., French, Spanish, German):")
content = st.text_area("English Text to Translate:")

# Button to trigger translation
if st.button("Translate"):
    if not language or not content:
        st.error("Please provide both the target language and the English text to translate.")
    else:
        # Prepare the messages
        messages = [
            SystemMessage(content=f"Translate the following from English to {language}:"),
            HumanMessage(content=content),
        ]

        # Generate a response using the LLM
        response = model.invoke(messages)

        # Display the translation
        st.write("**Translation Result:**")
        st.write(response.content)
