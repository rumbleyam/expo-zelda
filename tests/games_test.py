from scripts.games import games, retrieve_game_id

def test_games_success():
    response = games()
    assert response["success"] == True

def test_games_id_content_exists():
    response = games()
    id = response["data"][0]["id"]
    assert id is not None
    response = retrieve_game_id(id)
    print(response)
    #TODO fix game id