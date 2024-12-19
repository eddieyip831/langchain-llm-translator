from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LLM
llm = OpenAI(model_name="text-davinci-003", temperature=0.7)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer this question: {question}"
)

# Chain LLM with the prompt
chain = LLMChain(llm=llm, prompt=prompt)

# Interactive input
while True:
    user_input = input("Enter your question (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    response = chain.run(question=user_input)
    print(f"Answer: {response}")
