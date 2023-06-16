import requests
from scripts.constants import CHARACTER_NAME_ENDPOINT

def retrieve_characters_name(character_name: str):
    print("Called characters() function with " + character_name)
    url = (CHARACTER_NAME_ENDPOINT + character_name)
    response = requests.get(url=url)
    return response.json()
