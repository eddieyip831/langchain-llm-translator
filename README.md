## **LangChain LLM Translator**
This project is a Python-based application that uses LangChain to interact with OpenAI's GPT models. It provides a command-line and Streamlit-based interface for translating English text into various target languages.

---

### **Features**
- **Two Interfaces**:
  - **Command-Line Interface (CLI)** for terminal-based interactions.
  - **Streamlit Web App** for a user-friendly GUI.
- **Dynamic Target Language**: Translate English text into any specified language.
- **Environment Validation**: Ensures required environment variables are properly loaded before execution.
- **Debug Mode**:
  - Provides detailed logging when `DEBUG=true` in `.env`.
  - Suppresses verbose third-party logs when `DEBUG=false`.
- **Masked Logging**: Masks sensitive values (e.g., API keys) in logs for security.

---

### **Installation**

#### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/langchain-llm-translator.git
cd langchain-llm-translator
```

#### **2. Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Configure Environment Variables**
Create a `.env` file in the root directory:
```plaintext
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-3.5-turbo  # Or another supported model
DEBUG=true
```

**Important:** Replace `your_openai_api_key` with your own OpenAI API key. You can obtain one by creating an account at [OpenAI](https://platform.openai.com/signup/).

---

### **Usage**

#### **Command-Line Interface (CLI)**
Run the `main.py` script for terminal-based translations:
```bash
python main.py
```

**Example Interaction**:
```plaintext
Enter the language you want to translate English to (or 'exit' to quit): French
Enter the English text to translate: Hello, how are you?
Translation to French: Bonjour, comment ça va ?
```

#### **Streamlit Web App**
Run the Streamlit app for a web-based interface:
```bash
streamlit run app.py
```

Open the app in your browser (default: `http://localhost:8501`) and follow the prompts.

---

### **Project Structure**
```
langchain-llm-translator/
├── app.py               # Streamlit-based web app
├── main.py              # Command-line interface (CLI)
├── utilities.py         # Utility functions (logging, validation, etc.)
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md            # Project documentation
```

---

### **Key Components**

#### **Environment Variable Validation**
The project validates required environment variables (`OPENAI_API_KEY`, `OPENAI_MODEL`, etc.) before running the app. Missing variables result in a clear error message.

#### **Debug Logging**
- Set `DEBUG=true` in `.env` to enable verbose logging.
- Masked sensitive information ensures security in logs.

#### **Language Translation**
Uses OpenAI's `gpt-3.5-turbo` or other GPT models via LangChain to translate English text into a specified target language.

---

### **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### **Acknowledgments**
- [LangChain](https://github.com/hwchase17/langchain) for the modular AI framework.
- [Streamlit](https://streamlit.io/) for the interactive web interface.
- [OpenAI](https://openai.com/) for GPT-based language models.