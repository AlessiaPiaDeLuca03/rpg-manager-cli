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


def get_all_characters():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM characters
    """)

    characters = cursor.fetchall()

    connection.close()

    return characters

def update_character_level(
    character_id: int,
    level: int
) -> None:

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    UPDATE characters
    SET level = ?
    WHERE id = ?
    """, (
        level,
        character_id
    ))

    connection.commit()
    connection.close()

def delete_character(
    character_id: int
) -> None:

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM characters
    WHERE id = ?
    """, (character_id,))

    connection.commit()
    connection.close()


def search_character(
    name: str
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM characters
    WHERE name LIKE ?
    """, (f"%{name}%",))

    characters = cursor.fetchall()

    connection.close()

    return characters

def update_character_level(
    character_id: int,
    level: int
) -> None:

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    UPDATE characters
    SET level = ?
    WHERE id = ?
    """, (
        level,
        character_id
    ))

    connection.commit()
    connection.close()


def delete_character(
    character_id: int
) -> None:

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM characters
    WHERE id = ?
    """, (character_id,))

    connection.commit()
    connection.close()


def search_character(
    name: str
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM characters
    WHERE name LIKE ?
    """, (f"%{name}%",))

    characters = cursor.fetchall()

    connection.close()

    return characters
