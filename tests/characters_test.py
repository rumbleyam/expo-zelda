import scripts.characters


def retrieve_characters_name_success():
    response = scripts.characters.retrieve_characters_name("Zelda")
    assert response.success == "True"

def retrieve_characters_name_failure():
    response = scripts.characters.retrieve_characters_name("RUMBLEYAM")
    assert response.success == "False"
