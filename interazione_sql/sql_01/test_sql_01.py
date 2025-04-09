from persona_repository import *
from persona import Persona


# funzione per testare la registrazione
def test_registrazione():
    nome = input("Inserisci il nome >>> ").lower().capitalize()
    cognome = input("Inserisci il cognome >>> ").lower().capitalize()
    eta = int(input("Inserisci l'età >>> "))
    persona = Persona(nome=nome, cognome=cognome, eta=eta)
    # se passassi solo Persona(nome,cognome,eta) non funzionerebbe perchè il costruttore di Persona prevede id
    print(registrazione_persona_repo(persona))

# funzione per testare il recupero dei dati singoli
def test_dati_persona():
    id_persona = int(input("Inserisci l'id della persona di cui vuoi recuperare i dati >>> "))
    esito = dati_persona_repo(id_persona) # Persona / str / None
    if esito:
        print(esito)
    else:
        print("Errore di connessione con il database")

# funzione per testare il recupero di tutte le persone
def test_elenco_persone():
    elenco = elenco_persone_repo()


# invocazione funzioni
# test_registrazione()
# test_dati_persona()
test_elenco_persone()
