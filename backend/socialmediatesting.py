import retrieve_agent
import load_agent_database

from concurrent.futures import ThreadPoolExecutor, wait


def load_agents_task( email):
    agents_dict={}
    agents_lists = retrieve_agent.get_all_agents(email)
    print("List type"+ str(type(agents_lists)))
    # first,second,third= load_agent_database.split_into_three(agents_lists)
    if(len(agents_lists)>=3):
      with ThreadPoolExecutor(max_workers=3) as executor:
          futures = [executor.submit(load_agent_database.LoadAgent, 'rbpeddu@gmail.com',arg[0]) for arg in agents_lists]
          results = [future.result() for future in futures]
      # for agent in agents_lists: 
      #     print("Agentsn name is "+ str(agent[0]))
      #     agents_dict[agent[0]]= load_agent_database.LoadAgent(email,agent[0])
      for result in results:
        agents_dict[result.name]= result
    else: 
        for agent in agents_lists: 
          print("Agentsn name is "+ str(agent[0]))
          agents_dict[agent[0]]= load_agent_database.LoadAgent(email,agent[0])
    return  agents_dict





