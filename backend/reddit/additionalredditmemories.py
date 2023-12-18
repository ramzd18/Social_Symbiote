
import praw
import pandas as pd
from praw import reddit

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

from sklearn.feature_extraction.text import TfidfVectorizer
import requests
import json
from requests.auth import HTTPBasicAuth
import random
from prawcore.exceptions import Forbidden
from fuzzywuzzy import fuzz
from langchain.llms import OpenAI




def get_commmon_subreddit(val):     
  # list= interests_list.split(',')
  # list=interests_list
  # listlen = len(list)
  # if (listlen>10):
  #    random.shuffle(list)
  #    list= list[:10]

  # iteramount= 10//len(list)
  reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                          client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                          user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                          )

  # Searching in all subreddits  
  # creating lists for storing scraped data
  
  # for interest in list: 
    # for submission in all.search(interests_list, limit=4):
    #     submission_post = reddit.submission(id=submission.id)
    #     subreddit_name = submission_post.subreddit.display_name
  subreddits = reddit.subreddits.search(val, limit=2)
  subreddits= [subreddit.display_name for subreddit in subreddits]
  sub_name=subreddits[0]
  subreddit=reddit.subreddit(sub_name)
  top_posts = subreddit.top(time_filter='day', limit=5)
  list=[]
  for submission in top_posts:
    list.append(submission.author)
  return list


#### Finds plausible redditors for person based on their interest list
### Requires you input something of list format 
def get_common_subreddit_interestlist(iterestlist): 
  totalredditorlist=[]
  print(iterestlist)
  random.shuffle(iterestlist)
  iterestlist=iterestlist[:5]
  for iterest in iterestlist: 
    print(iterest)
    totalredditorlist.append(get_commmon_subreddit(iterest))
  flattened_list = [item for sublist in totalredditorlist for item in sublist]
  return flattened_list


def total_comments(interestslst): 
  new_list=interestslst.split(',')
  totlist=[]
  for sub in new_list: 
    comms=get_commmon_subreddit(sub)
    totlist+=comms
  return totlist 

def add_reddit_mems(query): 
  reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                          client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                          user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                          )
  subreddit = reddit.subreddit('all')
  for submission in subreddit.search(query, sort='hot', limit=25):
    print(submission.title)


def determine_most_similair_redditor(interestlist,authorlist): 
  max_user=""
  comments_list=[]
  submissions_list=[]
  max_count=0
  for author in authorlist: 
        authorname=author.name
        if authorname=="AutoModerator":
            continue 
        # user=reddit.redditor(authorname)
        totalkarma=1
        try: 
          totalkarma=int(author.comment_karma)
        except: 
            ()
        if(totalkarma>10000): 
            continue
    
        submissions_text= author.submissions.new(limit=150)
        commentes_text= author.comments.new(limit=150)
        # sorted_comments=sorted(commentes_text, key=lambda comment: len(comment.body), reverse=True)
        # sorted_submissions= sorted(submissions_text,key=lambda submit: len(submit.title), reverse=True)
        # print(type(sorted_submissions))
        text_str=""
        comments=[]
        count=0
        for submission in commentes_text: 
          body=str(submission.body)
          text_str+=". "+body
          count+=1
          comments.append(body)
        # sim_score=similairty_text(str(interestslist),text_str)
        # print(sim_score)
        print(count)
        final_score= count 
        print(authorname+" "+str(final_score))
        if final_score>max_count:
          max_count=final_score
          max_user=authorname
          comments_list=commentes_text
          submissions_list=submissions_text
  return (max_user,comments_list,submissions_list)

def gpt_redditor(max_user,comments,submissions): 
   reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                          client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                          user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                          )
   redditor = reddit.redditor(max_user)
   submissions_text= redditor.submissions.new(limit=150)
   commentes_text= redditor.comments.new(limit=150)
   sorted_comments=sorted(commentes_text, key=lambda comment: len(comment.body), reverse=True)
   sorted_submissions= sorted(submissions_text,key=lambda submit: len(submit.title), reverse=True)
   first100comments=sorted_comments[:75]
   first100submissions=sorted_submissions[:50]

   index=0
   for comment in first100comments: 
      first100comments[index]="Title of post:"+comment.submission.title+" How person responded: "+ comment.body
      print(index)
      index=index+1
   sindex=0
   for submit in first100submissions:
      first100submissions[sindex]=submit.title
      print(sindex)
      sindex=sindex+1

   return(first100comments,first100submissions)
# def prompt_gpt_reddit(comments): 
#   comments=str(comments)
#   llm = OpenAI(openai_api_key='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')
#   prompt = f"The following is going to be a list of posts a user has commented on. Each value in the list is formatted so you get the post title and then the persons response. Here is the list:"
#   {comments}
#   "Given this generate an extensive list of fake addiional posts the person plausibly may have also liked and interacted with online.ONLY INCLUDE THE POST TITLES AND NOT THE PERSONS RESPONSE TO THE TITLE. Generate at least 50 posts. DO not makeless then 50 posts. Do not only make a couple posts. Make them as creative as possible. Seperate each one with a semicolon. Example format: post1;post2;post3;post4;post5;post6; until post50; "
#   response = llm(prompt)
#   print("getting response now")
#   print(response)

# (user,coms,sums)= determine_most_similair_redditor(["sports","camping","home_improvement","traveling","music","concerts"],get_common_subreddit_interestlist(["sports","camping","home_improvement","traveling","music","concerts"]))
# (foms,fubs)=gpt_redditor(user,coms,sums)
# print(foms)
# print(fubs)
# totallist=[]
# print(type(fubs))
# for va in foms: 
#    totallist.append(va)
# for val in fubs: 
#    totallist.append(val)
# for val2 in totallist: 
#    print(type(val2))

