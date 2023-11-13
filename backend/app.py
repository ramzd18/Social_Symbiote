from flask import Flask, session, request, redirect, url_for
import retrieve_agent
import load_agent_database
import json
app = Flask(__name__)
app.secret_key = "super secret key"
agents_dict={}





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
        print (question)
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
# @app.route('/create_agent')
# def create_agent():
     

if __name__ == '__main__':
    app.run(debug=True)