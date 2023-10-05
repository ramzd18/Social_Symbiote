from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"]="2a1b3c69c495a34d2328c393b729f971563d489b464266a90fcb0bd214ce452f"
llm = OpenAI(temperature=0)
tools = load_tools(["serpapi"])
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("Find a product online that user generative agents to simualte product research")