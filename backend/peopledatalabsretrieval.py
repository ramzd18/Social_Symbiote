import json

# See https://github.com/peopledatalabs/peopledatalabs-python



# ##### Fields to query by: 
# job_company_industry,inferred_salary,job_onet_specific_occupation_detail,
# job_summary,job_title,birth_year,gender,education.summary,education.raw,education.majors,education.school.name,
# location_name,facebook_friends,
# twitter_username,
from peopledatalabs import PDLPY
import promptLLMmemories

def get_person(year,job ):
  CLIENT = PDLPY(
      api_key="f5075ad903d0a727d3807e8baa6cb167ecee2e7f0cc39b6a695a2c06e860d2a2",
  )

  # Create an Elasticsearch query
  ES_QUERY = {
    'query': {
      'bool': {
          'must': [
              {'term': {'location_country': "united states"}},
              {'term': {'job_title_sub_role': str(job).strip()}},
              {'term': {'birth_year': year}},
              {'exists': {'field': "twitter_username"}},
              {'exists':{'field':"skills"}},
              {'exists':{'field':"interests"}},
              {'exists':{'field':"job_title_role"}},
              {'exists':{'field':"education"}},
              {'exists':{'field':"first_name"}},
              {'exists':{'field':"gender"}}

        ]
      }
    }
  }

  # Create a parameters JSON object
  PARAMS = {
    'query': ES_QUERY,
    'size': 1,
    'pretty': True
  }

  # Pass the parameters object to the Person Search API
  response = CLIENT.person.search(**PARAMS).json()

  # Check for successful response
  if response["status"] == 200:
    data = response['data']
    print(type(data))
   
    return data[0]
    # Write out each profile found to file
    for record in data:
      print(type(record))
      print(record)
      print(f"Successfully grabbed {len(data)} records from PDL.")
      print(f"{response['total']} total PDL records exist matching this query.")
  else:
    print("NOTE: The carrier pigeons lost motivation in flight. See error and try again.")
    print("Error:", response)
    return "error"




def get_person_no_twitter(year,job):
  CLIENT = PDLPY(
      api_key="f5075ad903d0a727d3807e8baa6cb167ecee2e7f0cc39b6a695a2c06e860d2a2",
  )

  # Create an Elasticsearch query
  ES_QUERY = {
    'query': {
      'bool': {
          'must': [
              {'term': {'location_country': "united states"}},
              {'term': {'job_title_sub_role': str(job).strip()}},
              {'term': {'birth_year': year}},
              # {'exists': {'field': "twitter_username"}},
              {'exists':{'field':"skills"}},
              {'exists':{'field':"interests"}},
              {'exists':{'field':"job_title_role"}},
              {'exists':{'field':"education"}},
              {'exists':{'field':"first_name"}},
              {'exists':{'field':"gender"}}
        ]
      }
    }
  }

  # Create a parameters JSON object
  PARAMS = {
    'query': ES_QUERY,
    'size': 1,
    'pretty': True
  }

  # Pass the parameters object to the Person Search API
  response = CLIENT.person.search(**PARAMS).json()

  # Check for successful response
  if response["status"] == 200:
    data = response['data']
    print(type(data))
   
    return data[0]
    # Write out each profile found to file
    for record in data:
      print(type(record))
      print(record)
      print(f"Successfully grabbed {len(data)} records from PDL.")
      print(f"{response['total']} total PDL records exist matching this query.")
  else:
    print("NOTE: The carrier pigeons lost motivation in flight. See error and try again.")
    print("Error:", response)


#### Takes in people data labs json from api request and returns a dict only contains the fields for their name, gender, industry, currentrole, twitterusername, redditusername, education,skills and interests
def parsepeopledata(dictval):
  fullname= dictval["first_name"]
  print("fullname "+fullname)
  gender= dictval["gender"]
  print("gender "+gender)
  twitter_username=""
  if dictval['twitter_username'] != None: 
   twitter_username= dictval["twitter_username"]
  else: 
    twitter_username="false"
  if "industry" in dictval:
    industry=dictval["industry"]
  else:
    industry=""
  print("industry "+industry)
  if "birth_year" in dictval:
    age= 2023-dictval["birth_year"]
  else:
    age=""
  print("age "+str(age))
  # if "currentrole" in dictval:
  #   currentrole=dictval["job_title_role"]
  # else: 
  #   currentrole=""
  # print("currentrole "+currentrole)
  if "job_title" in dictval:
    specificoccupation= dictval["job_title"]
  else:
    specificoccupation=""
  print("specific occupation "+specificoccupation)
  if "job_company_name" in dictval:
    company= dictval["job_company_name"]
  else: 
    company=""
  print("company "+ company)
  location= dictval["location_metro"]
  print("location "+ location)
  interests=dictval["interests"]
  print("interests "+ str(interests))
  skills= dictval["skills"]
  print("skills "+ str(skills))

  educationstr=""
  education= dictval["education"]
  for school in education:
      if "majors" in school: 
          print (school)
          educationstr+="Attended this school: "+ school["school"]["name"]
          educationstr+="   Majored in these subjects:"+ str(school["majors"]) 
          educationstr+="\n"

      # if(school["school"])
      # for key in school:
      #     print(key)
  print(educationstr)
  return {"name":fullname,"gender":gender,"work industry":industry, "current job":specificoccupation ,"twitter":twitter_username,"age":age,"company":company,"location":location,"interests":interests,"skills":skills,"education":educationstr}



def get_person_sumary(peoplelabsdict): 
  person_name= peoplelabsdict["name"]
  generalsummary=""
  for key in peoplelabsdict: 
      if peoplelabsdict[key]!="": 
        generalsummary+= "This is "+person_name+" "+key+ ":"+str(peoplelabsdict[key]) +"\n"
  return generalsummary




def initialize_person(description,age,job): 
  usertup= promptLLMmemories.final_name_age_occupation(description,age,job)
  age=usertup[0]
  job=usertup[1]
  status= usertup[2]
  product=usertup[3]
  print(status)
  print(product)
  # salary=">"+str(usertup[2])
  print(age)
  print(job)
  # print(salary)
  persondict=get_person(age,job)
  if(str(persondict)=="error"):
    persondict=get_person_no_twitter(age,job)
  parsed_dict= parsepeopledata(persondict)
  print(parsed_dict)
  return (parsed_dict,job,status,product)



