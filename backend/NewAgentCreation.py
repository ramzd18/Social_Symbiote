from datetime import datetime, timedelta
from typing import List
from termcolor import colored
from langchain_experimental.generative_agents import (
    GenerativeAgent,
    GenerativeAgentMemory,
)
import os
import math
import faiss
from langchain.chat_models import ChatOpenAI
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
import json

os.environ["OPENAI_API_KEY"] = "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"

USER_NAME = "Person A" 
LLM = ChatOpenAI(max_tokens=1000)  # Can be any LLM you want.

def relevance_score_fn(score: float) -> float:
    """Return a similarity score on a scale [0, 1]."""
    return 1.0 - score / math.sqrt(2)
def addMemories(vectorstore):
    loader = TextLoader(file_path="backend\Rampr.txt")
    document=loader.load()
    vectorstore.add_documents(document)
    return vectorstore
def create_new_memory_retriever():
    """Create a new vector store retriever unique to the agent."""
      # Define your embedding model
    embeddings_model = OpenAIEmbeddings()
      # Initialize the vectorstore as empty
    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(
          embeddings_model.embed_query,
          index,
          InMemoryDocstore({}),
          {},
          relevance_score_fn=relevance_score_fn,
      )
    timevectorstore= TimeWeightedVectorStoreRetriever(
          vectorstore=vectorstore, other_score_keys=["importance"], k=15
      )
    timevectorstore=addMemories(timevectorstore)
    return timevectorstore
def create_agent():
  ram_memory = GenerativeAgentMemory(
    llm=LLM,
    memory_retriever=create_new_memory_retriever(),
    verbose=False,
    reflection_threshold=25,  # we will give this a relatively low number to show how reflection works
)
  ram= GenerativeAgent(
    name="Ram",
    age=25,
    traits="talkative,social,emphatetic",
    status="very political active",  # You can add more persistent traits here
    memory_retriever=create_new_memory_retriever(),
    llm=LLM,
    memory=ram_memory,
)
  return ram; 
ramprofile=create_agent()
tommie_observations = [
    "Ram remembers his dog, Bruno, from when he was a kid",
    "Ram feels tired from driving so far",
    "Ram sees the new home",
    "The new neighbors have a cat",
    "The road is noisy at night",
    "Ram is hungry",
    "Ram tries to get some rest.",
]
for observation in tommie_observations:
    ramprofile.memory.add_memory(observation)
def interview_agent(agent: GenerativeAgent, message: str) -> str:
    new_message = f"{USER_NAME} says {message}"
    return agent.generate_dialogue_response(new_message)[1]
stored_dict=ramprofile.__dict__
jsonval=ramprofile.memory.to_json()
#ramprofile.memory.format_memories_detail(ramprofile.memory.parse_file)
jsonval=json.dumps(jsonval)
memory=stored_dict.get('memory')
print(type(jsonval))
print(stored_dict.get("name"))
print(stored_dict.get("age"))
print(stored_dict.get("status"))
print(stored_dict.get("llm"))
print(stored_dict.get("verbose"))



# for i in stored_dict.keys():
#     print(stored_dict.get(i))
#print(ramprofile.memory.to_json())
# #print(interview_agent(ramprofile, "What are your thoughts on abortion?"))  
# #print(ramprofile.summarize_related_memories("Politics"))
# save_file = open("agentdata.json", "w")  
# json.dump(ramprofile.json,save_file, indent = 6)  
# save_file.close()  
