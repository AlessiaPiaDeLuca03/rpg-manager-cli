
RPG Character Manager ^-^

Descrizione:

RPG Character Manager è un'applicazione sviluppata in Python che permette la gestione di utenti
 e personaggi RPG tramite un database SQLite. Il programma include registrazione e login con 
 password protette tramite hashing usando Werkzeug, gestione dei ruoli, CRUD completo dei 
 personaggi (creazione, visualizzazione, modifica ed eliminazione) e funzionalità di ricerca. 
 Il progetto utilizza Git e GitHub ed è organizzato secondo una struttura modulare con 
 cartelle dedicate a modelli, servizi, repository e database.

 
------------------------------------------------------------------------------------------------
Tecnologie Utilizzate ^-^

Python 3,
SQLite,
Git,
GitHub,
Werkzeug,
Pathlib.
------------------------------------------------------------------------------------------------
Struttura del Progetto ^-^

database/
models/
repositories/
services/
validators/
menus/
------------------------------------------------------------------------------------------------
Gestione Utenti ^-^

Funzionalità implementate:

Registrazione utenti,
Login utenti,
Password hashate,
Email univoca,
Ruoli.

Ruoli disponibili:
admin,
user,
moderator,
game_master,
vip.
------------------------------------------------------------------------------------------------
Gestione Personaggi ^-^
Funzionalità CRUD complete.

Create:
Creazione personaggio.

Read:
Visualizzazione personaggi.

Update:
Modifica del livello del personaggio.

Delete:
Eliminazione personaggio.

Search:
Ricerca personaggio tramite nome.
------------------------------------------------------------------------------------------------
Sicurezza ^-^
Le password non vengono salvate in chiaro.
Per l'hashing vengono utilizzate le funzioni:

generate_password_hash()
e
check_password_hash()
fornite dal pacchetto Werkzeug.
------------------------------------------------------------------------------------------------

Database ^-^
Il database viene gestito tramite SQLite.
Tabelle implementate:

roles,
users,
characters.(![alt text](image-3.png))
------------------------------------------------------------------------------------------------
Installazione ^-^

Creazione ambiente virtuale:
python -m venv venv

Attivazione:
venv\Scripts\activate

Installazione dipendenze:
pip install -r requirements.txt

Avvio del progetto:
python main.py
------------------------------------------------------------------------------------------------
Funzionalità Future ^-^
Gestione amministratore dedicata.
Gestione gilde.
Gestione inventario.
Eventi RPG.
------------------------------------------------------------------------------------------------
Validators:
validators/
Contiene le funzioni di validazione degli input.


Autore:
Alessia P. De Luca 








