import requests
from scripts.constants import MONSTERS_LIST_ENDPOINT, MONSTER_NAME_ENDPOINT

def monsters():
    response = requests.get(url=MONSTERS_LIST_ENDPOINT)
    return response.json()

def retrieve_monsters_name(monster_name: str):
    print("Called monsters() function with " + monster_name)
    url = (MONSTER_NAME_ENDPOINT + monster_name)
    response = requests.get(url=url)
    return response.json()
