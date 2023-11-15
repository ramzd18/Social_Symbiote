import requests
import os
import json
import re
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
os.environ['BEARER_TOKEN']="AAAAAAAAAAAAAAAAAAAAAFoQRQEAAAAAHhsIv0rF%2FFj%2FmshUjYv3SzUn5Ug%3Dkho8eAYsO20pMEzMFjIkoOR2dGDLscEMdITwSAqGqWdyYA2Bax"
bearer_token = os.environ.get("BEARER_TOKEN")

#### 3 avalibale options for query parameter: liked_tweets, tweets, and mentions
def create_url(user_id,query,max_results):
    # Replace with user ID below
    # user_id = 2244994945
    return "https://api.twitter.com/2/users/{}/{}?max_results={}".format(user_id,query,max_results)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def clean_tweets(dicttweets):
  tweetlist=[]
  print(dicttweets)
  data= dicttweets['data']
  for tweet in data: 
    text= tweet['text']
    tweetlist.append(text)
  return tweetlist

def clean_likedtweets(dicttweets):
  retweetslist=[]
  pattern = r'\b@\w+\b'

  data=dicttweets['data']
  for retweet in data: 
    text=retweet['text']
    cleaned_text=re.sub(pattern, '', text)
    retweetslist.append(cleaned_text)
  return retweetslist

def clean_mentiontweets(dicttweets):
  mentionslist=[]
  pattern = r'\b@\w+\b'
  data=dicttweets['data']
  for retweet in data: 
    text=retweet['text']
    cleaned_text=re.sub(pattern, '', text)
    mentionslist.append(cleaned_text)
  return mentionslist
def main(userid,query,size):
    url = create_url(userid,query,size)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    return json_response
    # print(json.dumps(json_response, indent=4, sort_keys=True))




# main()