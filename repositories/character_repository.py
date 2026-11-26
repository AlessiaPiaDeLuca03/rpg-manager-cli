"""
Repository personaggi.
"""

from database.db_connection import get_connection
from models.character import Character


def create_character(character: Character) -> None:

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO characters
    (name, character_class, level, user_id)
    VALUES (?, ?, ?, ?)
    """, (
        character.name,
        character.character_class,
        character.level,
        character.user_id
    ))

    connection.commit()
    connection.close()