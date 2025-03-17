import csv

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
            for riga in contenuto:
                print(riga, type(riga))
    except Exception as e:
        print(e)


