import json

# See https://github.com/peopledatalabs/peopledatalabs-python



# ##### Fields to query by: 
# job_company_industry,inferred_salary,job_onet_specific_occupation_detail,
# job_summary,job_title,birth_year,gender,education.summary,education.raw,education.majors,education.school.name,
# location_name,facebook_friends,
# twitter_username,
from peopledatalabs import PDLPY

def get_person():
  CLIENT = PDLPY(
      api_key="f5075ad903d0a727d3807e8baa6cb167ecee2e7f0cc39b6a695a2c06e860d2a2",
  )

  # Create an Elasticsearch query
  ES_QUERY = {
    'query': {
      'bool': {
          'must': [
              {'term': {'location_country': "united states"}},
              {'term': {'job_title_role': "health"}},
              {'exists': {'field': "twitter_username"}},
              {'exists':{'field':"birth_year"}},
              {'exists':{'field':"skills"}},
              {'exists':{'field':"interests"}},


              # {'exists':{'field': "reddit"}}
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
    # Write out each profile found to file
    for record in data:
      print(type(record))
      print(record)
      print(f"Successfully grabbed {len(data)} records from PDL.")
      print(f"{response['total']} total PDL records exist matching this query.")
  else:
    print("NOTE: The carrier pigeons lost motivation in flight. See error and try again.")
    print("Error:", response)
# dictval= {'id': 'MuDv3XS8jispJ57pReUW8Q_0000', 'full_name': 'sara taylor', 'first_name': 'sara', 'middle_initial': 'd', 'middle_name': None, 'last_initial': 't', 'last_name': 'taylor', 'gender': 'female', 'birth_year': 1967, 'birth_date': None, 'linkedin_url': 'linkedin.com/in/sarataylor', 'linkedin_username': 'sarataylor', 'linkedin_id': '14881222', 'facebook_url': 'facebook.com/sara.taylor.940098', 'facebook_username': 'sara.taylor.940098', 'facebook_id': '697887839', 'twitter_url': 'twitter.com/sararecruiting', 'twitter_username': 'sararecruiting', 'github_url': None, 'github_username': None, 'work_email': 'staylor@sfspca.org', 'personal_emails': ['saratszoo@yahoo.com', 'sarataylor717@gmail.com'], 'recommended_personal_email': 'sarataylor717@gmail.com', 'mobile_phone': '+17073423293', 'industry': 'veterinary', 'job_title': 'vice president veterinary nursing', 'job_title_role': 'health', 'job_title_sub_role': 'nursing', 'job_title_levels': ['vp'], 'job_onet_code': None, 'job_onet_major_group': None, 'job_onet_minor_group': None, 'job_onet_broad_occupation': None, 'job_onet_specific_occupation': None, 'job_onet_specific_occupation_detail': None, 'job_company_id': 'sfspca', 'job_company_name': 'san francisco spca', 'job_company_website': 'sfspca.org', 'job_company_size': '201-500', 'job_company_founded': 1868, 'job_company_industry': 'non-profit organization management', 'job_company_linkedin_url': 'linkedin.com/company/sfspca', 'job_company_linkedin_id': '39469', 'job_company_facebook_url': 'facebook.com/sfspca', 'job_company_twitter_url': 'twitter.com/sfspca', 'job_company_location_name': 'san francisco, california, united states', 'job_company_location_locality': 'san francisco', 'job_company_location_metro': 'san francisco, california', 'job_company_location_region': 'california', 'job_company_location_geo': '37.77,-122.41', 'job_company_location_street_address': '201 alabama street', 'job_company_location_address_line_2': None, 'job_company_location_postal_code': '94103', 'job_company_location_country': 'united states', 'job_company_location_continent': 'north america', 'job_last_updated': '2023-09-12', 'job_start_date': '2022-05', 'location_name': 'oakland, california, united states', 'location_locality': 'oakland', 'location_metro': 'san francisco, california', 'location_region': 'california', 'location_country': 'united states', 'location_continent': 'north america', 'location_street_address': '289 hanover avenue', 'location_address_line_2': None, 'location_postal_code': '94606', 'location_geo': '37.80,-122.26', 'location_last_updated': '2022-06-28', 'phone_numbers': ['+17073423293', '+17076477271', '+17072465414', '+13033217438', '+13033937384', '+15102351772', '+15106477271'], 'emails': [{'address': 'saratszoo@yahoo.com', 'type': 'personal'}, {'address': 'sarataylor717@gmail.com', 'type': 'personal'}, {'address': 'sara.taylor@indecomm.net', 'type': 'professional'}, {'address': 'omarchy@ca.rr.com', 'type': None}, {'address': 'staylor@compass-usa.com', 'type': 'professional'}, {'address': 'staylor@sfspca.org', 'type': 'current_professional'}], 'interests': ['collecting antiques', 'exercise', 'sweepstakes', 'home improvement', 'reading', 'sports', 'the arts', 'hockey', 'watching hockey', 'home decoration', 'health', 'watching sports', 'photograph', 'cooking', 'cruises', 'outdoors', 'electronics', 'crafts', 'fitness', 'music', 'camping', 'dogs', 'movies', 'collecting', 'kids', 'medicine', 'diet', 'cats', 'travel', 'wine', 'motorcycling', 'investing', 'traveling', 'self improvement'], 'skills': ['recruiting', 'talent management', 'human resources', 'interviews', 'talent acquisition', 'leadership', 'executive search', 'temporary placement', 'employee benefits', 'hris', 'deferred compensation', 'onboarding', 'performance management', 'applicant tracking systems', 'employee relations', 'hiring', 'organizational development', 'training', 'cold calling', 'strategy', 'consulting', 'personnel management', 'technical recruiting', 'coaching', 'interviewing', 'employment law', 'internet recruiting', 'sourcing', 'employee engagement', 'contract recruitment', 'benefits negotiation', 'outsourcing', 'human resources information systems', 'team leadership', 'veterinary nursing', 'employee training', 'veterinary medicine', 'culture development', 'streamlining process'], 'location_names': ['vallejo, california, united states', 'yachats, oregon, united states', 'denver, colorado, united states', 'richmond, california, united states', 'doylestown, pennsylvania, united states', 'walnut creek, california, united states', 'littleton, colorado, united states', 'concord, california, united states', 'berkeley, california, united states', 'oakland, california, united states', 'charlotte, north carolina, united states'], 'regions': ['oregon, united states', 'california, united states', 'colorado, united states', 'pennsylvania, united states', 'north carolina, united states'], 'countries': ['united states'], 'street_addresses': [{'name': 'oakland, california, united states', 'locality': 'oakland', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '289 hanover avenue', 'address_line_2': None, 'postal_code': '94606', 'geo': '37.80,-122.26'}, {'name': 'oakland, california, united states', 'locality': 'oakland', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '643 54th street', 'address_line_2': None, 'postal_code': '94609', 'geo': '37.80,-122.26'}, {'name': 'oakland, california, united states', 'locality': 'oakland', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '365 santa clara avenue', 'address_line_2': 'apartment d', 'postal_code': '94610', 'geo': '37.80,-122.26'}, {'name': 'vallejo, california, united states', 'locality': 'vallejo', 'region': 'california', 'metro': 'vallejo, california', 'country': 'united states', 'continent': 'north america', 'street_address': '626 steffan street', 'address_line_2': None, 'postal_code': '94591', 'geo': '38.10,-122.25'}, {'name': 'concord, california, united states', 'locality': 'concord', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '1126 meadow lane', 'address_line_2': None, 'postal_code': '94520', 'geo': '37.97,-122.03'}, {'name': 'berkeley, california, united states', 'locality': 'berkeley', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '266 hillcrest road', 'address_line_2': None, 'postal_code': '94705', 'geo': '37.87,-122.27'}, {'name': 'walnut creek, california, united states', 'locality': 'walnut creek', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '1826 sharp avenue', 'address_line_2': None, 'postal_code': '94596', 'geo': '37.90,-122.06'}, {'name': 'oakland, california, united states', 'locality': 'oakland', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '633 alma avenue', 'address_line_2': 'apartment 4', 'postal_code': '94610', 'geo': '37.80,-122.26'}, {'name': 'yachats, oregon, united states', 'locality': 'yachats', 'region': 'oregon', 'metro': None, 'country': 'united states', 'continent': 'north america', 'street_address': '5299 fairview mountain road', 'address_line_2': None, 'postal_code': '97498', 'geo': '44.31,-124.10'}, {'name': 'richmond, california, united states', 'locality': 'richmond', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '1233 south 56th street', 'address_line_2': None, 'postal_code': '94804', 'geo': '37.93,-122.34'}, {'name': 'oakland, california, united states', 'locality': 'oakland', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '727 60th street', 'address_line_2': None, 'postal_code': '94609', 'geo': '37.80,-122.26'}, {'name': 'denver, colorado, united states', 'locality': 'denver', 'region': 'colorado', 'metro': 'denver, colorado', 'country': 'united states', 'continent': 'north america', 'street_address': '1035 leyden street', 'address_line_2': None, 'postal_code': '80220', 'geo': '39.73,-104.98'}, {'name': 'littleton, colorado, united states', 'locality': 'littleton', 'region': 'colorado', 'metro': 'denver, colorado', 'country': 'united states', 'continent': 'north america', 'street_address': '10292 west spread eagle mtn', 'address_line_2': None, 'postal_code': '80127', 'geo': '39.61,-105.01'}, {'name': 'doylestown, pennsylvania, united states', 'locality': 'doylestown', 'region': 'pennsylvania', 'metro': 'philadelphia, pennsylvania', 'country': 'united states', 'continent': 'north america', 'street_address': '91 west state street', 'address_line_2': None, 'postal_code': '18901', 'geo': None}, {'name': 'denver, colorado, united states', 'locality': 'denver', 'region': 'colorado', 'metro': 'denver, colorado', 'country': 'united states', 'continent': 'north america', 'street_address': '1460 north high street', 'address_line_2': 'apartment 5', 'postal_code': '80218', 'geo': '39.73,-104.98'}], 'experience': [{'company': {'name': 'four corners veterinary hospital', 'size': '11-50', 'id': 'four-corners-veterinary-hospital', 'founded': 1967, 'industry': 'veterinary', 'location': {'name': 'concord, california, united states', 'locality': 'concord', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '2956 treat boulevard', 'address_line_2': 'suite e', 'postal_code': '94518', 'geo': '37.97,-122.03'}, 'linkedin_url': 'linkedin.com/company/four-corners-veterinary-hospital', 'linkedin_id': '18346934', 'facebook_url': None, 'twitter_url': None, 'website': 'fourcornersvet.com'}, 'start_date': '2000', 'end_date': '2002', 'title': {'name': 'registered veterinary technician', 'role': None, 'sub_role': None, 'levels': []}, 'location_names': ['concord, california, united states'], 'is_primary': False}, {'company': {'name': 'san francisco veterinary specialists', 'size': None, 'id': None, 'founded': None, 'industry': None, 'location': None, 'linkedin_url': None, 'linkedin_id': None, 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['san francisco, california, united states'], 'end_date': '2011-09', 'start_date': '2003', 'title': {'name': 'veterinary clinical staff director', 'role': 'health', 'sub_role': None, 'levels': ['director']}, 'is_primary': False}, {'company': {'name': 'san francisco veterinary specialists san rafaeal ca', 'size': None, 'id': None, 'founded': None, 'industry': None, 'location': None, 'linkedin_url': None, 'linkedin_id': None, 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['san francisco, california, united states'], 'end_date': '2003', 'start_date': '2002', 'title': {'name': 'veterinary technician', 'role': None, 'sub_role': None, 'levels': []}, 'is_primary': False}, {'company': {'name': 'san francisco spca', 'size': '201-500', 'id': 'sfspca', 'founded': 1868, 'industry': 'non-profit organization management', 'location': {'name': 'san francisco, california, united states', 'locality': 'san francisco', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '201 alabama street', 'address_line_2': None, 'postal_code': '94103', 'geo': '37.77,-122.41'}, 'linkedin_url': 'linkedin.com/company/sfspca', 'linkedin_id': '39469', 'facebook_url': 'facebook.com/sfspca', 'twitter_url': 'twitter.com/sfspca', 'website': 'sfspca.org'}, 'location_names': ['san francisco, california, united states'], 'end_date': None, 'start_date': '2022-05', 'title': {'name': 'vice president veterinary nursing', 'role': 'health', 'sub_role': 'nursing', 'levels': ['vp']}, 'is_primary': True}, {'company': {'name': 'san francisco spca', 'size': '201-500', 'id': 'sfspca', 'founded': 1868, 'industry': 'non-profit organization management', 'location': {'name': 'san francisco, california, united states', 'locality': 'san francisco', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '201 alabama street', 'address_line_2': None, 'postal_code': '94103', 'geo': '37.77,-122.41'}, 'linkedin_url': 'linkedin.com/company/sfspca', 'linkedin_id': '39469', 'facebook_url': 'facebook.com/sfspca', 'twitter_url': 'twitter.com/sfspca', 'website': 'sfspca.org'}, 'location_names': ['san francisco, california, united states'], 'end_date': '2022-09', 'start_date': '2011-10', 'title': {'name': 'veterinary nursing care director, mission campus hospital', 'role': 'health', 'sub_role': 'nursing', 'levels': ['director']}, 'is_primary': False}], 'education': [{'school': {'name': 'r.b. chamberlin hs', 'type': 'secondary school', 'id': None, 'location': None, 'linkedin_url': None, 'facebook_url': None, 'twitter_url': None, 'linkedin_id': None, 'website': None, 'domain': None}, 'degrees': [], 'start_date': None, 'end_date': None, 'majors': [], 'minors': [], 'gpa': None}, {'school': {'name': 'george school', 'type': None, 'id': None, 'location': None, 'linkedin_url': None, 'facebook_url': None, 'twitter_url': None, 'linkedin_id': None, 'website': None, 'domain': None}, 'degrees': [], 'start_date': None, 'end_date': None, 'majors': [], 'minors': [], 'gpa': None}, {'school': {'name': 'bel - rea institute of animal technology', 'type': 'post-secondary institution', 'id': '0q22AtgCULvE865UR1-HPQ_0', 'location': {'name': 'denver, colorado, united states', 'locality': 'denver', 'region': 'colorado', 'country': 'united states', 'continent': 'north america'}, 'linkedin_url': 'linkedin.com/school/bel-rea-institute-of-animal-technology', 'facebook_url': None, 'twitter_url': None, 'linkedin_id': '33370', 'website': 'bel-rea.com', 'domain': 'bel-rea.com'}, 'end_date': '1996', 'start_date': '1994', 'gpa': 4.0, 'degrees': ['associates'], 'majors': [], 'minors': []}, {'school': {'name': 'university of california, berkeley', 'type': 'post-secondary institution', 'id': '2qNY2SMMyQp-PfcClA1jmA_0', 'location': {'name': 'berkeley, california, united states', 'locality': 'berkeley', 'region': 'california', 'country': 'united states', 'continent': 'north america'}, 'linkedin_url': 'linkedin.com/school/uc-berkeley', 'facebook_url': 'facebook.com/ucberkeley', 'twitter_url': 'twitter.com/ucberkeley', 'linkedin_id': '17939', 'website': 'berkeley.edu', 'domain': 'berkeley.edu'}, 'end_date': '1990', 'start_date': '1986', 'gpa': None, 'degrees': ['bachelors', 'bachelor of arts'], 'majors': ['anthropology'], 'minors': []}, {'school': {'name': 'bowling green state university', 'type': 'post-secondary institution', 'id': '0QnklO7IqQyYAFCqbZwoWg_0', 'location': {'name': 'bowling green, ohio, united states', 'locality': 'bowling green', 'region': 'ohio', 'country': 'united states', 'continent': 'north america'}, 'linkedin_url': 'linkedin.com/school/bowling-green-state-university', 'facebook_url': 'facebook.com/officialbgsu', 'twitter_url': 'twitter.com/bgsu', 'linkedin_id': '19087', 'website': 'bgsu.edu', 'domain': 'bgsu.edu'}, 'end_date': '1999', 'start_date': '1995', 'gpa': None, 'degrees': ['bachelors', 'bachelor of science in business administration', 'bachelor of science'], 'majors': ['business administration', 'sociology', 'human resource management'], 'minors': []}], 'profiles': [{'network': 'linkedin', 'id': '55202210', 'url': 'linkedin.com/in/sarataylor', 'username': 'sarataylor'}, {'network': 'linkedin', 'id': '14881222', 'url': 'linkedin.com/in/sarastclair', 'username': 'sarastclair'}, {'network': 'facebook', 'id': '697887839', 'url': 'facebook.com/sara.taylor.940098', 'username': 'sara.taylor.940098'}, {'network': 'linkedin', 'id': '55202210', 'url': 'linkedin.com/in/sara-taylor-8825a116', 'username': 'sara-taylor-8825a116'}, {'network': 'linkedin', 'id': '14881222', 'url': 'linkedin.com/in/sarataylor', 'username': 'sarataylor'}, {'network': 'twitter', 'id': None, 'url': 'twitter.com/sararecruiting', 'username': 'sararecruiting'}, {'network': 'linkedin', 'id': None, 'url': 'linkedin.com/in/sara-taylor-99ab974', 'username': 'sara-taylor-99ab974'}, {'network': 'klout', 'id': None, 'url': 'klout.com/sararecruiting', 'username': 'sararecruiting'}], 'version_status': {'status': 'updated', 'contains': [], 'previous_version': '23.0', 'current_version': '24.0'}}

# print (type(dictval))
# for key in dictval:
#     print(key)




#### Takes in people data labs json from api request and returns a dict only contains the fields for their name, gender, industry, currentrole, twitterusername, redditusername, education,skills and interests
def parsepeopledata(dictval):
  fullname= dictval["first_name"]+ " "+dictval["last_name"]
  print("fullname "+fullname)
  gender= dictval["gender"]
  print("gender "+gender)
  twitter_url= dictval["twitter_username"]
  print("twitter_url "+twitter_url)

  if "industry" in dictval:
    industry=dictval["industry"]
  else:
    industry=""
  print("industry "+industry)
  if "age" in dictval:
    age= 2022-dictval["birth_year"]
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
      # print(school["school"]["name"])
      educationstr+="Attended this school: "+ school["school"]["name"]
      if "majors" in school: 
        if school["majors"]:
          educationstr+="   Majored in these subjects:"+ str(school["majors"]) 
      educationstr+="\n"
      # if(school["school"])
      # for key in school:
      #     print(key)
  print(educationstr)
  return {"name":fullname,"gender":gender,"work industry":industry, "current job":specificoccupation ,"twitter":twitter_url,"age":age,"role":company,"location":location,"interests":interests,"skills":skills,"education":educationstr}



def get_person_sumary(peoplelabsdict): 
  person_name= peoplelabsdict["name"]
  generalsummary=""
  for key in peoplelabsdict: 
      if peoplelabsdict[key]!="": 
        generalsummary+= "This is "+person_name+" "+key+ ":"+str(peoplelabsdict[key]) +"\n"
  return generalsummary

get_person()
