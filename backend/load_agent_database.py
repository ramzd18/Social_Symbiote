import retrieve_agent
from langchain_experimental.generative_agents import (
    GenerativeAgent,
    GenerativeAgentMemory,
)
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
from datetime import datetime
def LoadAgent(email,agent_name): 
  LLM = ChatOpenAI(max_tokens=200)
  agent_data= retrieve_agent.retrieve_agents_record(email,agent_name)
  if agent_data=="Error":
    return "Agent data is not in database"
  else:
   
    memory= agent_data[3]
    memory_retriever=memory.get('memory_retriever')
    print(memory_retriever.keys())
    stream=memory_retriever['memory_stream']
    Document_list= []
    for i in stream: 
      metadataval=i['metadata']
      datetimeobj= datetime.strptime('13-03-21 06:33:13','%d-%m-%y %H:%M:%S')
      metadataval["last_accessed_at"] = datetime.strptime(str(i['metadata']["last_accessed_at"][2:10]),'%y-%m-%d')
      metadataval["created_at"] = datetime.strptime(i['metadata']["created_at"][2:10],'%y-%m-%d')
      document= Document(page_content=i.get('page_content'),metadata=metadataval)
      Document_list.append(document)
    memory_retriever= create_new_memory_retriever()
    timeweightedstore=add_existing_memories_vectorstore(memory_retriever,Document_list)
    ram_memory = GenerativeAgentMemory(
    llm=LLM,
    memory_retriever=timeweightedstore,
    verbose=False,
    reflection_threshold=25,  # we will give this a relatively low number to show how reflection works
    )
  ram= GenerativeAgent(
    name="Ram",
    age=25,
    traits="talkative,social,emphatetic",
    status="very political active",  # You can add more persistent traits here
    memory_retriever=timeweightedstore,
    llm=LLM,
    memory=ram_memory,
)

  return ram

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
    
    


# Ram_agent=LoadAgent('rbpeddu@gmail.com','Ram')
# # print(NewAgentCreation.interview_agent(Ram_agent,"What do you think about healthcare"))



# Rams_anwser= Ram_agent.generate_reaction("What do you think about healthcare")
# print(Rams_anwser)
