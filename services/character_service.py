"""
Servizi per la gestione dei personaggi.
"""

from models.character import Character

from repositories.character_repository import (
    create_character,
    get_all_characters,
    update_character_level,
    delete_character,
    search_character
)


def create_new_character(
    name: str,
    character_class: str,
    level: int,
    user_id: int
) -> None:

    character = Character(
        name=name,
        character_class=character_class,
        level=level,
        user_id=user_id
    )

    create_character(character)


def show_all_characters():

    characters = get_all_characters()

    if not characters:
        print("Nessun personaggio trovato.")
        return

    for character in characters:

        print(
            f"ID: {character[0]} | "
            f"Nome: {character[1]} | "
            f"Classe: {character[2]} | "
            f"Livello: {character[3]}"
        )

def update_character(
    character_id: int,
    level: int
):

    update_character_level(
        character_id,
        level
    )

def remove_character(
    character_id: int
):

    delete_character(
        character_id
    )

def find_character(
    name: str
):

    characters = search_character(name)

    for character in characters:

        print(
            f"ID: {character[0]} | "
            f"Nome: {character[1]} | "
            f"Classe: {character[2]} | "
            f"Livello: {character[3]}"
        )