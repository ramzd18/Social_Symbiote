from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os
from langchain.chains import LLMChain
from fuzzywuzzy import fuzz
import random



os.environ["OPENAI_API_KEY"]="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"
llm = ChatOpenAI(max_tokens=1200)
def chain( prompt: PromptTemplate) -> LLMChain:
        return LLMChain(
            llm=llm, prompt=prompt, verbose=False
        )

def generate_relevant_description(descirption,age,job): 
    llm = ChatOpenAI(max_tokens=1200)

    prompt = PromptTemplate.from_template(
            """
Given this description of a person. 
Description: {description}, and that they are {age} years old and are a {job}. 
Fill in the followng fields with information inferring what their values would be from the description. 
Fields:  status, category . Status represents what they are currently looking for. Category represents the product cateogy or field the description matches. Only return two values representing your anwsers to the field and seperate them with a semicolon. 
For example, if I inputted (a person who wants to improve their sleep by tracking sleep perforance, 30,nurse) a example return format would be : Looking for ways to track my sleep performance ; Wearable sleep technology
"""
        )        
    description=descirption
    age=age
    result= chain(prompt=prompt).run(description=description,age=age,job=job).strip()
    result.split(';')
    return result



total_job_list=[
"broadcasting","editorial","journalism","video"	"writing","customer_success",	"support","education_administration",	"professor","researcher",	"teacher",	"data",	"devops",	"electrical","mechanical",	"network","information_technology",	"project_engineering",	
"quality_assurance","security",	"software",	"systems",	"web",	"accounting",	"investment",	"tax","dental	","fitness","doctor","nursing","therapy","wellness","compensation","employee_development",	
"recruiting","lawyer","paralegal",	"judicial",	"brand_marketing",	"content_marketing",	"product_marketing",	"project_management",	"office_management","logistics","product","graphic_design","product_design","web_design",
"events","media_relations",	"property_management",	"realtor",	"accounts",	"business_development"	,"pipeline","media","customer_service","education","engineering","finance","health","human_resources",
"legal","marketing","operations","design","public_relations","real_estate","sales"
]
smallerlist=[
"media","customer_service","education","engineering","finance","health","human_resources","legal","marketing","operations",
"design","public_relations","real_estate","sales"
]
smallerdict={}
smallerdict["media"]=["broadcasting","editorial","journalism","video","writing"]
smallerdict["customer_service"]=["customer_success","support"]
smallerdict["education"]=["education_administration",	"professor","researcher",	"teacher"]
smallerdict["engineering"]=["data",	"devops",	"electrical","mechanical",	"network","information_technology",	"project_engineering",	"quality_assurance","security",	"software",	"systems","web"]
smallerdict["finance"]=["accounting",	"investment","tax"]
smallerdict["health"]=["dental	","fitness","doctor","nursing","therapy","wellness"]
smallerdict["human_resources"]=["compensation","employee_development","recruiting"]
smallerdict["legal"]=["lawyer","paralegal",	"judicial"]
smallerdict["marketing"]=["brand_marketing","content_marketing","product_marketing"]
smallerdict["operations"]=["project_management","office_management","logistics","product"]
smallerdict["design"]=["graphic_design","product_design","web_design"]
smallerdict["public_relations"]=["events","media_relations"]
smallerdict["real_estate"]=["property_management","realtor"]
smallerdict["sales"]=["accounts",	"business_development","pipeline"]

def similairty_text(interests_text, comment_text):
  text1 = interests_text
  text2 = comment_text
  similarity = fuzz.ratio(text1, text2)

  return similarity/100

def most_similair_job(job_text): 
    similairity_dict={}
    job_text=job_text.lower()
    for job in total_job_list: 
        similairity_dict[job]=similairty_text(job,job_text)

    sorted_dict_desc = dict(sorted(similairity_dict.items(), key=lambda item: item[1], reverse=True))
    first_key = list(sorted_dict_desc.keys())[0]
    if first_key in smallerdict:
        joblist= smallerdict[first_key]
        first_key= random.choice(joblist)
    return first_key

def final_name_age_occupation(description,age,job):
    initial_arr= generate_relevant_description(description,age,job)
    initial_arr=initial_arr.split(';')
    age=2023-int(age)
    job=most_similair_job(job)
    status=initial_arr[0]
    # product= initial_arr[1]
    product=""
    return (age,job,status,product)

         
      