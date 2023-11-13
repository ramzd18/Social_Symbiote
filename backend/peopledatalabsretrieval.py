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




dictval1= {'id': 'Upszqul5dCEuXaZXnTveuA_0000', 'full_name': 'cassie jones', 'first_name': 'cassie', 'middle_initial': None, 'middle_name': None, 'last_initial': 'j', 'last_name': 'jones', 'gender': 'female', 'birth_year': 1993, 'birth_date': None, 'linkedin_url': 'linkedin.com/in/cassiejones11', 'linkedin_username': 'cassiejones11', 'linkedin_id': '290076716', 'facebook_url': 'facebook.com/cassie.jones11', 'facebook_username': 'cassie.jones11', 'facebook_id': '1461960910', 'twitter_url': 'twitter.com/cassie_jones1', 'twitter_username': 'cassie_jones1', 'github_url': None, 'github_username': None, 'work_email': None, 'personal_emails': ['cassie.jones11@gmail.com'], 'recommended_personal_email': 'cassie.jones11@gmail.com', 'mobile_phone': '+12183480001', 'industry': 'primary/secondary education', 'job_title': 'spanish teacher', 'job_title_role': 'education', 'job_title_sub_role': 'teacher', 'job_title_levels': [], 'job_company_id': 'maplewood-middle-school', 'job_company_name': 'maplewood middle school', 'job_company_website': 'maplewood.k12.oh.us', 'job_company_size': '51-200', 'job_company_founded': None, 'job_company_industry': 'education management', 'job_company_linkedin_url': 'linkedin.com/company/maplewood-middle-school', 'job_company_linkedin_id': '4019981', 'job_company_facebook_url': None, 'job_company_twitter_url': None, 'job_company_location_name': 'cortland, ohio, united states', 'job_company_location_locality': 'cortland', 'job_company_location_metro': 'youngstown, ohio', 'job_company_location_region': 'ohio', 'job_company_location_geo': '41.33,-80.72', 'job_company_location_street_address': '4174 greenville road', 'job_company_location_address_line_2': None, 'job_company_location_postal_code': '44410', 'job_company_location_country': 'united states', 'job_company_location_continent': 'north america', 'job_last_updated': '2023-09-18', 'job_start_date': '2018-08-01', 'location_name': 'saint paul, minnesota, united states', 'location_locality': 'saint paul', 'location_metro': 'minneapolis, minnesota', 'location_region': 'minnesota', 'location_country': 'united states', 'location_continent': 'north america', 'location_street_address': '1017 chatsworth street north', 'location_address_line_2': None, 'location_postal_code': '55103', 'location_geo': '44.94,-93.09', 'location_last_updated': '2020-01-01', 'phone_numbers': ['+12183480001'], 'emails': [{'address': 'cassie.jones11@gmail.com', 'type': 'personal'}, {'address': 'cjones@gapinc.com', 'type': 'professional'}, {'address': 'cjones@minneapolisparks.org', 'type': 'professional'}], 'interests': ['writing', 'children', 'languages', 'traveling', 'education', 'dancing', 'editing', 'photography', 'reading', 'music', 'poverty alleviation', 'grammar', 'human rights', 'animal welfare', 'organizing', 'health'], 'skills': ['spanish speaking', 'english grammar', 'social media', 'blogger', 'microsoft office', 'associated press style', 'microsoft publisher', 'dance', 'editing', 'public relations', 'photography', 'advertising', 'time management', 'storytelling', 'interviews', 'creative writing', 'news writing', 'ap style'], 'location_names': ['saint cloud, minnesota, united states', 'duluth, minnesota, united states', 'minneapolis, minnesota, united states', 'saint paul, minnesota, united states', 'fridley, minnesota, united states'], 'regions': ['minnesota, united states'], 'countries': ['united states'], 'street_addresses': [{'name': 'saint paul, minnesota, united states', 'locality': 'saint paul', 'region': 'minnesota', 'metro': 'minneapolis, minnesota', 'country': 'united states', 'continent': 'north america', 'street_address': '1017 chatsworth street north', 'address_line_2': None, 'postal_code': '55103', 'geo': '44.94,-93.09'}], 'experience': [{'company': {'name': 'maplewood middle school', 'size': '51-200', 'id': 'maplewood-middle-school', 'founded': None, 'industry': 'education management', 'location': {'name': 'cortland, ohio, united states', 'locality': 'cortland', 'region': 'ohio', 'metro': 'youngstown, ohio', 'country': 'united states', 'continent': 'north america', 'street_address': '4174 greenville road', 'address_line_2': None, 'postal_code': '44410', 'geo': '41.33,-80.72'}, 'linkedin_url': 'linkedin.com/company/maplewood-middle-school', 'linkedin_id': '4019981', 'facebook_url': None, 'twitter_url': None, 'website': 'maplewood.k12.oh.us'}, 'location_names': ['maplewood, minnesota, united states'], 'end_date': None, 'start_date': '2018-08-01', 'title': {'name': 'spanish teacher', 'role': 'education', 'sub_role': 'teacher', 'levels': []}, 'is_primary': True}, {'company': {'name': 'youth arts online paddington arts', 'size': None, 'id': None, 'founded': None, 'industry': None, 'location': None, 'linkedin_url': None, 'linkedin_id': None, 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['london, greater london, united kingdom'], 'end_date': '2014-05-01', 'start_date': '2014-03-01', 'title': {'name': 'journalist', 'role': 'media', 'sub_role': 'journalism', 'levels': []}, 'is_primary': False}, {'company': {'name': 'seyfer family kovich family', 'size': None, 'id': None, 'founded': None, 'industry': None, 'location': None, 'linkedin_url': None, 'linkedin_id': None, 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['duluth, minnesota, united states'], 'end_date': '2013-08-01', 'start_date': '2012-05-01', 'title': {'name': 'summer nanny', 'role': None, 'sub_role': None, 'levels': []}, 'is_primary': False}, {'company': {'name': 'duluth figure skating club', 'size': '11-50', 'id': 'duluth-figure-skating-club', 'founded': None, 'industry': 'sports', 'location': {'name': 'hermantown, minnesota, united states', 'locality': 'hermantown', 'region': 'minnesota', 'metro': 'duluth, minnesota', 'country': 'united states', 'continent': 'north america', 'street_address': '4309 ugstad road', 'address_line_2': None, 'postal_code': '55811', 'geo': '46.80,-92.23'}, 'linkedin_url': 'linkedin.com/company/duluth-figure-skating-club', 'linkedin_id': '4074465', 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['duluth, minnesota, united states'], 'end_date': '2011-08-01', 'start_date': '2009-06-01', 'title': {'name': 'summer monitor', 'role': None, 'sub_role': None, 'levels': []}, 'is_primary': False}, {'company': {'name': 'minnesota premier publications', 'size': '11-50', 'id': 'minnesota-premier-publications', 'founded': 1990, 'industry': 'newspapers', 'location': {'name': 'minneapolis, minnesota, united states', 'locality': 'minneapolis', 'region': 'minnesota', 'metro': 'minneapolis, minnesota', 'country': 'united states', 'continent': 'north america', 'street_address': '1115 hennepin avenue', 'address_line_2': None, 'postal_code': '55403', 'geo': '44.98,-93.26'}, 'linkedin_url': 'linkedin.com/company/minnesota-premier-publications', 'linkedin_id': '75718', 'facebook_url': None, 'twitter_url': None, 'website': 'mnpubs.com'}, 'location_names': [], 'end_date': '2014-08-01', 'start_date': '2014-06-01', 'title': {'name': 'editorial intern', 'role': 'media', 'sub_role': 'editorial', 'levels': ['training']}, 'is_primary': False}, {'company': {'name': 'old navy', 'size': '10001+', 'id': 'gap-inc.-old-navy', 'founded': 1994, 'industry': 'retail', 'location': {'name': 'san francisco, california, united states', 'locality': 'san francisco', 'region': 'california', 'metro': 'san francisco, california', 'country': 'united states', 'continent': 'north america', 'street_address': '550 terry a francois boulevard', 'address_line_2': None, 'postal_code': '94158', 'geo': '37.77,-122.41'}, 'linkedin_url': 'linkedin.com/company/gap-inc.-old-navy', 'linkedin_id': '165295', 'facebook_url': 'facebook.com/oldnavy', 'twitter_url': None, 'website': None}, 'location_names': ['roseville, minnesota, united states'], 'end_date': '2017-08-01', 'start_date': '2015-06-01', 'title': {'name': 'brand associate and training lead', 'role': 'human_resources', 'sub_role': 'employee_development', 'levels': []}, 'is_primary': False}, {'company': {'name': "project eight college of saint benedict/saint john's university", 'size': None, 'id': None, 'founded': None, 'industry': None, 'location': None, 'linkedin_url': None, 'linkedin_id': None, 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['st. joseph, minnesota, united states'], 'end_date': '2013-05-01', 'start_date': '2012-09-01', 'title': {'name': 'public relations representative', 'role': 'public_relations', 'sub_role': None, 'levels': []}, 'is_primary': False}, {'company': {'name': 'dsw', 'size': '10001+', 'id': 'dsw', 'founded': 1969, 'industry': 'retail', 'location': {'name': 'australia', 'locality': None, 'region': None, 'metro': None, 'country': 'australia', 'continent': 'oceania', 'street_address': None, 'address_line_2': None, 'postal_code': None, 'geo': None}, 'linkedin_url': 'linkedin.com/company/dsw', 'linkedin_id': '36105348', 'facebook_url': 'facebook.com/dsw', 'twitter_url': 'twitter.com/dswshoelovers', 'website': 'dswinc.com'}, 'location_names': ['maplewood, minnesota, united states'], 'end_date': '2014-08-01', 'start_date': '2014-06-01', 'title': {'name': 'sales associate', 'role': 'sales', 'sub_role': 'accounts', 'levels': []}, 'is_primary': False}, {'company': {'name': 'reading corps', 'size': '501-1000', 'id': 'reading-corps', 'founded': 2003, 'industry': 'primary/secondary education', 'location': {'name': 'minneapolis, minnesota, united states', 'locality': 'minneapolis', 'region': 'minnesota', 'metro': 'minneapolis, minnesota', 'country': 'united states', 'continent': 'north america', 'street_address': '1200 south washington avenue', 'address_line_2': None, 'postal_code': None, 'geo': '44.98,-93.26'}, 'linkedin_url': 'linkedin.com/company/reading-corps', 'linkedin_id': '2364701', 'facebook_url': 'facebook.com/mnreadingcorps', 'twitter_url': 'twitter.com/mnreadingcorps', 'website': 'readingandmath.org'}, 'location_names': ['duluth, minnesota, united states'], 'end_date': '2016-06-01', 'start_date': '2015-06-01', 'title': {'name': 'kindergarten-focused literacy tutor', 'role': None, 'sub_role': None, 'levels': []}, 'is_primary': False}, {'company': {'name': 'college of saint benedict dance team', 'size': None, 'id': None, 'founded': None, 'industry': None, 'location': None, 'linkedin_url': None, 'linkedin_id': None, 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['st. joseph, minnesota, united states'], 'end_date': '2015-03-01', 'start_date': '2012-09-01', 'title': {'name': 'social media coordinator', 'role': 'media', 'sub_role': None, 'levels': []}, 'is_primary': False}, {'company': {'name': "the record college of st benedict/st john's university", 'size': None, 'id': None, 'founded': None, 'industry': None, 'location': None, 'linkedin_url': None, 'linkedin_id': None, 'facebook_url': None, 'twitter_url': None, 'website': None}, 'location_names': ['st. joseph, minnesota, united states'], 'end_date': '2015-01-01', 'start_date': '2013-09-01', 'title': {'name': 'writer', 'role': 'media', 'sub_role': 'writing', 'levels': []}, 'is_primary': False}, {'company': {'name': 'college of saint benedict and saint john’s university', 'size': '1001-5000', 'id': 'csbsju', 'founded': None, 'industry': 'higher education', 'location': {'name': 'st. joseph, minnesota, united states', 'locality': 'st. joseph', 'region': 'minnesota', 'metro': None, 'country': 'united states', 'continent': 'north america', 'street_address': '37 south college avenue', 'address_line_2': None, 'postal_code': '56374', 'geo': None}, 'linkedin_url': 'linkedin.com/company/csbsju', 'linkedin_id': '35229', 'facebook_url': 'facebook.com/twocolleges', 'twitter_url': 'twitter.com/csbsju', 'website': 'csbsju.edu'}, 'location_names': ['st. joseph, minnesota, united states', 'saint joseph, minnesota, united states'], 'end_date': '2015-05-01', 'start_date': '2015-03-01', 'title': {'name': 'student custodian- margretta hall', 'role': None, 'sub_role': None, 'levels': []}, 'is_primary': False}, {'company': {'name': 'minneapolis park & recreation board', 'size': '501-1000', 'id': 'minneapolis-park-and-recreation-board', 'founded': 1883, 'industry': 'recreational facilities and services', 'location': {'name': 'minneapolis, minnesota, united states', 'locality': 'minneapolis', 'region': 'minnesota', 'metro': 'minneapolis, minnesota', 'country': 'united states', 'continent': 'north america', 'street_address': '2117 west river road', 'address_line_2': None, 'postal_code': '55411', 'geo': '44.98,-93.26'}, 'linkedin_url': 'linkedin.com/company/minneapolis-park-and-recreation-board', 'linkedin_id': '10387556', 'facebook_url': 'facebook.com/minneapolisparks', 'twitter_url': 'twitter.com/mplsparkboard', 'website': 'minneapolisparks.org'}, 'location_names': ['minneapolis, minnesota, united states'], 'end_date': '2018-08-01', 'start_date': '2016-06-01', 'title': {'name': 'assistant preschool teacher and front desk associate and piano teacher', 'role': 'education', 'sub_role': 'teacher', 'levels': []}, 'is_primary': False}], 'education': [{'school': {'name': 'bethel university', 'type': 'post-secondary institution', 'id': 'FqKEpWpFwon5mNqFMB0YMg_0', 'location': {'name': 'minnesota, united states', 'locality': None, 'region': 'minnesota', 'country': 'united states', 'continent': 'north america'}, 'linkedin_url': 'linkedin.com/school/bethel-university', 'facebook_url': 'facebook.com/betheluniversityindiana', 'twitter_url': 'twitter.com/bethelindiana', 'linkedin_id': '18650', 'website': 'bethel.edu', 'domain': 'bethel.edu'}, 'end_date': '2018', 'start_date': '2016', 'gpa': None, 'degrees': ['masters'], 'majors': ['teaching', 'spanish'], 'minors': []}, {'school': {'name': 'marshall school', 'type': 'post-secondary institution', 'id': 'xgaIeBOUUHH-6gX8VIfXkA_0', 'location': {'name': 'duluth, minnesota, united states', 'locality': 'duluth', 'region': 'minnesota', 'country': 'united states', 'continent': 'north america'}, 'linkedin_url': 'linkedin.com/school/marshall-school', 'facebook_url': None, 'twitter_url': None, 'linkedin_id': '3201394', 'website': 'marshallschool.org', 'domain': 'marshallschool.org'}, 'end_date': '2011', 'start_date': '2003', 'gpa': None, 'degrees': [], 'majors': [], 'minors': []}, {'school': {'name': "saint john's university", 'type': 'post-secondary institution', 'id': '1oCRKmFsa1yExXnNPRQznw_0', 'location': {'name': 'collegeville, minnesota, united states', 'locality': 'collegeville', 'region': 'minnesota', 'country': 'united states', 'continent': 'north america'}, 'linkedin_url': "linkedin.com/school/saint-john's-university", 'facebook_url': 'facebook.com/csbsju', 'twitter_url': 'twitter.com/csbsju', 'linkedin_id': '18671', 'website': 'csbsju.edu', 'domain': 'csbsju.edu'}, 'end_date': '2015', 'start_date': '2011', 'gpa': 3.83, 'degrees': ['bachelors'], 'majors': ['media studies', 'communication', 'dance'], 'minors': []}], 'profiles': [{'network': 'facebook', 'id': '1461960910', 'url': 'facebook.com/cassie.jones11', 'username': 'cassie.jones11'}, {'network': 'linkedin', 'id': '290076716', 'url': 'linkedin.com/in/cassiejones11', 'username': 'cassiejones11'}, {'network': 'linkedin', 'id': None, 'url': 'linkedin.com/in/cassie-jones-57819081', 'username': 'cassie-jones-57819081'}, {'network': 'twitter', 'id': None, 'url': 'twitter.com/cassie_jones1', 'username': 'cassie_jones1'}], 'version_status': {'status': '', 'contains': [], 'previous_version': '', 'current_version': ''}}

# print (type(dictval))
# for key in dictval:
#     print(key)




#### Takes in people data labs json from api request and returns a dict only contains the fields for their name, gender, industry, currentrole, twitterusername, redditusername, education,skills and interests
def parsepeopledata(dictval):
  fullname= dictval["first_name"]
  print("fullname "+fullname)
  gender= dictval["gender"]
  print("gender "+gender)
  twitter_username= dictval["twitter_username"]
  print("twitter_url "+twitter_username)

  if "industry" in dictval:
    industry=dictval["industry"]
  else:
    industry=""
  print("industry "+industry)
  if "age" in dictval:
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
        if school["majors"]:
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
  # salary=">"+str(usertup[2])
  print(age)
  print(job)
  # print(salary)
  # persondict=get_person(age,job)
  parsed_dict= parsepeopledata(dictval1)
  # print(parsed_dict)
  return (parsed_dict,job,status,product)


