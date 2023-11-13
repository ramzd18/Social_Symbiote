# Creating keyword list
import praw
import pandas as pd
from praw import reddit
import logging

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

from sklearn.feature_extraction.text import TfidfVectorizer
import requests
import json
from requests.auth import HTTPBasicAuth
import random
from prawcore.exceptions import Forbidden
from fuzzywuzzy import fuzz




##### Requires inputted interst list is seperted by commas
##### Given a list of the persons interests returns subreddits that may interest them. 
def get_commmon_subreddit(interests_list):     
  # list= interests_list.split(',')
  list=interests_list
  listlen = len(list)
  if (listlen>10):
     random.shuffle(list)
     list= list[:10]

  iteramount= 10//len(list)
  reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                          client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                          user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                          )

  # Searching in all subreddits  
  # creating lists for storing scraped data
  subreddit_dict= {'subreddits':[]}
  count_dict={}
  for interest in list: 
    # for submission in all.search(interests_list, limit=4):
    #     submission_post = reddit.submission(id=submission.id)
    #     subreddit_name = submission_post.subreddit.display_name
      subreddits = reddit.subreddits.search(interest, limit=iteramount)
      subreddits= [subreddit.display_name for subreddit in subreddits]

      for subreddit in subreddits:
        if(subreddit_dict['subreddits'].__contains__(subreddit)):
            count_dict[subreddit]+=1
        else :
            count_dict[subreddit]=1
            subreddit_dict['subreddits'].append(subreddit)
  return count_dict




##This function takes in a list of subreddits a person is interested in and a list of their interests. It then goes throught their favorite subreddits and finds top contirbutors in them
## and returns the contributor whose comments are the most similair to the persons interests. 
def get_users(interestslist, countsdict):
  reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                          client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                          user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                          )
  print(type(countsdict))
  l=[(k,v) for k,v in countsdict.items()]
  random.shuffle(l)
  subs_dict = dict(l)

  nonelist=["announcements","funny","AskReddit","aww","pics","videos","todayilearned","Showerthoughts","explainlikeimfive","mildlyinteresting","nottheonion","memes","shitposting"] 
  count=0 
  subslist=[]
  for key in subs_dict: 
     if count>3: 
        break 
     if key not in nonelist:
      subslist.append(key)
      count+=1
  max_user=""
  max_count=0
  comments_list=[]

  print("finished sub loop list count" + str(len(subslist)))
  for list in subslist: 
    print("beginning loop")
    try:
      subreddit= reddit.subreddit(list)
      new_posts= subreddit.new(limit=3)
      for submission in new_posts:
          submit= reddit.submission(submission.id)
          authorname=str(submit.author)
          if authorname=="AutoModerator":
             continue 
          user=reddit.redditor(authorname)
          totalkarma=1
          try: 
            totalkarma=int(user.comment_karma)
          except: 
             ()
          if(totalkarma>10000): 
             continue
          submissions_text= user.submissions.new(limit=None)
          text_str=""
          comments=[]
          count=0
          for comment in submissions_text: 
            body=str(comment.title)
            if(count<100):
              text_str+=". "+body
              count+=1
            comments.append(body)
          sim_score=similairty_text(str(interestslist),text_str)
          final_score= (count) * sim_score
          if final_score>max_count:
            max_count=final_score
            max_user=authorname
            comments_list=submissions_text
    except Forbidden:
       print("private subreddit")


  return (max_user,comments_list)

def match_comments_with_titles(username, commentslist,name):
  reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                          client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                          user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                          )

  handler = logging.StreamHandler()
  handler.setLevel(logging.DEBUG)
  for logger_name in ("praw", "prawcore"):
      logger = logging.getLogger(logger_name)
      logger.setLevel(logging.DEBUG)
      logger.addHandler(handler)
  user = reddit.redditor(username)
  comments = user.comments.new(limit=2)  # Retrieve all comments, you can specify a limit if needed
  total_commented_posts=[]
  print("before comments")
  for comment in comments:
    post = comment.submission
    total_commented_posts.append(post.title)
  print("after comments")
  if(len(commentslist)!=len(total_commented_posts)):
    print("Mismatch length")
  else: 
    index=0
    print("before posts")
    for post in total_commented_posts:
      commentslist[index]="Someone posted: "+total_commented_posts[index]+ f"and {name} responded with "+ commentslist[index]
      index+=1
  return commentslist


def find_most_relevant_submissions(interests,submissions,user):
    reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                          client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                          user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                          )
    user=reddit.redditor(user)
    submissions_text= user.submissions.new(limit=None)

    dictval={}
    comments=[]
    # print("submissions length"+ str(len(submissions)))
    for post in submissions_text: 
      body=str(post.title)
      dictval[body]=similairty_text(str(interests),body)
    sorted_dict = dict(sorted(dictval.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    count = 0
    first_100_elements=[]
    for key, value in sorted_dict.items():
      first_100_elements.append(key)
      count += 1
      if count == 200:
          break
    return first_100_elements


   
### Takes two texts and returns the similairy score between them . 
def similairty_text(interests_text, comment_text):
  text1 = interests_text
  text2 = comment_text
  similarity = fuzz.ratio(text1, text2)

  return similarity/100




# interestslist= [['writing', 'children', 'languages', 'traveling', 'education', 'dancing', 'editing', 'photography', 'reading', 'music', 'poverty alleviation', 'grammar', 'human rights', 'animal welfare', 'organizing', 'health']]
# subredditslist= get_commmon_subreddit(interestslist)
# user= get_users(interestslist,subredditslist)
# print(user[0])
# print(user[1])
# print(find_most_relevant_submissions(interestslist,user[1],user[0]))