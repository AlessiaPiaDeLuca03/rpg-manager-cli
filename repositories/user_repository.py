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

def get_user_by_email(email: str):
    """
    Recupera un utente dal database in base all'email.
    """
    #spiegazione
    # La funzione get_user_by_email accetta un'email come parametro.
    # Si connette al database, crea un cursore e esegue una query per recuperare l'utente con l'email specificata.
    # Restituisce l'utente trovato o None se non esiste.
    # La connessione al database viene chiusa dopo aver eseguito la query.

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    connection.close()

    return user

    connection.commit()
    connection.close()

    #spiegazione
    # La funzione create_user accetta un oggetto User come parametro.
    # Si connette al database, crea un cursore e inserisce i dati dell'utente nella tabella users.
    # Dopo l'inserimento, esegue il commit delle modifiche e chiude la connessione al database.
    # La funzione non restituisce alcun valore.