import requests
from scripts.constants import CHARACTERS_LIST_ENDPOINT, CHARACTER_NAME_ENDPOINT

def characters():
    response = requests.get(url=CHARACTERS_LIST_ENDPOINT)
    return response.json()

def retrieve_characters_name(character_name: str):
    print("Called characters() function with " + character_name)
    url = (CHARACTER_NAME_ENDPOINT + character_name)
    response = requests.get(url=url)
    return response.json()
