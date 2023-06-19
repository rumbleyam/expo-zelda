import scripts.monsters

def test_retrieve_monsters_name_success():
    response = scripts.monsters.retrieve_monsters_name("Zelda")
    assert response["success"] == True

def test_retrieve_monsters_name_empty():
    response = scripts.monsters.retrieve_monsters_name("RUMBLEYAM")
    assert response["count"] == 0

def test_retrieve_monsters():
    response = scripts.monsters.monsters()
    assert response["success"] == True
