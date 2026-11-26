
from database.database_setup import create_tables
from menus.main_menu import show_main_menu
from services.auth_service import (
    register_user,
    login_user
)
from services.character_service import (
    create_new_character,
    show_all_characters,
    update_character,
    remove_character,
    find_character
)


def main() -> None:

    create_tables()

    while True:

        show_main_menu()
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

        elif scelta == "3":

            name = input("Nome Personaggio: ")
            character_class = input("Classe: ")

            try:
                level = int(input("Livello: "))
            except ValueError:
                print("Inserisci un numero valido")
                continue

            create_new_character(
                name=name,
                character_class=character_class,
                level=level,
                user_id=1
            )

            print("Personaggio creato!")

        elif scelta == "4":

           show_all_characters()

        elif scelta == "5":

            try:
                character_id = int(
                    input("ID Personaggio: ")
                )
            except ValueError:
                print("Inserisci un ID valido")
                continue

            try:
                level = int(
                    input("Nuovo Livello: ")
                )
            except ValueError:
                print("Inserisci un numero valido")
                continue

            update_character(
                character_id,
                level
            )

            print("Personaggio aggiornato!")

        elif scelta == "6":

            try:
                character_id = int(
                    input("ID Personaggio: ")
                )
            except ValueError:
                print("Inserisci un ID valido")
                continue

            remove_character(
                character_id
            )

            print("Personaggio eliminato!")
        
        elif scelta == "7":

            name = input(
                "Nome da cercare: "
            )

            find_character(name)
 
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
# con try e except gestiamo gli input non validi dell'utente, come ID o livello non numerici.
# Se l'utente inserisce un valore non valido, viene mostrato un messaggio di errore e 
# il ciclo continua senza interrompere l'applicazione.