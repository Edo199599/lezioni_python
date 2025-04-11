from model.contatto import Contatto
from model.indirizzo import Indirizzo
from exceptions.validation_exception import ValidationException
from repository.contatto_repository import ContattoRepository

class Eseguibile:

    # injection del componente di repository e chiamata a metodo di gestione menu
    def __init__(self):
        self.contatto_repository = ContattoRepository()
        self.pannello_comandi()

    # metodo di gestione menu
    def pannello_comandi(self):
        match input("***** APPLICAZIONE RUBRICA *****\n1 - Nuovo Contatto\n2 - Elenco Contatti\n0 - Esci >>> "):
            case "1":
                self.registrazione_contatto()
                self.pannello_comandi()
            case "2":
                self.elenco_contatti()
                self.pannello_comandi()
            case _:
                exit(0)

    # metodo di registrazione contatto
    def registrazione_contatto(self):
        print("***** REGISTRAZIONE CONTATTO *****")
        try:
            input_utente = []
            for campo in Contatto.schema_validazione.keys():
                valore = input(f"Digita {campo} Contatto >>> ").strip()
                Contatto.validazione(valore, campo)
                input_utente.append(valore)
            indirizzo = Indirizzo(via=input_utente[4], civico=input_utente[5], cap=input_utente[6],
                                  comune=input_utente[7], provincia=input_utente[8])
            contatto = Contatto(nome=input_utente[0], cognome=input_utente[1], telefono=input_utente[2],
                                mail=input_utente[3], indirizzo=indirizzo)
            print(self.contatto_repository.registrazione_contatto_repo(contatto))
        except ValidationException as e:
            print(e)
            self.pannello_comandi()

    # metodo di stampa elenco contatti
    def elenco_contatti(self):
        print("***** ELENCO CONTATTI *****")
        contatti = self.contatto_repository.elenco_contatti_repo()
        if isinstance(contatti, str):
            print(contatti)
        elif len(contatti) == 0:
            print("Nessun Contatto Registrato")
        else:
            for contatto in contatti:
                print(contatto, "------------------------------------------------", sep="\n")

# avvio programma
Eseguibile()