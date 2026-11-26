from database.database_setup import create_tables
from services.auth_service import register_user


def main() -> None:

    create_tables()

    username = input("Username: ")

    email = input("Email: ")

    password = input("Password: ")

    register_user(
        username=username,
        email=email,
        password=password
    )

    print("Utente registrato correttamente!")


if __name__ == "__main__":
    main()

#spiegazione
# Questo file contiene il punto di ingresso principale dell'applicazione.
# La funzione main chiama create_tables per creare le tabelle del database se non esistono già.
# Dopo aver creato le tabelle, stampa un messaggio di conferma.
# La funzione main viene eseguita solo se il file viene eseguito direttamente, non se importato come modulo.
# prima avevo messo un print all'inizio del main per indicare l'avvio del programma, ma l'ho rimosso per semplificare il flusso.
# Ora il flusso è più lineare: crea le tabelle, chiede i dati dell'utente e registra l'utente senza messaggi iniziali superflui.