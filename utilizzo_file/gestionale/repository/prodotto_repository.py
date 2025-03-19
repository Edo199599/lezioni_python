import csv

from utilizzo_file.gestionale.model.prodotto import Prodotto

# importa funzionalità specifiche per l'elaborazione di file .csv come il nostro magazzino

# costante riservata per riferimento al file di archiviazione
# ovvero attributi e modelli che non verranno usate al di fuori del loro file
_FILE_PATH = "magazzino.csv" # convenzione: tutte maiuscole con _ iniziale e _ in mezzo ad ogni parola
# per registrare funzioni di lettura/scrittura/elaborazione/etc...
# assegno il file magazzino alla costante per poterlo poi richiamare senza rischiare di sbagliare

# funzione per leggere il contenuto del file ottendendo una lista di oggetti Prodotto
def elenco_prodotti():
    try:
        with open(_FILE_PATH) as file: # non metto la r essendo di default per evitare di rischiare un errore # nel farlo
            contenuto = csv.reader(file) # ritorna una struttura iterabile (che possiamo scorrere)
            next(contenuto) # così che venga skippata solo la prima riga ad ogni invocazione (elimina l'intestazione)
            prodotti = []
            for riga in contenuto:
                #print(riga, type(riga))
                prodotto = Prodotto()
                prodotto.id = int(riga[0]) # asse
                prodotto.tipologia = riga[1]
                prodotto.marca = riga[2]
                prodotto.modello = riga[3]
                prodotto.prezzo = float(riga[4])
                prodotti.append(prodotto)
            return prodotti
    except Exception as e:
        print(e)
        return None


# funzione ausiliaria per generare id progressivo in fare di registrazione prodotto
def _generatore_id(): # convenzione per definire le funzioni private quindi limitate al contesto in cui sono definite
    prodotti = elenco_prodotti()
    if prodotti is None:
        return None # se il file è illeggibile continuamo a dare None
    if len(prodotti) == 0:
        return 1
    return max(list(map(lambda prodotto: prodotto.id, prodotti))) + 1
    # rimappiamo una lista di oggetti di tipo Prodotto in una lista dei soli id di quei prodotti, prendi di quella il max e aggiungi 1


# funzione per registrare un nuovo prodotto nel file
def registrazione_prodotto(prodotto):
    id_nuovo_prodotto = _generatore_id()
    if id_nuovo_prodotto is None:
        return "Problemi con il file di archiviazione"
        # non riusciamo a leggere, non abbiamo scritto id e ora non riusciamo ad archiviare
    try:
        with open(_FILE_PATH, "a", newline="") as file: # newline per evitare che si crei una riga con solo \n di default ad ogni aggiunta
            writer = csv.writer(file)   #passiamo alla variabile writer il file su cui dobbiamo scrivere
            writer.writerow([id_nuovo_prodotto, prodotto.tipologia, prodotto.marca, prodotto.modello, prodotto.prezzo])
            return "Prodotto registrato correttamente"
    except Exception as e:
        print(e)
        return "Registrazione impossibile"


# funzione per eliminare un prodotto dal file (non esiste per i file la cancellazione e modifica selettiva di una riga)
def eliminazione_prodotto(magazzino): # la lista magazzino è già senza prodotto eliminato
    try:
        with open(_FILE_PATH, "w", newline="") as file: # va bene qua la riscrittura tanto vogliamo eseguire proprio questa operazione
            writer = csv.writer(file)
            writer.writerow(["ID", "Tipologia", "Marca", "Modello", "Prezzo"]) # ricreiamo la riga di intestazione con row e ricopiamo poi con rows.
            writer.writerows([prodotto.to_list() for prodotto in magazzino])
            return "Prodotto Eliminato"
    except Exception as e:
        print(e)
        return "Eliminazione impossibile"