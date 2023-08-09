import requests

def post(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    return response.json()

def get(url, data=None, headers=None):
    response = requests.post(url, json=data, headers=headers)
    return response.json()
