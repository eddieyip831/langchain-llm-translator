import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LLM
llm = OpenAI(model_name="text-davinci-003", temperature=0.7)

# Prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer this question: {question}"
)

# LLM Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit frontend
st.title("LangChain LLM Chain")
st.write("Ask any question, and get an AI-generated answer!")

question = st.text_input("Your Question:")
if st.button("Get Answer"):
    response = chain.run(question=question)
    st.write("**Answer:**", response)
