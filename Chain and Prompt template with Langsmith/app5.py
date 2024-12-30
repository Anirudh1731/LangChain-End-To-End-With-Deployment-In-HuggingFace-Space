from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_community.llms.ollama import Ollama

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a AI researcher . Please respond in the same manner "),
        ("user","Question:{question}")
    ]
)


model = Ollama(model="gemma:2b")

#model=ChatOpenAI(model="gpt-4o-mini")
output_parser=StrOutputParser()

chain=prompt|model|output_parser
question="Can u summarize activation function"



print(chain.invoke({"question":question}))



