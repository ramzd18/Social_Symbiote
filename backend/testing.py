import load_agent_database
import agent_memories_maintainance
import retrieve_agent
import promptLLMmemories


Ram_agent=load_agent_database.LoadAgent('rbpeddu@gmail.com','Ram')
# Ram_agent= agent_memories_maintainance.add_memories_to_agent(Ram_agent,"Generate memories for Ram about how he wants to buy some of his favorite sports teams jerseys but needs to save money")
# data=retrieve_agent.altermemories(Ram_agent,'Ram','rbpeddu@gmail.com')
# print(data)
# data=retrieve_agent.retrieve_agents_record('rbpeddu@gmail.com','Ram')
# print(data)
str= """You are being interviewed by a company about their product. Tell me what you like and do not like about the product. Here is the product: Bluetooth headphone that can detect your face movements to lower and raise volume and also end or start calls.
"""
output=(Ram_agent._generate_reaction(str,""))
print(output)