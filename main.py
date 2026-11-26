from database.database_setup import create_tables


def main() -> None:

    create_tables()

    print("Database creato correttamente!")


if __name__ == "__main__":
    main()

#spiegazione
# Questo file contiene il punto di ingresso principale dell'applicazione.
# La funzione main chiama create_tables per creare le tabelle del database se non esistono già.
# Dopo aver creato le tabelle, stampa un messaggio di conferma.
# La funzione main viene eseguita solo se il file viene eseguito direttamente, non se importato come modulo.
# prima avevo messo un print all'inizio del main per indicare l'avvio del programma, ma l'ho rimosso per semplificare il flusso.