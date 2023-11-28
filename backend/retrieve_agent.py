import NewAgentCreation
import psycopg2
import json 
def push_user_info(first,last,email):
      conn = psycopg2.connect(
      host="35.233.155.93",
      database="user-agents",
      user="postgres",
      password="Jeff@2234")
      cur = conn.cursor()
      print('PostgreSQL database version:')
      postgres_insert_query = """ INSERT INTO user_info (firstname, lastname, email) VALUES (%s,%s,%s)"""
      user_records= (first,last,email)
      cur.execute(postgres_insert_query,user_records)
      conn.commit()
      count = cur.rowcount
      print(count, "Record inserted successfully into mobile table")
      cur.close()
      conn.close()
def push_agent_info(name,age,status,memory,llm,personemail,social_media_memory,educationwork,personalitylist,interests,gender,job,user_description):
     #name,age,status,memory,llm= NewAgentCreation.add_data()
    try:
      conn = psycopg2.connect(
      host="35.233.155.93",
      database="user-agents",
      user="postgres",
      password="Jeff@2234")
      cur= conn.cursor()
      postgres_insert_query = """ INSERT INTO user_agents_info (name, age, status,memory,llm,personemail,social_media_memory,educationwork,personalitylist,interests,gender,job,user_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
      record_to_insert = (name,age,status,memory,llm,personemail,social_media_memory,educationwork,personalitylist,interests,gender,job,user_description)
      print("database here")
      cur.execute(postgres_insert_query, record_to_insert)
      print("database executed")
      conn.commit()
      count = cur.rowcount
      print(count, "Record inserted successfully into mobile table")
    
    except (Exception, psycopg2.Error) as error:
      print("Failed to insert record into mobile table", error)

    finally: 
      if conn:
          cur.close()
          conn.close()
          print("PostgreSQL connection is closed")

def update_agent_info(email,name,memory,personalitylist): 
  try:
      conn = psycopg2.connect(
      host="35.233.155.93",
      database="user-agents",
      user="postgres",
      password="Jeff@2234")
      cur= conn.cursor()
      postgres_insert_query = """ 
    UPDATE user_agents_info
    SET memory = %s, personalitylist = %s  
    WHERE personemail = %s AND name = %s;  
"""
      record_to_insert=(memory,personalitylist,email,name)
      cur.execute(postgres_insert_query, record_to_insert)
      conn.commit()
      count = cur.rowcount
      print(count, "Record inserted successfully into mobile table")
    
  except (Exception, psycopg2.Error) as error:
      print("Failed to insert record into mobile table", error)

  finally: 
      if conn:
          cur.close()
          conn.close()
          print("PostgreSQL connection is closed")
def updatesoical_agent_info(email,name,social_media_memory,personalitylist): 
  try:
      conn = psycopg2.connect(
      host="35.233.155.93",
      database="user-agents",
      user="postgres",
      password="Jeff@2234")
      cur= conn.cursor()
      postgres_insert_query = """ 
    UPDATE user_agents_info
    SET social_media_memory = %s, personalitylist = %s  
    WHERE personemail = %s AND name = %s;  
"""
      record_to_insert=(social_media_memory,personalitylist,email,name)
      cur.execute(postgres_insert_query, record_to_insert)
      conn.commit()
      count = cur.rowcount
      print(count, "Record inserted successfully into mobile table")
    
  except (Exception, psycopg2.Error) as error:
      print("Failed to insert record into mobile table", error)

  finally: 
      if conn:
          cur.close()
          conn.close()
          print("PostgreSQL connection is closed")

          

    
def retrieve_agents_record(email,agentname): 
  try:
      conn = psycopg2.connect(
      host="35.233.155.93",
      database="user-agents",
      user="postgres",
      password="Jeff@2234")
      cur= conn.cursor()
      #query="""SELECT * FROM user_agents_info WHERE (SELECT email FROM user_agents_info={email})"""
      query=f""" SELECT * FROM user_agents_info
WHERE ((personemail='{email}')
AND
(name='{agentname}'));"""
      cur.execute(query)
      conn.commit()
      data= cur.fetchone(); 
      return data
  except (Exception, psycopg2.Error) as error:
     print("Failed to inser record into mobile table",error)
     return "Error"
  finally: 
      if conn: 
         cur.close()
         conn.close()
         print("Postgresql connection closed")



# def altermemories(agent,agentname,personemail): 
#     try:
#       conn = psycopg2.connect(
#       host="35.233.155.93",
#       database="user-agents",
#       user="postgres",
#       password="Jeff@2234")
#       cur= conn.cursor()
#       query=f""" UPDATE user_agents_info 
#                 SET memory = %s
#                 WHERE (personemail='{personemail}')
#                 AND
#                 (name='{agentname}')
#                 """
#       print(query)
#       memory=agent.memory.dict()
#       memory=json.dumps(memory,default=str)
#       record_to_insert=(24)
#       cur.execute(query,[memory])
#       conn.commit()
#       data= cur.statusmessage; 
#       return data
#     except (Exception, psycopg2.Error) as error:
#       print("Failed to update agent's memory",error)
#       return "Error"
#     finally: 
#         if conn: 
#          cur.close()
#          conn.close()
#          print("Postgresql connection closed")

def get_all_agents(email): 
  try:
      conn = psycopg2.connect(
      host="35.233.155.93",
      database="user-agents",
      user="postgres",
      password="Jeff@2234")
      cur= conn.cursor()
      #query="""SELECT * FROM user_agents_info WHERE (SELECT email FROM user_agents_info={email})"""
      query=f""" SELECT * FROM user_agents_info
WHERE ((personemail='{email}'));"""
      cur.execute(query)
      conn.commit()
      data= cur.fetchall(); 
      return data
  except (Exception, psycopg2.Error) as error:
     print("Failed to inser record into mobile table",error)
     return "Error"
  finally: 
      if conn: 
         cur.close()
         conn.close()
         print("Postgresql connection closed")

def scrape_user_databse(usertup:tuple): 
   name=usertup[0]
   age=usertup[1]



# print(get_all_agents('rbpeddu@gmail.com'))

# name,age,status,memory,llm= NewAgentCreation.get_agent_initial_data()
# push_agent_info(name,age,status,memory,llm,'rbpeddu@gmail.com')

# data=retrieve_agents_record("rbpeddu@gmail.com",'Ram')
# print("This is the type of data" , data)


# print(retrieve_agents_record("akhiliyengar2004@gmail.com","michael")[10])


"fitness, gym, health and wellness,traveling,food, finance,sports"

