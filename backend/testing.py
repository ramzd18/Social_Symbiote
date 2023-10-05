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
str= """You are following a certain company on social media and you see a tweet they published. Tell me if you liked the tweet and what you would change about it. Here is the tweet: I find it pretty incredible, that a house brand golf ball from Dicks Sporting Goods has two of the best scores ever in our Ball Lab.
There are golf ball companies who have spent millions of dollars 💵 on R&D and been making balls for decades that aren’t making a ball as consistent as a Maxfli.

Credit where credit is due. Nice job to everyone making the Maxfli golf ball. 

It’s a hellova a ball for a hell of a price. You are not only competing with the big boys you are kicking some of their butts.
"""
output=(Ram_agent._generate_reaction(str,""))
print(output)