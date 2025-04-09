from PIL.ImageOps import expand

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

# funzione per scrivere l'intera lista contatti nel file json
def _riscrittura_file(lista_contatti):
    try:
        with open("rubrica.json", "w") as file: # w perché tanto voglio riscrivere tutto
            lista_contatti = [contatto.serializzazione() for contatto in lista_contatti]
            json.dump(lista_contatti, file, indent=4)
            # dump serve per scrivere su file
            # file è il file su cui voglio scrivere
            # indent serve per formattare il file json. 4 è il numero di spazi da usare per indentare
            return True
    except Exception as e:
        print(e)
        return False

# funzione per eliminare un contatto dal file json
def eliminazione_contatto_repo(contatto):
    lista_contatti = elenco_contatti_repo() # ottengo la lista di contatti
    if contatto in lista_contatti:
        lista_contatti.remove(contatto)
        return _riscrittura_file(lista_contatti)

# funzione per aggiungere un contatto al file json
def aggiunta_contatto_repo(contatto):
    lista_contatti = elenco_contatti_repo() # ottengo la lista di contatti
    lista_contatti.append(contatto)
    return _riscrittura_file(lista_contatti)