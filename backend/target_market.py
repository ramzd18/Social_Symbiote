# from datasets import load_dataset
# from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import re
# classifier = pipeline('zero-shot-classification')
# text ="""This group consists of individuals who are on the cusp of becoming professional esports players. They may participate in semi-professional leagues or aspire to break into the professional scene.
# They seek controllers that offer a competitive edge and are willing to invest in equipment to improve their gameplay."""
# labels = ['young', 'old']
# result = classifier(text, labels)
# print(result)

class GptMarketScrapeException(Exception):
    "Raised when GPT market group analysis is not three groups"
    pass



def generate_target_market(productdescription,targetmarket,question): 
    llm = OpenAI(openai_api_key="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")
    template = """
{context}
{question}
Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["context","question"])
    formatted_prompt=  prompt.format(
        context=f""" I am building a product that {productdescription}. My target market is {targetmarket}""",
        question=f"""{question}"""
    )
    prediction= llm.predict(formatted_prompt)
    result = [x.strip() for x in prediction.split(',')]
    return result
productdescription="A new age video game controller that optimizes gaming"
targetmarket= """My target market is young esport gamers"""
question="""Can you  specify three specific groups within this target market focus and for each group include a paragrap description of each group and an age range"""
# print(generate_target_market(productdescription,targetmarket,question))
examplestr= ['Group 1: Competitive Esports Players: This group consists of gamers who take gaming very seriously and compete in tournaments or leagues. They are typically aged between 15-25 and have an extensive knowledge of video games. They are highly involved in the gaming community', 'often streaming their games and discussing strategies with other players.\n\nGroup 2: Casual Esports Players: This group consists of gamers who enjoy playing video games as a hobby', 'but do not take part in tournaments or leagues. They are typically aged between 10-30 and are interested in having fun with video games. They typically have a moderate knowledge of video games and often seek out advice from other players.\n\nGroup 3: Professional Esports Players: This group consists of gamers who play video games professionally', 'either for teams or as individual players. They are typically aged between 18-30 and have an extensive knowledge of video games. They are highly invested in the gaming community', 'often streaming their games and discussing strategies with other players. They have invested a lot of time and effort into becoming professional gamers and are very dedicated to their craft.']


### Function that scrapes gpt output and return list of each target market group and their ages in a list of tuples
def scrape_gpt_target_market(output):
   output= ' '.join(output)
   list=output.splitlines()
   while("" in list):
      list.remove("")
   if(len(list)==3):
      group1= list[0]
      agerange1=(-1,-1)
      temp = re.findall(r'\d+', group1)
      for i in range(len(temp)-1):
         if group1.__contains__(temp[i]+"-"+temp[i+1]):
            agerange1=(temp[i],temp[i+1])
            break
      agerange2=(-1,-1)
      group2= list[1]
      temp1 = re.findall(r'\d+', group2)
      for i in range(len(temp1)-1):
         if group2.__contains__(temp1[i]+"-"+temp1[i+1]):
            agerange2=(temp1[i],temp1[i+1])
            break
      agerange3=(-1,-1)
      group3=list[2]
      temp2 = re.findall(r'\d+', group3)
      for i in range(len(temp2)-1):
         if group3.__contains__(temp2[i]+"-"+temp2[i+1]):
            agerange3=(temp2[i],temp2[i+1])
            break
      return([(group1,agerange1),(group2,agerange2),(group3,agerange3)])
   else: 
    raise GptMarketScrapeException

# Function that scrapes gpt output about target market in list format and returns a list of the age ranges in tuple format for each recommended gpt group. 
def generate_age_names_market(list_of_market_tuples): 
   first_age_tuple=list_of_market_tuples[0]
   second_age_tuple= list_of_market_tuples[1]
   third_age_tuple=list_of_market_tuples[2]
   return [first_age_tuple,second_age_tuple,third_age_tuple]
   
testmarket= scrape_gpt_target_market(examplestr)
ages= generate_age_names_market(testmarket)


def generate_interviewdoc(agent,problem,product):
  listquestions=["Tell me about yourself","What are some interests/hobbies you have and what do you like doing","Desribe your personality.",f"Do you think this problem: {problem} is a problem that you have", f"What are some pain points you might have with this problem: {problem}",f"Given this product:{product} can you think of any alternative comapnies and products you use. Desrcribe how you use these alternatives.",f"What are your thoughts about this product: {product}. Is it something you would use reguarly? Do you think it would be useful for you.",f"What are your biggest concerns about this product{product}. WHy might you not buy it? What worries you? What do you think could be a potential issue for you?",f"Score the following product: {product} on how well it does in the fields of usabillity, value proposition and likelihood to recommend. Score each from 0 to 1 and return the scores in a list. For example you might return [.43,.51,.88]. Only put the numbers in the list."]
  counter=0; 
  contextdoc=""
  interviewdoc=""
  interviewlist=[]
  for question in listquestions:
   try: 
      print("question iteration")
      interviewdoc+=f"Question: {question}" 
      response=agent.generate_question_response_interview(question,contextdoc)
      interviewdoc+=f"Anwser: {response}"
      interviewlist.append(response)
      if counter>2: 
         contextdoc+=f"Question: {question}" 
         contextdoc+=f"Anwser: {response}"
      counter+=1
   except Exception as e:
      print("ERROr", e)
      interviewdoc+=f"Question: {question}"
      interviewdoc+=f"Anwser: NO response"

      interviewlist.append("NO ANWSER") 


  dict={}
  dict["Tell me about yourself"]=interviewlist[0]
  dict["Interests & hobbies"]=interviewlist[1]
  dict["Personality traits"]=interviewlist[2]
  dict["Thoughts on problem"]=interviewlist[3]+"\n"+interviewlist[4]
  dict["Competitors"]=interviewlist[5]
  dict["Thoughts on product"]=interviewlist[6]
  dict["Concerns about product"]=interviewlist[7]
  dict["Scores"]= interviewlist[8]

  return dict
