import scripts.characters

def test_retrieve_characters_name_success():
    response = scripts.characters.retrieve_characters_name("Zelda")
    assert response["success"] == True

def test_retrieve_characters_name_empty():
    response = scripts.characters.retrieve_characters_name("RUMBLEYAM")
    assert response["count"] == 0

def test_retrieve_characters():
    response = scripts.characters.characters()
    assert response["success"] == True
