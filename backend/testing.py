# import load_agent_database 
# import agent_memories_maintainance
# import retrieve_agent
import promptLLMmemories
from langchain_experimental import generative_agents
from datetime import datetime, timedelta
from typing import List
from termcolor import colored
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
from twitter import user_lookup
from twitter import user_tweets
from reddit import redditapi
from reddit import redditusers
import re
import google_search_results
import random
from retrieve_agent import push_agent_info
from load_agent_database import LoadAgent
import datetime


os.environ["OPENAI_API_KEY"]="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"
LLM = ChatOpenAI(model_name="gpt-3.5-turbo-16k")  # Can be any LLM you want.
USER_NAME="Person A"
def relevance_score_fn(score: float) -> float:
    """Return a similarity score on a scale [0, 1]."""
    return 1.0 - score / math.sqrt(2)
# def addMemories(vectorstore):
#     loader = TextLoader(file_path="libs/experimental/langchain_experimental/generative_agents/backend.txt")
#     print("called here ")
#     document=loader.load()
#     vectorstore.add_documents(document)
#     return vectorstore
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
          vectorstore=vectorstore, other_score_keys=["importance"], k=5  
      )
    return timevectorstore
def create_agent():
  memoryretr= create_new_memory_retriever()
  memory1= create_new_memory_retriever()
  memory2=create_new_memory_retriever()
  # newmemretr= addMemories(memoryretr)
  ram_memory = generative_agents.GenerativeAgentMemory(
    llm=LLM,
    memory_retriever=memoryretr,
    social_media_memory= memory1,
    product_memory=memory2,
    verbose=False,
    reflection_threshold=1100,  # we will give this a relatively low number to show how reflection works
)
  ram= generative_agents.GenerativeAgent(
    name="Jason",
    age=28,
    # traits="talkative,social,emphatetic",
    status="Looking to buy first house",  # You can add more persistent traits here
    # memory_retriever=create_new_memory_retriever(),
    education_and_work="Sara attended Arizona Statue Univeristy and currently works as a vetinerary nurse",
    interests="collecting antiques', 'exercise', 'sweepstakes', 'home improvement', 'reading', 'sports', 'the arts', 'hockey', 'watching hockey', 'home decoration', 'health', 'watching sports', 'photograph', 'cooking', 'cruises', 'outdoors', 'electronics', 'crafts', 'fitness', 'music', 'camping', 'dogs', 'movies', 'collecting', 'kids', 'medicine', 'diet', 'cats', 'travel', 'wine', 'motorcycling', 'investing', 'traveling', 'self improvement",
    llm=LLM,
    memory=ram_memory,
)
  return ram; 

ram=create_agent()
ram.memory.add_memory("I go to a basketball game")
ram.memory.add_memory("I go to a football game")
ram.memory.add_memory("I play soccer")
ram.memory.add_socialmedia_memory("Bayern Mucnhen is plauing soccer")
ram_memory= ram.memory.memory_retriever.dict()
ram_soc_memory=ram.memory.social_media_memory.dict()
del ram_memory['vectorstore']
del ram_soc_memory['vectorstore']
# def push_agent_info(name,age,status,memory,llm,personemail,social_media_memory,educationwork,personalitylist,interests):

push_agent_info(ram.name,ram.age,ram.status,json.dumps(str(ram_memory)),json.dumps({}),'rbpeddu@gmail.com', json.dumps(str(ram_soc_memory)),ram.education_and_work,json.dumps(ram.memory.personalitylist),ram.interests)

