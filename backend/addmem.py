from reddit import additionalredditmemories
import load_agent_database
import retrieve_agent

import json

from langchain.chat_models import ChatOpenAI
import json
import google_search_results
from langchain.chat_models import ChatOpenAI
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document
import json
import threading
import time
import retrieve_agent
import re
from concurrent.futures import ThreadPoolExecutor, wait
import CreateAgentFinal
import warnings

# results=["I care deeply about LGBTQ right and their rally for equal protection","The housing market looks very good right now, it is making me want to buy a house","Political movements for equal rights have been gaining momentum","Climate is changing rapidly and I have to try and make a change in my daily life.","Vaccines Masking Guidelines Visitor Guidelines Close Search Search Johns Hopkins Medicine Search Close Health Health Close Main Menu Health Conditions and Diseases Treatments, Tests and Therapies Wellness and Prevention Caregiving Health and Prevention Gender Affirmation Nonsurgical Services Gender affirmation can include various procedures such as hormone therapy, genital reconstruction, breast reconstruction, facial plastic surgery, speech therapy and primary care . Patients choose only the gender-affirming nonsurgical services that best fit their needs as they transition","The banning of gender-affirming care creates a dangerous environment for NC trans youth . Edit Close Sign Up Log In Dashboard Logout My Account Dashboard Profile Saved items Logout Home About Us Get Involved Editorial Staff Advertise With The Niner Times Sign Up For Our Newsletter News Campus Student Organizations City Events Day of Remembrance Sports Baseball Mens Basketball Womens Basketball Cross Country Football Golf Softball Mens Soccer Womens Soccer Tennis Track & Field Volleyball National Sports Arts & Culture Campus Events Guides","The restrictions mean that 25% of Americans age 10 to 17 now live more than a dayâs drive away, round trip, from a clinic that could provide medications and hormones to support their gender transition ."]
# reduced_list = [results[i] +" New Article"+ results[i+1]+results[i+2]+results[i+4]+results[i+5] for i in range(0, len(results)-5, 5)]
# print(len(reduced_list))
# print(reduced_list[0])
# print(len(reduced_list))
# all_agents= retrieve_agent.get_all_agents('rbpeddu@gmail.com')

# print(all_agents)

# brendan=load_agent_database.LoadAgent('rbpeddu@gmail.com','chris')
(jenna,gend,job)=CreateAgentFinal.create_and_store_agent("A first time home buyer looking to understand the market",28,"devops")
print(jenna.generate_question_response("what do you think about the home buying process"))
print(jenna.generate_question_response("what are your biggest problems with buying a home right now"))
print(jenna.generate_question_response("what type of homes interest you"))


# splitlist=google_search_results.split_list(results,3)
# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(brendan.analysis_of_product, arg) for arg in splitlist]
#     wait(futures)
#     results1 = [future.result() for future in futures]
# interests=chris.interests
# print(interests)
# memsresult=brendan.analysis_of_product(reduced_list)

# # memsresult= [element for sublist in results1 for element in sublist ]
# # print("memsresult length"+ str(len(memsresult)))
# for mem in memsresult: 
#     print("25"+ mem)
#     brendan.memory.add_memory(mem)


print("responses")
# print(chris.generate_question_response("What are you primarily interested in"))
# print(chris.generate_question_response("Where do you spend a lot of your money"))
# print(chris.generate_question_response("What branding do you like better Taste the eneregy or green, clean and powerful"))


# total=len(chris.memory.memory_retriever.vectorstore.index_to_docstore_id)
# index_len=total//4
# first_split=chris.memory.memory_retriever.memory_stream[0:index_len]
# second_split=chris.memory.memory_retriever.memory_stream[index_len:2*index_len]
# third_split=chris.memory.memory_retriever.memory_stream[2*index_len:3*index_len]
# fourth_split=chris.memory.memory_retriever.memory_stream[3*index_len:4*index_len]
# first=(chris.memoriesprompt(first_split)).split(';')
# second=(chris.memoriesprompt(second_split)).split(';')
# third=(chris.memoriesprompt(third_split)).split(';')
# fourth=(chris.memoriesprompt(fourth_split)).split(';')
# totlist=[first,second,third,fourth]
# totlist=[item for sublist in totlist for item in sublist]
# for mem in totlist: 
#   chris.memory.add_memory(mem)
# list=chris.marketing_analysis("Replenish your energy with our revitalizing sports drink","The product is a sports drink made for people who workout to replenish their electrolytes")
# list=list.split(",")
# actuallist=[]
# count=0; 
# for li in list: 
#   if(count<4):
#     try:
#             li1=li.split(':')[1]
#             actuallist.append(float(li1))
#     except: 
#             actuallist.append(float(0.5))
#   else: 
#     li1= li.split(':')[1]
#     actuallist.append(li1)
#   count+=1
# print(actuallist)
# print(chris.generate_question_response("What are you primarily interested in"))
# print(chris.generate_question_response("Where do you spend a lot of your money"))
# print(chris.generate_question_response("Where in a grocery store should our energy drink be to make you view it more"))


# agent_memory= chris.memory.memory_retriever.dict()
# agent_soc_memory=chris.memory.social_media_memory.dict()
# del agent_memory['vectorstore']
# del agent_soc_memory['vectorstore']
# personalitylist=json.dumps(chris.memory.personalitylist)
# retrieve_agent.update_agent_info('rbpeddu@gmail.com','chris',json.dumps(str(agent_memory)),personalitylist)

# print(chris.memory.fetch_memories("What are you favorite things to do"))








# mikemem= michael.memory.memory_retriever
# del mikemem['vectorstore']

# retrieve_agent.update_agent_info('akhiliyengar2004@gmail.com','michael',json.dumps(str(mikejson)),json.dumps(michael[9]))



# print(len(google_search_results.urls_to_summarizedtext(flattened_list)))

# print(google_search_results.summarize(totalstr))
# print(relevant_mems)

# for mem in list: )
#   michael.memory.add_socialmedia_memory(mem)
# mick_memory=dict(michael.memory.social_media_memory)
# del mick_memory ['vectorstore']


# print(retrieve_agent.retrieve_agents_record('akhiliyengar2004@gmail.com','mark')[7])
# mark=load_agent_database.LoadAgent('akhiliyengar2004@gmail.com','mark')
# mem_retriever=dict(mark.memory.social_media_memory)
# del mem_retriever['vectorstore']
# retrieve_agent.updatesoical_agent_info('akhiliyengar2004@gmail.com','michael',json.dumps(str(mikejson)),json.dumps({'openness': 0.23, 'neuroticism': -0.54, 'extraversion': 0.8, 'agreeableness': 0.23, 'conscientiousness': -0.34}))
# print(michael.generate_question_response("what are some things you are interested in learning about"))