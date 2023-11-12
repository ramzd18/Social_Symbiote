# import requests
# import requests.auth
# client_auth = requests.auth.HTTPBasicAuth('p-jcoLKBynTLew', 'gko_LXELoV07ZBNUXrvWZfzE3aI')
# post_data = {"grant_type": "password", "username": "Rpeddu", "password": "Jeff@2234"}
# headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# print(response.json())

# # {u'access_token': u'fhTdafZI-0ClEzzYORfBSCR7x3M',
# #  u'expires_in': 3600,
# #  u'scope': u'*',
# #  u'token_type': u'bearer'}
import praw

def reddit_scraper(username):

    reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                        client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                        user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)',
                        )
    username = "AdeptnessJazzlike617"
    user = reddit.redditor(username)
    comments = user.comments.new(limit=None)
    print("reached")
    my_dict = {'username': username, 'comments': [], 'subreddits': [], 'goldstatus': False}
    dict_of_subreddits = {}
    my_dict['goldstatus'] = (user.is_gold)
    my_dict['downvoted'] = (user.downvoted)

    for comment in comments:
        if (my_dict['subreddits'].__contains__(comment.subreddit.display_name)):
            dict_of_subreddits[comment.subreddit.display_name] += 1
        else:
            my_dict['subreddits'].append(comment.subreddit.display_name)
            dict_of_subreddits[comment.subreddit.display_name] = 1
        my_dict['comments'].append(comment.body)
        
    sorted_dict = dict(sorted(dict_of_subreddits.items(), key=lambda item: item[1]))
    top_keys = {}
    count = 0
    for key in sorted_dict:
        if count == 5:
            break
        subreddit = reddit.subreddit(key)
        top_keys[key] = []
        for submission in subreddit.hot(limit=5):
            top_keys[key].append(submission.selftext)
        count += 1
    return (sorted_dict,top_keys)
 
# print(my_dict['downvoted'])
