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

reddit = praw.Reddit(client_id='nj0rg_lxJnxtu-h2gE_1rw',
                     client_secret='jGGnaaNdZq7aJRPax2qJkVwPs5lTWw',
                     user_agent='desktop:com.example.myredditapp:v1.2.3 (by u/Rpeddu)')

user = reddit.redditor('ayatilabs')
comments = user.comments.new()
print("reached")

for comment in comments:
    print(comment.body)
