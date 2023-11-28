
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
  subreddits = reddit.subreddits.search(val, limit=1)
  subreddits= [subreddit.display_name for subreddit in subreddits]

  sub_name=subreddits[0]
  subreddit=reddit.subreddit(sub_name)
  top_posts = subreddit.top(limit=25)
  list=[]
  for submission in top_posts:
    list.append(submission.title)

  return list

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


