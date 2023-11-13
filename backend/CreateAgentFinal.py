import peopledatalabsretrieval
from langchain_experimental import generative_agents
from twitter import user_lookup
from twitter import user_tweets
from reddit import redditapi
from reddit import redditusers
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
import re
import google_search_results
import random
from retrieve_agent import push_agent_info
from load_agent_database import LoadAgent
import datetime


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

def relevance_score_fn(score: float) -> float:
    """Return a similarity score on a scale [0, 1]."""
    return 1.0 - score / math.sqrt(2)



def create_and_store_agent(description,age,job):
  os.environ["OPENAI_API_KEY"]="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"
  LLM = ChatOpenAI(model_name="gpt-3.5-turbo-1106") 
  usertup= peopledatalabsretrieval.initialize_person(description,age,job)
  job=usertup[1]
  persondict= usertup[0]
  status=usertup[2]
  product=usertup[3]
  interestslist=persondict["interests"]
  memoryretr= create_new_memory_retriever()
  memory1= create_new_memory_retriever()
  memory2=create_new_memory_retriever()
  # newmemretr= addMemories(memoryretr)
  interestsliststr= str(interestslist)
  interestsliststr=interestsliststr.replace('[','')
  interestsliststr=interestsliststr.replace(']','')


  agent_memory = generative_agents.GenerativeAgentMemory(
    llm=LLM,
    memory_retriever=memoryretr,
    social_media_memory= memory1,
    product_memory=memory2,
    verbose=False,
    reflection_threshold=900,  # we will give this a relatively low number to show how reflection works
)
  #  return {"name":fullname,"gender":gender,"work industry":industry, "current job":specificoccupation ,"twitter":twitter_username,"age":age,"company":company,"location":location,"interests":interests,"skills":skills,"education":educationstr}

  agent= generative_agents.GenerativeAgent(
    name=persondict["name"],
    age=age,
    traits="talkative,social,emphatetic",
    status=status,  # You can add more persistent traits here
    # memory_retriever=create_new_memory_retriever(),
    education_and_work=persondict['name'] + " works as a "+persondict["current job"]+" and "+ persondict["education"],
    interests=interestsliststr,
    llm=LLM,
    memory=agent_memory,
)
  twitter_username=persondict["twitter"]
  userid= user_lookup.find_user(twitter_username)
  likedtweets=user_tweets.main(userid,"liked_tweets",10)
  tweets=user_tweets.main(userid,"tweets",20)
  tweets=user_tweets.clean_tweets(tweets)
  likedtweets=user_tweets.clean_likedtweets(likedtweets)
  subredditslist= redditusers.get_commmon_subreddit(interestslist)
  user= redditusers.get_users(interestslist,subredditslist)
  comments= user[1]
  username=user[0]
  totallist= redditusers.find_most_relevant_submissions(interestslist,comments,username)
  for memory in totallist:
    print("looped memory"+memory)
    agent.memory.add_socialmedia_memory(memory)

  productstring= agent.memory.search_prodct_questions(product,agent.status)
  actual_product_list= productstring[:3]
  print(actual_product_list)
  big_url_list=[]
  count=0
  for query in actual_product_list: 
    if(count>2): 
        break 
    print("Finding queries")
    big_url_list.append(google_search_results.api_results(query))

  
  big_url_list = [item for sublist in big_url_list for item in sublist]
  print("overall big url list"+ str(big_url_list))
  random.shuffle(big_url_list)
  big_url_list=big_url_list[:10]
  text_url_list=google_search_results.urls_to_summarizedtext(big_url_list)
  print("finished summarizing")
  print("Overall total url list"+ str(big_url_list))
  if(len(text_url_list)>10): 
      random.shuffle(text_url_list)
      text_url_list= text_url_list[:10]
  for text in text_url_list: 
    print("looped products")
    agent.memory.add_product_memory(text)
    print("")

  print("memoryinginginginign")
  agent.product_to_memory(product)
  return agent


agent= create_and_store_agent("My target customer is a person who is looking forward to buying their first home and needs help and advice with the process",28,"Nurse")
print(agent.generate_question_response("What do you think about home financing"))







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