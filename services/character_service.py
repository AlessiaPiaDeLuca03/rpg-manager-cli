"""
Servizi per la gestione dei personaggi.
"""

from models.character import Character

from repositories.character_repository import (
    create_character,
    get_all_characters
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