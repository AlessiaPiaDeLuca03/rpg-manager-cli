"""
Creazione tabelle del database.
"""

from database.db_connection import get_connection


def create_tables() -> None:

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role_id INTEGER NOT NULL,
        FOREIGN KEY(role_id) REFERENCES roles(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS characters(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        character_class TEXT NOT NULL,
        level INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    connection.commit()
    connection.close()

    #spiegazione
    # Ho creato una funzione create_tables che si occupa di creare le tabelle del database se non esistono già.
    # Le tabelle create sono:
    # - roles: contiene i ruoli degli utenti (id e name)
    # - users: contiene gli utenti (id, username, email, password_hash, role_id) con una chiave esterna verso roles
    # - characters: contiene i personaggi (id, name, character_class, level, user_id) con una chiave esterna verso users
    # Alla fine, la connessione al database viene chiusa dopo aver eseguito i commit delle modifiche.