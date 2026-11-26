"""
Repository utenti.
"""

from database.db_connection import get_connection
from models.user import User


def create_user(user: User) -> None:
    """
    Inserisce un utente nel database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO users
    (username, email, password_hash, role_id)
    VALUES (?, ?, ?, ?)
    """, (
        user.username,
        user.email,
        user.password_hash,
        user.role_id
    ))

    connection.commit()
    connection.close()

    #spiegazione
    # La funzione create_user accetta un oggetto User come parametro.
    # Si connette al database, crea un cursore e inserisce i dati dell'utente nella tabella users.
    # Dopo l'inserimento, esegue il commit delle modifiche e chiude la connessione al database.
    # La funzione non restituisce alcun valore.