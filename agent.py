from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch

from reels_tools import get_creator_transcriptions, list_available_creators

from dotenv import load_dotenv

load_dotenv()

copywriter = create_agent(
    model=init_chat_model('openai:gpt-4.1-mini'),
    tools=[
        TavilySearch(),
        get_creator_transcriptions,
        list_available_creators
        ],
    system_prompt=open('prompts/copywriter.md').read()
)