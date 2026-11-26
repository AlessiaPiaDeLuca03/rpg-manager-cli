"""
Servizi per la gestione dei personaggi.
"""

from models.character import Character
from repositories.character_repository import create_character


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