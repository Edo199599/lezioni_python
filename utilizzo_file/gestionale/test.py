# script eseguibile
from repository.prodotto_repository import *
# l'asterisco significa "all" importa tutto

# funzione per la stampa del magazzino
def stampa_magazzino():
    magazzino = elenco_prodotti()
    # lista di oggetti di tipo prodotto, vuota nel caso non abbia recuperato nulla, None se ha avuto problemi in lettura la funzione
    if magazzino is not None:
        if len(magazzino) > 0:
            print("--------- Magazzino ----------")
            for prodotto in magazzino:
                print(prodotto)
        else:
            print("Nessun prodotto attualmente registrato")
    else:
        print("Problemi con il file di archiviazione")

# funzione per l'aggiunta di un nuovo prodotto
def aggiunta_prodotto():
    print("---- Aggiunta Prodotto ----")
    tipologia = input("Inserire tipologia >>> ").strip().replace(",","") # la virgola è l'unico carattere che potrebbe dare problemi
    marca = input("Inserire marca >>> ").strip().replace(",","") # essendo la virgola la separazione nei database csv tra le caratteristiche oggetto
    modello = input("Inserire modello >>> ").strip().replace(",","")
    try:
        prezzo = float(input("Inserire prezzo >>> ").strip().replace(",","."))
        prodotto = Prodotto(tipologia=tipologia, marca=marca, modello=modello, prezzo=prezzo)
        print(registrazione_prodotto(prodotto)) # oltre a triggerare la funzione stampa uno dei return per capire l'esito
    except ValueError as v:
        print("Il prezzo inserito non è valido")
        pannello_comandi()


# funzione per la cancellazione di un prodotto
def cancellazione_prodotto():
    magazzino = elenco_prodotti()
    if magazzino is None:
        print("Problemi con il file di archiviazione")
    elif len(magazzino) == 0:
        print("Nessun prodotto è attualmente registrato")
    else:
        print("----- Cancellazione Prodotto -----")
        for prodotto in magazzino:
            print(prodotto)
        try:
            id_prodotto = int(input("Inserire id prodotto da eliminare >>> ").strip())
            prodotto_da_eliminare = list(filter(lambda p: p.id == id_prodotto, magazzino))[0]
            # non vogliamo che prodotto_da_el sia una lista quindi segnamo alla fine il [0] per dare l'unico elemento della lista
            magazzino.remove(prodotto_da_eliminare)
            print(eliminazione_prodotto(magazzino))
        except Exception as e:
            print("Input errato o Prodotto non trovato")
            pannello_comandi()


# funzione di avvio e gestione dell'applicazione
def pannello_comandi():
    match input("******** GESTIONALE MAGAZZINO ********\n"
                "Digita 1 per stampa magazzino\n"
                "Digita 2 per aggiungere un prodotto\n"
                "Digita 3 per eliminare un prodotto\n"
                "Digita 0 per terminare\n"
                ">>> "):
        case "1":
            stampa_magazzino()
            pannello_comandi()
        case "2":
            aggiunta_prodotto()
            pannello_comandi()
        case "3":
            cancellazione_prodotto()
            pannello_comandi()
        case _:
            exit(0)


# invocazione funzione di avvio
pannello_comandi()