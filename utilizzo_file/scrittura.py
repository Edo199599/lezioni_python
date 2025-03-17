
# funzione per scrivere testo su un file che verrà creato
def scrivi_su_file(testo):
    file = None # la dichiaro fuori per far si che sia accedibile in tutta la struttura try except e finally
    try:
        file = open("file.txt", "w") # apertura stream di dati in modalità write
        file.write(testo)
    except Exception as e:
        print(e)
    finally:
        if file:
            file.close() # non è obbligatorio ma si consiglia la chiusura dello stream


# invocazione delle funzioni
scrivi_su_file("1^a riga di testo") # la modalità di apertura dello stream con la w è di sovrascrittura
scrivi_su_file("2^a riga di testo") # non aggiunge quindi la riga ma sovrascrive tutto il file perdendo lo storico


# funzione per aggiungere testo a un file che verrà creato (se eiste il testo si aggiunge in coda al precedente senza sovrascrivere)
def aggiungi_a_file(testo):
    file = None # la dichiaro fuori per far si che sia accedibile in tutta la struttura try except e finally
    try:
        file = open("file2.txt", "a") # apertura stream di dati in modalità append
        file.write(testo)
    except Exception as e:
        print(e)
    finally:
        if file:
            file.close()

# invocazine delle funzioni
aggiungi_a_file("1^a riga di testo\n") # la modalità di apertura dello stream con la a aggiunge in coda
aggiungi_a_file("2^a riga di testo")



# funzione per scrivere testo su un file con gestione automatica della chiusura
def scrivi_e_chiudi(testo):
    try: # al posto di open che va assegnato ad una variabile e che richiede chiusura uso:
        with open("file3.txt", "x") as file: # apertura stream (x = modalità protetta)
        # per tutti quegli elementi che richiedono chiusura al termine delle operazioni
        # as file è l'assegnazione più veloce del with ad una variabile file
            file.write(testo)
    except Exception as e:
        print(e)

# invocazione funzioni
scrivi_e_chiudi("1^a riga di testo") # la x come modalità di scrittura permette di scrivere una volta sola ad un file da creare
# la x si utilizza in casi abbastanza rari a dispetto di "a" e "w"
