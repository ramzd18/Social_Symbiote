from backend import peopledatalabsretrieval
from langchain_experimental import generative_agents
from backend.twitter import user_lookup
from backend.twitter import user_tweets
from backend.reddit import redditapi
from backend.reddit import redditusers
from backend.reddit import additionalredditmemories
# import promptLLMmemories
from langchain_experimental import generative_agents
# from langchain_experimental.generative_agents import search_prodct_questions
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
from backend import google_search_results
import random
# from backend.retrieve_agent import push_agent_info
# from backend.load_agent_database import LoadAgent
import datetime
import threading
# import retrieve_agent
# from langchain.llms import OpenAI


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



def create_and_store_agent(description,age,job1):
  os.environ["OPENAI_API_KEY"]="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"
  LLM = ChatOpenAI(model_name="gpt-3.5-turbo-1106") 
  usertup= peopledatalabsretrieval.initialize_person(description,age,job1)
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
  gender=persondict['gender']
  if gender=='female':
     gender='F'
  else: 
     gender='M'

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
    education_and_work=persondict['name'] + " works as a "+job+" and "+ persondict["education"],
    interests=interestsliststr,
    llm=LLM,
    memory=agent_memory,
)
  tweets=[]
  likedtweets=[]
  if(persondict['twitter']!='false'):
   try:
      twitter_username=persondict["twitter"]
      userid= user_lookup.find_user(twitter_username)
      likedtweets=user_tweets.main(userid,"liked_tweets",10)
      tweets=user_tweets.main(userid,"tweets",20)
      tweets=user_tweets.clean_tweets(tweets)
      likedtweets=user_tweets.clean_likedtweets(likedtweets)
   except:
      likedtweets=[]
      tweets=[]
  else: 
     tweets=[]
     likedtweets=[]
  try:
   (user,coms,sums)= additionalredditmemories.determine_most_similair_redditor(interestslist,additionalredditmemories.get_common_subreddit_interestlist(interestslist))
   (foms,agent1)=additionalredditmemories.gpt_redditor(user,coms,sums,agent)
  except:
   foms=[]
   fubs=[]
  

  totallist=[]

  agent=agent1
  skills=persondict['skills']
  firstmems=agent.memoriesprompt(str(skills),"")
  def secondtask():
    secondmem=agent.memoriesprompt(str(skills),str(firstmems))
    secondmem=secondmem.split(';')
    for mem1 in secondmem: 
      agent.memory.add_memory(mem1)
      print("memadd")
  task_thread = threading.Thread(target=secondtask,)
  task_thread.start()

  firstmem=firstmems.split(';')
  for mem in firstmem: 
     agent.memory.add_memory(mem)
  print("first done")


  descriptionqueries=agent.search_description_questions(description)
  print("third done")
  if(len(descriptionqueries)<3): 
     descriptionqueries=descriptionqueries[0].split("\n")

  print("Length of wanted questions" + str(len(descriptionqueries)))
  dlinks=[]
  for dquery in descriptionqueries:
     print("query")
     dlinks.append(google_search_results.api_results(dquery))

  if dlinks is not None:
    dlinks = [item for sublist in dlinks if sublist is not None for item in sublist]
  else:
    dlinks = []
  random.shuffle(dlinks)
  dlinks[:70]
  print("Dlinks length"+ str(len(dlinks)))
  description_text= google_search_results.urls_to_summarizedtext(dlinks)
  description_text=[item for sublist in description_text for item in sublist]
  print("Description text length"+ str(len(description_text)))

  totlist1=agent.analysis_of_product(description_text,description)
  for mem in totlist1: 
    print(mem)
    if(isinstance(mem,str)):
      agent.memory.add_memory(mem)
    else:
       print("not mem")

  print("memoryinginginginign")
  return (agent,gender,job1)










# (agent,gender,job1)=create_and_store_agent("Someone who is very interested in technology and loves to watch movies and tv shows",25,"developer")
# print(agent.generate_question_response("What do you like doing"))
# print(agent.generate_question_response("what are the most important thigns in your life"))
# agent_memory= agent.memory.memory_retriever.dict()
# agent_soc_memory=agent.memory.social_media_memory.dict()
# del agent_memory['vectorstore']
# del agent_soc_memory['vectorstore']
# retrieve_agent.push_agent_info(agent.name,agent.age,agent.status,json.dumps(str(agent_memory)),json.dumps({}),'rbpeddu@gmail.com',json.dumps(str(agent_soc_memory)),agent.education_and_work,json.dumps(agent.memory.personalitylist),agent.interests,gender,"senior developer","Technology enthusiast who is interested in natrue")


















# print(create_and_store_agent("Wants to buy a new computer",34,"developer"))
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