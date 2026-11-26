from database.database_setup import create_tables
from services.auth_service import (
    register_user,
    login_user
)


def main() -> None:

    create_tables()

    while True:

        print("\n===== RPG MANAGER =====")
        print("1. Registrazione")
        print("2. Login")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":

            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")

            register_user(
                username=username,
                email=email,
                password=password
            )

            print("Utente registrato!")

        elif scelta == "2":

            email = input("Email: ")
            password = input("Password: ")

            if login_user(email, password):
                print("Login effettuato!")
            else:
                print("Email o password errati!")

        elif scelta == "0":

            print("Arrivederci!")
            break

        else:

            print("Scelta non valida")


if __name__ == "__main__":
    main()

#spiegazione
# Questo file contiene il punto di ingresso principale dell'applicazione.
# La funzione main chiama create_tables per creare le tabelle del database se non esistono già.
# Dopo aver creato le tabelle, stampa un messaggio di conferma.
# La funzione main viene eseguita solo se il file viene eseguito direttamente, non se importato come modulo.
# prima avevo messo un print all'inizio del main per indicare l'avvio del programma, ma l'ho rimosso per semplificare il flusso.
# Ora il flusso è più lineare: crea le tabelle, chiede i dati dell'utente e registra l'utente senza messaggi iniziali superflui.
# La funzione main gestisce il flusso principale dell'applicazione.
# Mostra un menu con le opzioni di registrazione, login e uscita.
# In base alla scelta dell'utente, esegue le azioni corrispondenti.
# Il ciclo continua fino a quando l'utente sceglie di uscire.
# Le azioni di registrazione e login sono attualmente solo dei placeholder e devono essere implementate.