import os

from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ['LANGCHAIN_PROJECT']="LLM Test"



from langchain_core.output_parsers import StrOutputParser

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an helpful assisitant , Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#Streamlit
st.title("Langchain Demo with gemma")
input_text=st.text_input("What Question do u have in mind")


## Ollama mode
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))



