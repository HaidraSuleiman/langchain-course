from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch



llm = ChatOpenAI(model='gpt-4.1-mini')
tools = [TavilySearch()]
agent = create_agent(model=llm, tools= tools)

def main():
    result = agent.invoke({'messages':HumanMessage(content='Search for 3 job postings for an AI engineer using langchain on linkedIn in Cardiff area nad list their details ')})
    print(result)


if __name__ == "__main__":
    main()
