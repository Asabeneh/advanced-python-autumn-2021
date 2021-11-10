import requests
from pprint import pprint
# GET, PUT, POST, DELETE

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data


