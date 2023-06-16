import requests
from constants import GAMES_LIST_ENDPOINT

def games():
    print("Called games() function")
    url = (GAMES_LIST_ENDPOINT)
    response = requests.get(url=url)
    print(response.json())
    return response.json

def retrieve_game_id(game_id: str):
    print("Called retrieve_game_id() with " + game_id)
    if ':' in game_id:
        url = (GAMES_LIST_ENDPOINT + game_id)
    else:
        url = (GAMES_LIST_ENDPOINT + ":" + game_id)
    response = requests.get(url=url)
    return response.json 