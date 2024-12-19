# LangChain LLM Chain Tutorial with Streamlit Frontend

This project demonstrates the implementation of an LLM chain with a Streamlit-based frontend interface.

## Features
- Integration with OpenAI GPT.
- Custom prompt chaining using LangChain.
- Interactive frontend built with Streamlit.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/langchain-llm-streamlit.git
   cd langchain-llm-streamlit
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key in the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Example Workflow
- Use the Streamlit frontend to ask questions and get AI-generated answers.
