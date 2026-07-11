from picoagents.llm import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
load_dotenv()


client = OpenAIChatCompletionClient(
    base_url= os.getenv("OPENAI_BASE_URL"),
    api_key= os.getenv("OPENAI_API_KEY"),
    model= os.getenv("OPENAI_MODEL"),
)
