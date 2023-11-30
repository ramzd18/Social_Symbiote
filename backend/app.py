from flask import Flask, session, request, redirect, url_for
from flask_cors import CORS, cross_origin

# import retrieve_agent 
import load_agent_database
import json
import CreateAgentFinal
import os

app = Flask(__name__, static_folder='../build', static_url_path='/')
app.secret_key = "super secret key"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
agents_dict={}

os.environ['KMP_DUPLICATE_LIB_OK']='True'

@app.route('/')
def index():
    # Render the main HTML file from the React build
    return app.send_static_file('index.html')

@app.route('/initialize_agents')
def loads_users():
    email= request.args.get("email").strip()
    agents_lists= retrieve_agent.get_all_agents(email)
    print("List type"+ str(type(agents_lists)))
    for agent in agents_lists: 
        print("Agentsn name is "+ str(agent[0]))
        agents_dict[agent[0]]= load_agent_database.LoadAgent(email,agent[0])
    
    return 'Agents initiialized'

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
        # memory= current_agent.memory.memory_retriever.dict()
        # del memory['vectorstore']
        # email=request.args.get("email").strip()
        (agent,gender,jobval)=CreateAgentFinal.create_and_store_agent(description,age,job)
        agent_memory= agent.memory.memory_retriever.dict()
        agent_soc_memory=agent.memory.social_media_memory.dict()
        del agent_memory['vectorstore']
        del agent_soc_memory['vectorstore']
        retrieve_agent.push_agent_info(agent.name,agent.age,agent.status,json.dumps(str(agent_memory)),json.dumps({}),email,json.dumps(str(agent_soc_memory)),agent.education_and_work,json.dumps(agent.memory.personalitylist),agent.interests,gender,jobval,description)
        agents_dict[agent.name]=agent
        return "Completed"


if __name__ == '__main__':
    app.run(debug=True)