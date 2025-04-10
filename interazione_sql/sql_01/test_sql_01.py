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
    esito = elenco_persone_repo()
    if esito is None:
        print("Errore di connessione con il database")
    else:
        if len(esito) == 0:
            print("Nessuna persona trovata nel database")
        else:
            for persona in esito:
                print(persona)


# funzione per testare aggiornamento dati
def test_aggiornamento():
    test_elenco_persone()
    id_persona_da_modificare = int(input("Inserisci l'id della persona da modificare >>> "))
    persona = dati_persona_repo(id_persona_da_modificare) # Persona / str / None
    if persona and isinstance(persona, Persona):
        print(f"Le attuali specifiche sono: {persona}")
        persona.nome = input("Inserisci il nuovo Nome >>> ").lower().capitalize()
        persona.cognome = input("Inserisci il nuovo Cognome >>> ").lower().capitalize()
        persona.eta = int(input("Inserisci la nuova Età >>> "))
        print(aggiornamento_persona_repo(persona))
    else:  # Caso di errore o `None`
        print("Errore di connessione con il database o persona non trovata.")

# funzione per testare eliminazione
def test_eliminazione():
    test_elenco_persone()
    id_persona_da_eliminare = int(input("Inserisci l'id della persona da eliminare >>> "))
    esito = eliminazione_persona_repo(id_persona_da_eliminare)
    if esito:
        print(f"Eliminazione avvenuta con successo, {esito} righe eliminate.")
    else:
        print("Errore di connessione con il database o persona non trovata.")

# funzione per testare ricerca per caratteri cognome
def test_ricerca_cognome():
    sequenza_caratteri = input("Inserisci caratteri per la ricerca >>> ").lower().capitalize()
    esito = elenco_persone_like_cognome_repo(sequenza_caratteri)
    if esito is not None:
        for persona in esito:
            print(persona)


# invocazione funzioni
# test_registrazione()
# test_dati_persona()
# test_elenco_persone()
# test_aggiornamento()
# test_eliminazione()
test_ricerca_cognome()