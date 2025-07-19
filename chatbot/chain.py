# chatbot/chain.py
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from .prompt import get_fitness_prompt
import os
from dotenv import load_dotenv

load_dotenv()

def build_chain():
    azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    llm = AzureChatOpenAI(
        openai_api_version="2024-02-15-preview",
        azure_endpoint=azure_endpoint,
        azure_deployment=azure_deployment,
        api_key=azure_api_key
    )

    prompt = get_fitness_prompt()
    output_parser = StrOutputParser()
    return prompt | llm | output_parser
