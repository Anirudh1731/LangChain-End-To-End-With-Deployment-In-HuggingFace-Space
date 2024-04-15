# Q and A chat bot
from langchain.llms import OpenAI

from dotenv import load_dotenv

#take variables from .env files
load_dotenv()

import streamlit as st

import os
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name='gpt-3.5-turbo-instruct',temperature=0.5)
    response=llm(question)
    return response

#initialize 

st.set_page_config(page_title="Q&A demo")

st.header("Langchain Application")

input=st.text_input("Input : ",key="input")
response=get_openai_response(input)
submit=st.button("Ask the question")

if submit:
    st.subheader("The response is ")
    st.write(response)
