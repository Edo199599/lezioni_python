from interfacce_grafiche_utente.rubrica.model.contatto import Contatto
import json

# funzione per leggere i dati dal file e ottenere una lista di oggetti Contatto
def elenco_contatti_repo():
    try:
        with open("rubrica.json") as file:
            dati_recuperati = json.load(file) # per recuperare tutti i dati in un unico oggetto
            # print(dati_recuperati, type(dati_recuperati))
            lista_contatti = [Contatto.deserializzazione(dizionario) for dizionario in dati_recuperati]
            # otteniamo così una lista di oggetti Contatto
            return lista_contatti
    except Exception as e:
        print(e)
        return None

