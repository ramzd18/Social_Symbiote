import requests

url = "https://reviewindexapi.datashake.com/reviews"
params = {
    "api_key": "a73fcc1bec6ac4d705cfad7ed432e28b565effeb",
    "callback": "https://www.example.com/reviewindexapi_callback",
    "domain": "syntheticusers.com"
}
response = requests.get(
    url=url,
    params=params
)
print(response)