# dict={"tags": None, "metadata": None, "vectorstore": "<langchain.vectorstores.faiss.FAISS object at 0x000002CE9B387F50>", "search_kwargs": {"k": 100}, "memory_stream": [{"page_content": "I go to a basketball game", "metadata": {"importance": 0.12, "last_accessed_at": datetime.datetime(2023, 11, 11, 2, 30, 24, 696542), "created_at": datetime.datetime(2023, 11, 11, 2, 30, 24, 696542), "buffer_idx": 0}, "type": "Document"}, {"page_content": "I go to a football game", "metadata": {"importance": 0.12, "last_accessed_at": datetime.datetime(2023, 11, 11, 2, 30, 26, 572600), "created_at": datetime.datetime(2023, 11, 11, 2, 30, 26, 572600), "buffer_idx": 1}, "type": "Document"}, {"page_content": "I play soccer", "metadata": {"importance": 0.15, "last_accessed_at": datetime.datetime(2023, 11, 11, 2, 30, 27, 889572), "created_at": datetime.datetime(2023, 11, 11, 2, 30, 27, 889572), "buffer_idx": 2}, "type": "Document"}], "decay_rate": 0.01, "k": 5, "other_score_keys": ["importance"], "default_salience": None}
# print(type(dict))

# sara=LoadAgent('rbpeddu@gmail.com',"Sara")
# print(sara.memory.memory_retriever.dict())
# print(sara.memory.social_media_memory.dict())
# print(sara.generate_question_response("Do you like sports"))
# print(sara.memory.memory_retriever.dict())


















































print("Making agent")
# userid= user_lookup.find_user("sararecruiting")
# likedtweets=user_tweets.main(userid,"liked_tweets",10)
# tweets=user_tweets.main(userid,"tweets",20)
# tweets=user_tweets.clean_tweets(tweets)
# likedtweets=user_tweets.clean_likedtweets(likedtweets)
# interestslist=['collecting antiques', 'exercise', 'sweepstakes', 'home improvement', 'reading', 'sports', 'the arts', 'hockey', 'watching hockey', 'home decoration', 'health', 'watching sports', 'photograph', 'cooking', 'cruises', 'outdoors', 'electronics', 'crafts', 'fitness', 'music', 'camping', 'dogs', 'movies', 'collecting', 'kids', 'medicine', 'diet', 'cats', 'travel', 'wine', 'motorcycling', 'investing', 'traveling', 'self improvement']
# subredditslist= redditusers.get_commmon_subreddit(interestslist)
# user= redditusers.get_users(interestslist,subredditslist)
# comments= user[1]
# username=user[0]

# print(username)
# totallist= redditusers.find_most_relevant_submissions(interestslist,comments)
# print ("Reflecting Threshold"+str(ram.memory.reflection_threshold))
# for memory in totallist:
#   print("looped memory"+memory)
#   ram.memory.add_socialmedia_memory(memory)
# productstring= ram.memory.search_prodct_questions("Home Financing Options",ram.status)
# actual_product_list= productstring[:3]
# print(actual_product_list)
# big_url_list=[]
# count=0
# for query in actual_product_list: 
#     if(count>2): 
#         break 
#     print("Finding queries")
#     big_url_list.append(google_search_results.api_results(query))


# big_url_list = [item for sublist in big_url_list for item in sublist]
# random.shuffle(big_url_list)
# big_url_list=big_url_list[:6]
# text_url_list=google_search_results.urls_to_summarizedtext(big_url_list)
# print("finished summarizing")
# print("Overall total url list"+ str(big_url_list))
# if(len(text_url_list)>10): 
#      random.shuffle(text_url_list)
#      text_url_list= text_url_list[:10]
# for text in text_url_list: 
#    print("looped products")
#    ram.memory.add_product_memory(text)
#    print("")

# print("memoryinginginginign")
# ram.product_to_memory("Home financing")

# print("Got here")
# print(ram.generate_question_response("What does a day in your life look like"))
# print(ram.generate_question_response("What are you current biggest problems with home financing"))
# print(ram.generate_question_response("What is your experience level with home financing"))
# print(ram.generate_question_response("What would you think about a product that simplifies the home financing process by providing relevant information to users"))
# print(ram.generate_question_response("What are some features you would want on an add simplyfing the home financing process"))


