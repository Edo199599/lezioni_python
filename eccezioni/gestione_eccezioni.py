# def divisione(a,b):
#     print(int(a) / int(b))

# versione 2
def divisione(a, b):
    try:
        print(int(a) / int(b))
    except ValueError as v: # non genera più errore ma assegna l'errore ad una variabile v e la stampa
        print(v)
    except ZeroDivisionError as z:
        print(z)

# versione 3 (multi except - non risparmia molte righe rispetto al precedente - POCO UTILE)
def divisione_due(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e: # assegno l'errore che può spuntare alla stessa variabile
        # print(e) # se voglio comunque operare in maniera diversa per tipo di errore devo comunque distinguerli
        print("Valori non corretti") if isinstance(e, ValueError) else print ("Divisione per 0 impossibile")
        # isinstance: se e è istanza di ValueError printa la prima, altrimenti la seconda

def divisione_tre(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Valori non corretti") if isinstance(e, ValueError) else print ("Divisione per 0 impossibile")
    finally:
        print("Questa istruzione viene eseguita comunque")
    #print("Anche questa e ha lo stesso identico funzione") finally è abbastanza inutile potendo mettere un print fuori


def divisione_quattro(a, b):
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Valori non corretti") if isinstance(e, ValueError) else print ("Divisione per 0 impossibile")
    else: # funziona solo se il try è andato e non si è passati per l'except
        print("Tutto è andato per il meglio")
    finally: # sempre ramo finale
        print("Questa istruzione viene eseguita comunque")


# invocazioni funzioni
print("Avvio Programma")

divisione("5", "2")

divisione("5", "ciao")

divisione("5", "0") # nonostante il try/except comunque da errore per divisione per 0
# non era un ValueError ma un ZeroDivisionError che quindi non è sttao intercettato
# aggiungo un altro except
# tutti gli errori posso identificarli con la loro tipologia o con Execption che fa capo a tutte le tipologie di errore
# se voglio differenziare le cose per tipo di errore devo distinguere i problemi


divisione_tre("5", "2") # esegue il finally anche se il try è andato bene
divisione_tre("5", "ciao")
divisione_tre("3", "0")


divisione_quattro("5", "2")
divisione_quattro("5", "ciao") # non viene stampato l'else perchè il try non è andato

print("Fine Programma")