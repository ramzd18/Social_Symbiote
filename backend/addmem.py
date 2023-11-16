from reddit import additionalredditmemories
import load_agent_database
import retrieve_agent

import json

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

# list=additionalredditmemories.total_comments("fitness, gym, health and wellness,traveling,food, finance,sports")

michael=load_agent_database.LoadAgent('akhiliyengar2004@gmail.com','michael')

# for mem in list: 
#   michael.memory.add_socialmedia_memory(mem)
# mick_memory=dict(michael.memory.social_media_memory)
# del mick_memory ['vectorstore']


# print(retrieve_agent.retrieve_agents_record('akhiliyengar2004@gmail.com','mark')[7])
# mark=load_agent_database.LoadAgent('akhiliyengar2004@gmail.com','mark')
# mem_retriever=dict(mark.memory.social_media_memory)
# del mem_retriever['vectorstore']
# retrieve_agent.updatesoical_agent_info('akhiliyengar2004@gmail.com','michael',json.dumps(str(mick_memory)),json.dumps({'openness': 0.23, 'neuroticism': -0.54, 'extraversion': 0.8, 'agreeableness': 0.23, 'conscientiousness': -0.34}))
print(michael.generate_question_response("Do you like energy drinks"))
print(michael.generate_question_response("What do you like about energy drinks"))
print(michael.generate_question_response("What places are you the most likely to buy energy drinks"))
print(michael.generate_question_response("What do you not like about energy drinks"))

