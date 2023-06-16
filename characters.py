import requests

def my_function(character_name: str):
    print("Called characters() function with " + str)
    url = ("https://zelda.fanapis.com/api/characters?name=" + character_name)
    response = requests.get(url=url)
    print(response.json())
