import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
os.environ['BEARER_TOKEN']="AAAAAAAAAAAAAAAAAAAAAFoQRQEAAAAAHhsIv0rF%2FFj%2FmshUjYv3SzUn5Ug%3Dkho8eAYsO20pMEzMFjIkoOR2dGDLscEMdITwSAqGqWdyYA2Bax"
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url(username):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    user_fields = "user.fields=id"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by/username/{}".format(username)
    print(url)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def find_user(username):
    url = create_url(username)
    json_response = connect_to_endpoint(url)
    data=json_response['data']
    return data['id']


