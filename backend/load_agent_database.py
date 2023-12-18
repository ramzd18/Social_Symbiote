import retrieve_agent
# from langchain_experimental.generative_agents import (
#     GenerativeAgent,
#     GenerativeAgentMemory,
# )
from langchain_experimental import generative_agents

from langchain.chat_models import ChatOpenAI
import json
import NewAgentCreation
import faiss
from langchain.chat_models import ChatOpenAI
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document
import json
import datetime
import os
import warnings


os.environ["OPENAI_API_KEY"]="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"
def LoadAgent(email,agent_name): 
  warnings.filterwarnings("ignore")
  LLM = ChatOpenAI(model_name="gpt-3.5-turbo-1106") 
  agent_data= retrieve_agent.retrieve_agents_record(email,agent_name)
  if agent_data=="Error":
    return "Agent data is not in database"
  else:
    print("1")
    agent_data_1=agent_data[3]
    memory= (eval((str(agent_data_1))))
    stream=memory['memory_stream']
    Document_list= []
    memory_retriever= create_new_memory_retriever()

    for i in stream: 
      metadataval=i['metadata']
      datetimeobj= datetime.datetime.strptime('13-03-21 06:33:13','%d-%m-%y %H:%M:%S')
      #  datetime.datetime.strptime(i['metadata']["last_accessed_at"],'%y-%m-%d')
      metadataval["last_accessed_at"] = i['metadata']["last_accessed_at"]
      metadataval["created_at"] = i['metadata']["created_at"]
      document= Document(page_content=i.get('page_content'),metadata=metadataval)
      Document_list.append(document)
    print("2")
    timeweightedstore=add_existing_memories_vectorstore(memory_retriever,Document_list)
    name= str(agent_data[0])
    age= int(agent_data[1])
    status= str(agent_data[2])
    social_media_memory= eval((str(agent_data[7])))
    social_stream=social_media_memory['memory_stream']
    social_list= []
    social_media_mem_retriever= create_new_memory_retriever()

    for i in social_stream: 
      i=dict(i)
      print("iterate")
      metadataval=i['metadata']
      # datetimeobj= datetime.strptime('13-03-21 06:33:13','%d-%m-%y %H:%M:%S')
      metadataval["last_accessed_at"] = i['metadata']["last_accessed_at"]
      metadataval["created_at"] = i['metadata']["created_at"]
      document= Document(page_content=i.get('page_content'),metadata=metadataval)
      social_list.append(document)
      social_media_mem_retriever.add_documents([document])
    print("3")
    # socialtimeeweightedstore= add_existing_memories_vectorstore(social_media_mem_retriever,social_list)
    socialtimeeweightedstore=social_media_mem_retriever
    print("4")
    education_work = str(agent_data[8])
    personalitylist= dict(agent_data[9])
    interests= str(agent_data[10])

    agent_memory = generative_agents.GenerativeAgentMemory(
    llm=LLM,
    memory_retriever=timeweightedstore,
    social_media_memory=socialtimeeweightedstore,
    product_memory= create_new_memory_retriever(),
    verbose=False,
    reflection_threshold=1000,  # we will give this a relatively low number to show how reflection works
    )
  agent= generative_agents.GenerativeAgent(
    name=name,
    age=age,
    traits="talkative,social,emphatetic",
    status=status, 
    education_and_work=education_work,
    interests=interests,
    llm=LLM,
    memory=agent_memory,
)

  return agent

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
          relevance_score_fn=NewAgentCreation.relevance_score_fn,
      )
    timevectorstore= TimeWeightedVectorStoreRetriever(
          vectorstore=vectorstore, other_score_keys=["importance"], k=15
      )
    #timevectorstore=ad(timevectorstore)
    return timevectorstore
def add_existing_memories_vectorstore(vectorstore,document_list):
    vectorstore.add_documents(document_list)
    return vectorstore

#     return ram
    
def split_into_three(lst):
    # Divide the length of the list by 3
    split_size = len(lst) // 3
    # Handle the case where the list size is not a multiple of 3
    remainder = len(lst) % 3

    # Determine the split points
    first_split = split_size
    second_split = first_split + split_size + (1 if remainder > 0 else 0)
    third_split = second_split + split_size + (1 if remainder > 1 else 0)

    return lst[:first_split], lst[first_split:second_split], lst[second_split:third_split]
# # print(NewAgentCreation.interview_agent(Ram_agent,"What do you think about healthcare"))



# Rams_anwser= Ram_agent.generate_reaction("What do you think about healthcare")
# print(Rams_anwser)
