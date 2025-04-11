from rubrica_repository import *

# funzione per testare l'aggiunta di un contatto
def aggiunta_contatto():
    nome = input("Inserisci il nome del contatto da aggiungere in rubrica >>> ").lower().capitalize()
    cognome = input("Inserisci il cognome del contatto da aggiungere in rubrica >>> ").lower().capitalize()
    telefono = input("Inserisci il numero di telefono del contatto da aggiungere in rubrica >>> ")
    mail = input("Inserisci la mail del contatto da aggiungere in rubrica >>> ").lower()
    via = input("Inserisci la via del contatto da aggiungere in rubrica >>> ").lower().capitalize()
    civico = input("Inserisci il numero civico del contatto da aggiungere in rubrica >>> ")
    cap = input("Inserisci il CAP del contatto da aggiungere in rubrica >>> ")
    comune = input("Inserisci il comune del contatto da aggiungere in rubrica >>> ").lower().capitalize()
    provincia = input("Inserisci la provincia del contatto da aggiungere in rubrica >>> ").upper()
    indirizzo = Indirizzo(via=via, civico=civico, cap=cap, comune=comune, provincia=provincia)
    contatto = Contatto(nome=nome, cognome=cognome, telefono=telefono, mail=mail, indirizzo=indirizzo)
    return contatto

def stampa_contatti():
    contatti = elenco_contatti_rubrica_repo()
    if contatti is None:
        print("Errore di connessione con il database")
    else:
        if len(contatti) == 0:
            print("Nessun contatto trovato nella rubrica")
        else:
            for contatto in contatti:
                print(contatto)


def menu():
    while True:
        scelta_utente = input("******** RUBRICA ********\n"
                              "Digita 1 per visualizza rubrica\n"
                              "Digita 2 per aggiungere un nuovo contatto\n"
                              "Digita 0 per uscire\n"
                              ">>> ")
        match scelta_utente:
            case "1":
                stampa_contatti()
                print()
            case "2":
                contatto = aggiunta_contatto()
                esito = aggiunta_contatto_rubrica_repo(contatto)
                if esito:
                    print("Contatto aggiunto con successo")
                else:
                    print("Errore durante l'aggiunta del contatto")
            case "0":
                print("Uscita...")
                break
            case _:
                print("Scelta non valida")

menu()

