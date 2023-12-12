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


# results=["I care deeply about LGBTQ right and their rally for equal protection","The housing market looks very good right now, it is making me want to buy a house","Political movements for equal rights have been gaining momentum","Climate is changing rapidly and I have to try and make a change in my daily life.","Vaccines Masking Guidelines Visitor Guidelines Close Search Search Johns Hopkins Medicine Search Close Health Health Close Main Menu Health Conditions and Diseases Treatments, Tests and Therapies Wellness and Prevention Caregiving Health and Prevention Gender Affirmation Nonsurgical Services Gender affirmation can include various procedures such as hormone therapy, genital reconstruction, breast reconstruction, facial plastic surgery, speech therapy and primary care . Patients choose only the gender-affirming nonsurgical services that best fit their needs as they transition","The banning of gender-affirming care creates a dangerous environment for NC trans youth . Edit Close Sign Up Log In Dashboard Logout My Account Dashboard Profile Saved items Logout Home About Us Get Involved Editorial Staff Advertise With The Niner Times Sign Up For Our Newsletter News Campus Student Organizations City Events Day of Remembrance Sports Baseball Mens Basketball Womens Basketball Cross Country Football Golf Softball Mens Soccer Womens Soccer Tennis Track & Field Volleyball National Sports Arts & Culture Campus Events Guides","The restrictions mean that 25% of Americans age 10 to 17 now live more than a dayâs drive away, round trip, from a clinic that could provide medications and hormones to support their gender transition ."]
# reduced_list = [results[i] +" New Article"+ results[i+1]+results[i+2]+results[i+4]+results[i+5] for i in range(0, len(results)-5, 5)]
# print(len(reduced_list))
# print(reduced_list[0])
# print(len(reduced_list))
chris=load_agent_database.LoadAgent('rbpeddu@gmail.com','chris')

# splitlist=google_search_results.split_list(results,3)
# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(brendan.analysis_of_product, arg) for arg in splitlist]
#     wait(futures)
#     results1 = [future.result() for future in futures]
interests=chris.interests
print(interests)
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
print(chris.marketing_analysis("Life is a sport, drink it up","Win from within","The product is a sports drink made for people who workout to replenish their electrolytes"))
print(chris.generate_question_response("What are you primarily interested in"))
print(chris.generate_question_response("Where do you spend a lot of your money"))
print(chris.generate_question_response("Where in a grocery store should our energy drink be to make you view it more"))


# agent_memory= chris.memory.memory_retriever.dict()
# agent_soc_memory=chris.memory.social_media_memory.dict()
# del agent_memory['vectorstore']
# del agent_soc_memory['vectorstore']
# personalitylist=json.dumps(chris.memory.personalitylist)
# retrieve_agent.update_agent_info('rbpeddu@gmail.com','chris',json.dumps(str(agent_memory)),personalitylist)

# print(chris.memory.fetch_memories("What are you favorite things to do"))












# interest=brendan.interests.split(',')
# print(interest)
# total_search_list=[]
# for interestval in interest: 
#   print(interestval)
#   print("start")
#   search=(brendan.search_prodct_questions(interestval,"Test"))[0].splitlines()
#   for query in search: 
#     search.remove(query)
#     search.append(query[2:])
#   total_search_list=total_search_list+search
# print(total_search_list)
# big_url_list=[]
# count=0
# for searchquery in total_search_list: 
#   print("Finding queries")
#   big_url_list.append(google_search_results.api_results(searchquery))

# big_url_list = [item for sublist in big_url_list for item in sublist]
# print(google_search_results.urls_to_summarizedtext(big_url_list))

# michael= retrieve_agent.get_all_agents('rbpeddu@gmail.com')
# mikemem=michael[3].replace('"', '')
# print(type(michael[3]))
# print(mikemem)
# mikemem=dict(json.loads(mikemem))
# mikdedict=json.dumps(mikemem)
# print(type(mikemem))


# mikedict=json.loads(michael[3])
# mikedict = re.sub(r''vectorstore':\s*\d+', '', michael[3])
# mikestr=str(michael[3])
# mikestr=mikestr.replace(" 'vectorstore': <langchain.vectorstores.faiss.FAISS object at 0x0000020DE9F54610>, ","")
# print(mikestr)
# mikejson=json.dumps(mikestr)


