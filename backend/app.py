from flask import Flask, session, request, redirect, url_for
from flask_cors import CORS, cross_origin



from backend import retrieve_agent 
from backend import load_agent_database
import json
from backend import CreateAgentFinal
import requests
import logging
import os
from flask_executor import Executor
from concurrent.futures import ThreadPoolExecutor, wait
from backend import target_market
import time


app = Flask(__name__, static_folder='../build', static_url_path='/')
app.secret_key = "super secret key"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
executor = Executor(app)

agents_dict={}
initialized={}


os.environ['KMP_DUPLICATE_LIB_OK']='True'


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

app.logger.info("Starting flask...")

# @app.route('/node/<path:subpath>', methods=['GET', 'POST'])
# def node_route(subpath):
#     app.logger.info(f"Handling /node/{subpath}")

#     # Assuming you want to pass the entire request to the Node.js server
#     response = requests.request(
#         method=request.method,
#         url='https://alias-testing-130265f16331.herokuapp.com/node' + subpath,
#         headers=request.headers,
#         data=request.get_data(),
#         cookies=request.cookies,
#         allow_redirects=False,
#     )

#     app.logger.info(f"Node.js server response: {response.status_code}")
#     return response.content, response.status_code, response.headers.items()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # print("Catch-all route reached!")
    # app.logger.info(f"Path: {path}")

    # if path.startswith('/node'):
    #     node_url = 'https://alias-testing-130265f16331.herokuapp.com/node' + path
    #     app.logger.info(f"Forwarding request to Node.js server: {node_url}")
    #     response = requests.request(
    #         method=request.method,
    #         url=node_url,
    #         headers=request.headers,
    #         data=request.get_data(),
    #         cookies=request.cookies,
    #         allow_redirects=False,
    #     )
    #     app.logger.info(f"Node.js server response: {response.status_code}")
    #     return response.content, response.status_code, response.headers.items()
    
    # app.logger.info(f"Serving static file for path: {path}")
    return app.send_static_file('index.html')
def load_agents_task(email):
    agents_lists = retrieve_agent.get_all_agents(email)
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

def interviewdoc(agentval,problem,product,agent): 
    targetdict=target_market.generate_interviewdoc(agentval,problem,product)
    print("FINSIHED INTERVEIWING")
    print("FINSIHED INTERVEIWING")
    print("FINSIHED INTERVEIWING")
    print("BEFORE PRINTING")
    print(problem+agent)
    print("AFTER PRINTING")
    initialized[product+agent]=targetdict
    return "Completed"

@app.errorhandler(404)   
def not_found(e):   
  app.logger.info("404 error")
  return app.send_static_file('index.html')

@app.route('/initialize_agents')
def loads_users():
    email = request.args.get("email").strip()
    executor.submit(load_agents_task,email)
    return "starting"


@app.route('/load_response')
def generate_response():
    
        name= request.args.get("name").strip()
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
        executor.submit(create_database_agent,email,job,description,age)
        return "Completed"
  
@app.route('/check')
def check_status():
    print(len(initialized))
    key= request.args.get("key")
    if  initialized.__contains__(key):
        return {'status': 'finished'}
    else:
        return {'status': 'pending'}
    
@app.route('/checkval')
def check_status1():
    print(len(initialized))
    key= request.args.get("key")
    if  initialized.__contains__(key):
        return initialized[key]
    else:
        return {'status': 'pending'}




@app.route('/interview')
def interview():
    for key in agents_dict:
        print("loop")
        print(key)
    problem=request.args.get("problem").strip()
    product=request.args.get("product").strip()
    agent=request.args.get("agent").strip()
    email=request.args.get("email").strip()
    print("Starting")
    print("problem : "+ problem)
    print("product: "+ product)
    try: 
        agentval=agents_dict[agent]
    except: 
        # time.sleep(2)
        agentval=load_agent_database.LoadAgent(email,agent)
    executor.submit(interviewdoc,agentval,problem,product,agent)
    # targetdict=target_market.generate_interviewdoc(agentval,problem,product)
    # initialized[problem+product]='finished'
    return {'status':'finsihed'}
    

