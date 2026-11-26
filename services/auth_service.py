"""
Servizio autenticazione.
"""

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models.user import User
from repositories.user_repository import create_user


def register_user(
    username: str,
    email: str,
    password: str
) -> None:
    """
    Registra un nuovo utente.
    """

    email = email.strip().lower()

    password_hash = generate_password_hash(password)

    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role_id=2
    )

    create_user(user)

from repositories.user_repository import get_user_by_email


def login_user(
    email: str,
    password: str
) -> bool:

    email = email.strip().lower()

    user = get_user_by_email(email)

    if user is None:
        return False

    return check_password_hash(
        user[3],
        password
    )

    create_user(user)

    #spiegazione
    # La funzione register_user accetta username, email e password come parametri.
    # Normalizza l'email rimuovendo spazi e convertendola in minuscolo.
    # Genera l'hash della password utilizzando generate_password_hash.
    # Crea un oggetto User con i dati forniti e il role_id impostato a 2 (utente standard).
    # Chiama la funzione create_user per inserire l'utente nel database.
    # La funzione non restituisce alcun valore.