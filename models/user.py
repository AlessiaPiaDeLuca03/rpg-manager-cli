"""
Modello utente.
"""


class User:
    """
    Rappresenta un utente del sistema.
    """

    def __init__(
        self,
        username: str,
        email: str,
        password_hash: str,
        role_id: int
    ) -> None:

        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role_id = role_id

    #spiegazione
    # La classe User rappresenta un utente del sistema.
    # Il costruttore (__init__) accetta i seguenti parametri:
    # - username: il nome utente dell'utente
    # - email: l'email dell'utente
    # - password_hash: l'hash della password dell'utente
    # - role_id: l'id del ruolo dell'utente (collegato alla tabella roles)
    # Questi valori vengono memorizzati come attributi dell'istanza.