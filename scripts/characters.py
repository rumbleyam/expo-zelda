import requests
from constants import CHARACTER_NAME_ENDPOINT

def characters(character_name: str):
    print("Called characters() function with " + character_name)
    url = (CHARACTER_NAME_ENDPOINT + character_name)
    response = requests.get(url=url)
    print(response.json())
    return response.json
