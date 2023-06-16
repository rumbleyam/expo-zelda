import scripts.characters

def test_retrieve_characters_name_success():
    response = scripts.characters.retrieve_characters_name("Zelda")
    print(response)
    assert response["success"] == True

def test_retrieve_characters_name_empty():
    response = scripts.characters.retrieve_characters_name("RUMBLEYAM")
    print(response)
    assert response["count"] == 0