# del mikedict['vectorstore']
# mikemem= michael.memory.memory_retriever.dict()
# listofmems=[]
# for mem in mikemem['memory_stream']:
#   mem=dict(mem)
#   listofmems.append(mem['page_content'])
# print(listofmems)
# # print(michael.turn_soc_memories_into_list(str(listofmems)))
# print(michael.turn_soc_memories_into_list(str(listofmems)))
# querylist=["What does a business development analyst do","How to play in recration leagues as an adult","Career oppurtunities for business development analyst","Fun hobbies to do in your spare time","Common sport activities to play as an adult"]
# urllist=[]
# for query in querylist: 
#   list=(google_search_results.api_results(query))
#   print(list)
#   urllist.append(list)
# flattened_list = [item for sublist in urllist for item in sublist]
# print(flattened_list)
# # flattened_list=['https://www.nerdwallet.com/article/mortgages/home-buying-checklist-steps-to-buying-house', 'https://www.rocketmortgage.com/learn/how-to-buy-a-house', 'https://www.vandaele.com/7-steps-to-home-buying/', 'https://www.quickenloans.com/learn/steps-to-buying-a-house', 'https://www.investopedia.com/updates/first-time-home-buyer/', 'https://bpfund.com/california-home-buying/', 'https://www.bankrate.com/real-estate/how-to-buy-a-house/', 'https://www.discover.com/home-loans/articles/10-steps-to-buying-a-home/', 'https://info.totalwellnesshealth.com/blog/health-tips-employees', 'https://www.indeed.com/career-advice/career-development/wellness-tips-for-the-workplace', 'https://www.teambonding.com/10-workplace-wellness-tips-to-maintain-mental-physical-wellness/', 'https://www.upmchealthplan.com/employers/blog/wellness/employee-health/', 'https://snacknation.com/blog/wellness-tips-for-the-workplace/', 'https://www.wellbeats.com/five-wellness-tips-for-your-workday/', 'https://www.healthandfitnesstravel.com/advice/topics/workplace-well-being-staying-healthy-at-work/25-easy-tips-to-enhance-your-well-being-at-work-angie-newson', 'https://fourwellness.co/blog/workplace-wellness-10-tips-for-good-health-at-work', 'https://www.planteriagroup.com/blog/10-tips-for-workplace-wellness/', 'https://www.corporatewellnessmagazine.com/article/fitness-at-work-top-tips-for-promoting-physical-activity-and-improving-employee-well-being', 'https://www.cdc.gov/healthyweight/healthy_eating/index.html', 'https://www.nhs.uk/live-well/eat-well/how-to-eat-a-balanced-diet/eight-tips-for-healthy-eating/', 'https://health.gov/sites/default/files/2019-10/DGA_Healthy-Eating-Pattern.pdf', 'https://www.eatingwell.com/article/7938737/top-healthy-eating-habits-according-to-a-dietitian/', 'https://www.helpguide.org/articles/healthy-eating/healthy-eating.htm', 'https://www.heartandstroke.ca/healthy-living/healthy-eating/healthy-eating-basics', 'https://www.myplate.gov/tip-sheet/healthy-eating-adults', 'https://www.hsph.harvard.edu/nutritionsource/healthy-eating-plate/', 'https://www.cnbc.com/economy/', 'https://www.marketwatch.com/economy-politics/calendar', 'https://www.wsj.com/economy', 'https://apnews.com/hub/economy', 'https://finance.yahoo.com/topic/economic-news/', 'https://www2.deloitte.com/us/en/insights/economy/global-economic-outlook/weekly-update.html', 'https://www.usnews.com/topics/subjects/economy', 'https://www.cnn.com/business/economy', 'https://www.investopedia.com/economic-news-5218422', 'https://www.nytimes.com/section/business/economy', 'https://www.redbookmag.com/body/health-fitness/g45360845/7-healthy-alternatives-to-energy-drinks/', 'https://honehealth.com/edge/nutrition/healthiest-energy-drinks/', 'https://letsliveitup.com/blogs/supergreens/healthy-alternatives-for-energy-drinks', 'https://www.healthline.com/health/energy-drinks-healthy-alternatives', 'https://news.umiamihealth.org/en/are-there-healthy-alternatives-to-coffee-and-energy-drinks/', 'https://brainmd.com/blog/4-energy-boosting-healthy-alternatives-to-energy-drinks/', 'https://b-sync.life/blogs/science/energy-drinks-alternatives', 'https://getmte.com/blogs/learn/the-5-best-energy-drink-alternatives-a-healthier-way-to-boost-energy-levels', 'https://www.reuters.com/sports/soccer/', 'https://www.sportingnews.com/us/soccer/news', 'https://www.goal.com/en-us', 'https://sports.yahoo.com/soccer/', 'https://theathletic.com/football/', 'https://www.espn.com/soccer/', 'https://en.as.com/soccer/', 'https://www.cbssports.com/soccer/', 'https://www.nytimes.com/section/sports/soccer', 'https://www.wsj.com/sports/soccer', 'https://www.health.harvard.edu/energy-and-fatigue/9-tips-to-boost-your-energy-naturally', 'https://www.sleephealthsolutionsohio.com/blog/10-ways-stay-energized-throughout-day/', 'https://www.webmd.com/women/features/10-energy-boosters', 'https://www.bhf.org.uk/informationsupport/heart-matters-magazine/wellbeing/boost-energy-levels', 'https://www.piedmont.org/living-better/secrets-for-all-day-energy', 'https://www.healthline.com/nutrition/how-to-boost-energy', 'https://medium.com/mind-cafe/7-scientifically-backed-ways-to-keep-your-energy-levels-high-all-day-long-ea5192187d8c', 'https://www.hss.edu/article_eating-for-energy.asp', 'https://www.urmc.rochester.edu/encyclopedia/content.aspx?contenttypeid=1&contentid=503', 'https://moderncastle.com/apartment-living-for-pet-owners/', 'https://www.country-classics.com/apartment-living-blog/4-tips-for-having-a-pet-in-an-apartment', 'https://pawprides.com/8-tips-for-living-in-an-apartment-with-dogs/', 'https://www.onehealth.org/blog/how-to-take-care-of-a-dog-in-an-apartment', 'https://www.wikihow.pet/Keep-a-Dog-in-an-Apartment', 'https://www.dialmycalls.com/blog/top-7-tips-for-managing-pet-friendly-apartments', 'https://neaterpets.com/blogs/news/apartment-living-with-dogs', 'https://www.petsbest.com/blog/top-7-tips-for-apartment-living-with-dogs', 'https://applaws.com/uk/dog/how-to-keep-your-pet-safe-when-living-in-an-apartment/']
# print(flattened_list)
# print("summarized")
# scraped_list=google_search_results.urls_to_summarizedtext(flattened_list)
# print(michael.memoriesprompt(str(listofmems)))
# mikemem= michael.memory.memory_retriever.dict()
# del mikemem['vectorstore']
# print("querying")
# print(michael.memoriesprompt(str(listofmems)))
# sportslist=michael.memoriespromptkeyword(str(listofmems),"sports")
# sportslist=sportslist.split(';')
# worklist=michael.memoriespromptkeyword(str(listofmems),"work")
# worklist=worklist.split(';')
# travellist=michael.memoriespromptkeyword(str(listofmems),"travel")
# travellist=travellist.split(';')
# financelist=michael.memoriespromptkeyword(str(listofmems),"finance")
# financelist=financelist.split(';')
# foodlist=michael.memoriespromptkeyword(str(listofmems),"food")
# foodlist=foodlist.split(';')
# totlist=sportslist+worklist+travellist+financelist+foodlist

# for mem in totlist: 
#   michael.memory.add_memory(mem)
# mikemem1= michael.memory.memory_retriever.dict()

# retrieve_agent.update_agent_info('akhiliyengar2004@gmail.com','michael',json.dumps(str(mikedict)),json.dumps(personlist))
# print("response")
# print(michael.generate_question_response("What times of the day would be most likely to buy energy drinks"))
# print(michael.generate_question_response("where are you most likely to buy enegy drinks"))
# print(michael.generate_question_response("What type of packing on energy drinks do you think would most attract you"))
# print(michael.generate_question_response("I am building an energy drink brand what tips do you have for me"))
# print(michael.generate_question_response("What does your daily schedule in your job look like"))
# print(michael.generate_question_response("What are some specific things you would search on the internet to learn more about"))





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