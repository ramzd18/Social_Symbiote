


agents_dict={}
initialized={}


def load_agents_task(email):
    agents_lists = retrieve_agent.get_all_agents(email)
    print("This is the email"+str(email)+" This is the totallength"+str(len(agents_lists)))
    print("List type"+ str(type(agents_lists)))
    # first,second,third= load_agent_database.split_into_three(agents_lists)
    if(len(agents_lists)>=3):
      with ThreadPoolExecutor(max_workers=3) as executor:
          futures = [executor.submit(load_agent_database.LoadAgent, email,arg[0]) for arg in agents_lists]
          results = [future.result() for future in futures]
      # for agent in agents_lists: 
      #     print("Agentsn name is "+ str(agent[0]))
      #     agents_dict[agent[0]]= load_agent_database.LoadAgent(email,agent[0])
      print("The length of results is"+ str(len(results)))
      for result in results:
        agents_dict[result.name]=result
    else: 
        for agent in agents_lists: 
          print("second route")
          print("Agentsn name is "+ str(agent[0]))
          agents_dict[agent[0]]= load_agent_database.LoadAgent(email,agent[0])
    print("Total length of dict"+ str(len(agents_dict)))
    initialized["initial"]="true"
    return"true"
def create_database_agent(email,job,description,age): 
        (agent,gender,jobval)=CreateAgentFinal.create_and_store_agent(description,age,job)
        agent_memory= agent.memory.memory_retriever.dict()
        agent_soc_memory=agent.memory.social_media_memory.dict()
        del agent_memory['vectorstore']
        del agent_soc_memory['vectorstore']
        retrieve_agent.push_agent_info(agent.name,agent.age,agent.status,json.dumps(str(agent_memory)),json.dumps({}),email,json.dumps(str(agent_soc_memory)),agent.education_and_work,json.dumps(agent.memory.personalitylist),agent.interests,gender,jobval,description)
        agents_dict[agent.name]=agent
        initialized[description]="true"
        return "true"

from flask import Flask, session, request, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_executor import Executor

import retrieve_agent
import load_agent_database
import json
import CreateAgentFinal
import os
from concurrent.futures import ThreadPoolExecutor, wait
from worker import conn
from app import agents_dict
import json
from flask import jsonify 
import time
# q = Queue(connection=conn)

app = Flask(__name__)
app.secret_key = "super secret key"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'

os.environ['KMP_DUPLICATE_LIB_OK']='True'
executor = Executor(app)

@app.route('/initialize_agents')
def loads_users():
    email = request.args.get("email").strip()
    # job = q.enqueue(load_agents_task, email)
    executor.submit(load_agents_task,email)
    # Wait for the job to finish with a timeout (e.g., 30 seconds)
    
        # if job.is_finished:
        #     print("The result is", job.result)
        #     for key, value in job.result.items():
        #         print("Adding", key, value)
        #         agents_dict[key] = value
        #     break
        # elif time.time() - start_time > timeout:
        #     print("Job timed out")
        #     break
        # else:
        #     time.sleep(0.5)  # Wait for a short period before checking again

    return "starting"

@app.route('/load_response')
def generate_response():
        print("initialized length:" + str(len(initialized)))
        name= request.args.get("name").strip()
        print("Length of agents_dict"+ str( len(agents_dict)))
        question=str(request.args.get("question"))
        current_agent= agents_dict[name]
        return str(current_agent.generate_question_response(question))
@app.route('/update_agent')
def update_agent():
        print("Starting")
        name= request.args.get("name").strip()
        current_agent= agents_dict[name]
        memory= current_agent.memory.memory_retriever.dict()
        del memory['vectorstore']
        email=request.args.get("email").strip()
        retrieve_agent.update_agent_info(email,name,json.dumps(str(memory)),json.dumps(current_agent.memory.personalitylist))
        return "Completed"

@app.route('/create_agent')
def create_agent():
        print("Starting")
        email= request.args.get("email").strip()
        description=request.args.get("description").strip()
        age=int(request.args.get("age").strip())
        job=request.args.get("job").strip()
        # memory= current_agent.memory.memory_retriever.dict()
        # del memory['vectorstore']
        # # email=request.args.get("email").strip()
        # (agent,gender,jobval)=CreateAgentFinal.create_and_store_agent(description,age,job)
        # agent_memory= agent.memory.memory_retriever.dict()
        # agent_soc_memory=agent.memory.social_media_memory.dict()
        # del agent_memory['vectorstore']
        # del agent_soc_memory['vectorstore']
        # retrieve_agent.push_agent_info(agent.name,agent.age,agent.status,json.dumps(str(agent_memory)),json.dumps({}),email,json.dumps(str(agent_soc_memory)),agent.education_and_work,json.dumps(agent.memory.personalitylist),agent.interests,gender,jobval,description)
        # agents_dict[agent.name]=agent
        executor.submit(create_database_agent,email,job,description,age)
        return "Completed"


@app.route('/marketing')
def market_make():
        context=request.args.get("context")
        agent_name= request.args.get("name").strip()
        tagline= request.args.get("tagline")
        agent=agents_dict.get(agent_name)
        response= agent.marketing_analysis(tagline,context)
        list=response.split(",")[:4]
        final=response.split("optimized_message")
        last=final.split(':')[1]
        print("This is the actual list"+ str(list))
        actuallist=[]
        count=0; 
        for li in list: 
            if(count<4):
                try:
                    li1=li.split(':')[1]
                    actuallist.append(float(li1))
                except: 
                    actuallist.append(float(0.5))
            else: 
                print(li)
                li1= str(li).split(':')[1]
                actuallist.append(li1)
            count+=1
        print(actuallist)
        actuallist.append(last)
        return actuallist
@app.route('/agentslist')
def agentslist(): 
     list=[]
     for key in agents_dict.keys():
          list.append(key)
     return jsonify({
        'ok': True, 
        'msg':'Success',
        'data': list
    })
@app.route('/check')
def check_status():
    print(len(initialized))
    key= request.args.get("key")
    if  initialized.__contains__(key):
        return {'status': 'finished'}
    else:
        return {'status': 'pending'}

if __name__ == '__main__':
    app.run(debug=True)

