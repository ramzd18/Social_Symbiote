import promptLLMmemories

def add_memories_to_agent(agent,added_memory): 
   agent_observations=promptLLMmemories.generate_relevant_memories(added_memory)
   for observation in agent_observations:
     agent.memory.add_memory(observation)
     
   return agent 

