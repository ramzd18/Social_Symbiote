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
import promptLLMmemories

os.environ["OPENAI_API_KEY"] = "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"

LLM = ChatOpenAI(max_tokens=800)  # Can be any LLM you want.
USER_NAME="Person A"
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
def update_vectorstore_with_memories(vectorstore):
   addMemories(vectorstore)
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

def interview_agent(agent: GenerativeAgent, message: str) -> str:
    new_message = f"{USER_NAME} says {message}"
    return agent.generate_dialogue_response(new_message)[1]




def get_agent_initial_data(): 
  ramprofile=create_agent()
  # ram_observations=promptLLMmemories.generate_relevant_memories("Generate memories for Ram. Ram is a college student who loves to watch football and play sports. He specifically spends a lot of money on basketball hoops and spikeball nets. Start the memories with Ram's name. Make each memory a full sentence")
  # for observation in ram_observations:
  #  ramprofile.memory.add_memory(observation)
  stored_dict=ramprofile.__dict__
  memory=ramprofile.memory.dict()
  memory=json.dumps(memory,default=str)
  print(type(memory))
  llm=ramprofile.llm.to_json()
  llm=json.dumps(llm)
  print(type(llm))
  name=stored_dict.get("name")
  age=stored_dict.get("age")
  status=stored_dict.get("status")
  print(type(name))
  print(type(age))
  print(type(status))
  return name,age,status,memory,llm

# name,age,status,memory,llm=add_data()
# print(name)
# for i in stored_dict.keys():
#     print(stored_dict.get(i))
#print(ramprofile.memory.to_json())
# #print(interview_agent(ramprofile, "What are your thoughts on abortion?"))  
# #pint(ramprofile.summarize_related_memories("Politics"))
# save_file = open("agentdata.json", "w")  
# json.dump(ramprofile.json,save_file, indent = 6)  
# save_file.close()  
