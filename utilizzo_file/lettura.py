
# funzione per leggere il contenuto di un file e ritornarlo come stringa
def leggi_file():
    try:
        with open("file2.txt", "r+") as file: # apro il file come read ma sono io che poi do la sequenza di scrittura/lettura
            contenuto = file.read() # legge carattere per carattere. Anche i \n
            print(type(contenuto))
            return contenuto
    except Exception as e:
        print(e)


# invocazione funzioni
print(leggi_file())

# funzione per leggere il contenuto di un file e ritornarlo come lista
def leggi_file_due():
    try:
        with open("file2.txt") as file: # posso non dare la r essendo il valore di default di open "r"
            contenuto = file.readlines() # per i file che sappiamo avere strutture su varie righe con ognuna un elemento ben preciso
            print(type(contenuto))
            return contenuto # qui non considera il \n e te lo scrive in stampa nella lista
    except Exception as e:
        print(e)


print(leggi_file_due())
