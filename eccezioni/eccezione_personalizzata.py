# definizione classe di eccezione personalizzata
class MiaEccezione(Exception):

    # metodo di inizializzazione
    def __init__(self, messaggio="Eccezione Generica"): # passo anche già un messaggio di default
        self.messaggio = messaggio

    # metodo di rappresentazione testuale
    def __str__(self): # non uso il repr perché non accade mai che errori siano liste
        return self.messaggio

# acquisizione di imput utente
input_utente = input("Digita codice prodotto preceduto da PROD- >>> ")


# valutazione input utente
if input_utente.startswith("PROD-"):
    print("Prodotto registrato correttamente")
else:
    try:
        raise MiaEccezione("Il codice prodotto non è corretto") # genero errore con messaggio
# lanciare eccezioni per inchiodare il programma in casi di attacci potrebbe essere utile piuttosto che andare avabnti
    except MiaEccezione as m:
        print(m) # invece di dare un errore e bloccare il programma, intercetto l'errore e lo stampo senza crash