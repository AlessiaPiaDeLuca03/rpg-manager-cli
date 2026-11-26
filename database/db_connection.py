"""
Gestione connessione database SQLite.
"""

import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent  # Directory principale del progetto, parent serve per risalire alla cartella principale dal file corrente

DATABASE_PATH = BASE_DIR / "game.db"


def get_connection() -> sqlite3.Connection:
    """
    Restituisce una connessione al database.
    """

    return sqlite3.connect(DATABASE_PATH)

#spiegazione totale
# Questo file gestisce la connessione al database SQLite.
# Viene definita la costante BASE_DIR che rappresenta la directory principale del progetto.
# DATABASE_PATH contiene il percorso completo del file del database "game.db".
# La funzione get_connection restituisce una connessione al database utilizzando sqlite3.connect con il percorso DATABASE_PATH.
