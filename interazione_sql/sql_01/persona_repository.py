import pymysql

from interazione_sql.sql_01.persona import Persona


# Ogni volta che l'app deve interagire con il DB, deve aprire una connessione
# aprire una connessione richiede:
# Localizzazione del ServerMySQL + Credenziali + Database di riferimento
# ip computer su cui gira il server, la porta a cui risponde il server, il nome del DB, username e password
# Al termine dell'interazione con il DB, la connessione deve essere chiusa

# per evitare di scrivere tutto ogni volta possiamo creare una funzione ausiliaria per ottenere la connessione al DB
# funzione ausiliaria
def _get_connection():
    return pymysql.connect(
        host = 'localhost', # potremmo anche inserire l'IP come "127.0.0.1"
        port = 3306,
        user = 'root', # standard user per MySQL
        password = '',
        database = 'sql_01' # nome del DB
    )

# funzione per registrare un nuovo oggetto Persona nel database
def registrazione_persona_repo(persona): # persona con dati recuperati in input da utente
    try:
        # apertura della connessione al DB
        with _get_connection() as connection: # alla fine del blocco with la connessione viene chiusa automaticamente
            # creazione del cursore per eseguire le query
            with connection.cursor() as cursor:
                sql = "INSERT INTO persone (nome, cognome, eta) VALUES (%s, %s, %s)"
                # le %s sono dei segnaposto per i valori che andremo a passare a cursor.execute
                valori = persona.nome, persona.cognome, persona.eta
                cursor.execute(sql, valori) # esecuzione della query
                # di default cursore.execute non fa il commit, quindi dobbiamo farlo noi
                connection.commit() # per inviare istruzione di manipolazione dati al DB
                return cursor.rowcount # conteggio righe interessate dalla query (dovrebbe qui ritornare 1 - 1 riga creata)
    except Exception as e:
        print("Errore durante la registrazione della persona:", e)
        return None

# funzione per ottenere un oggetto Persona dal DataBase (ricerca per id)
def dati_persona_repo(id):
    try:
        # apertura della connessione al DB
        with _get_connection() as connection:
            # creazione del cursore
            with connection.cursor() as cursor:
                sql = "SELECT * FROM persone WHERE id = %s"
                valori = id, # id è una tupla con un solo elemento
                cursor.execute(sql, valori)
                # recupero dei dati
                risultato = cursor.fetchone() # fetchone() recupera una sola riga
                # è una tupla con dati record in ordine colonne oppure None se non trova nulla
                if risultato:
                    return Persona(risultato[0], risultato[1], risultato[2], risultato[3])
                else:
                    return "Nessuna persona trovata con l'id fornito."
    except Exception as e:
        # le possibili exception sono problemi in scrittura di query, problemi di connessione, ecc.
        # print("Errore durante il recupero dei dati della persona:", e) post fase di produzione la commentiamo
        return None

# funzione per ottenere una lista di oggetti Persona dal DataBase (lettura generale)
def elenco_persone_repo():
    try:
        # apertura della connessione al DB
        with _get_connection() as connection:
            # creazione del cursore
            with connection.cursor() as cursor:
                sql = "SELECT * FROM persone"
                cursor.execute(sql)
                # recupero dei dati
                risultato = cursor.fetchall() # fetchall() recupera tutte le righe
                print(risultato)
    except Exception as e:
        print("Errore durante il recupero dei dati delle persone:", e)
        return None

