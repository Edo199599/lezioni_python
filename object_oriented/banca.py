"""
SIMULAZIONE SEMPLIFICATA BANCA
- Possibilità di aprire un conto corrente ricevendone IBAN (saldo 0)
- Possibilità di registrare versamenti e prelevamenti (Quanti ne vuole)
- Possibilità di terminare il programma in qualsiasi momento

SVILUPPO OBJECT ORIENTED -> Oggetto logico da gestire è ContoCorrente
                            . Intestatario (nome e cognome del cliente)
                            . Saldo
                            . Numero del conto (casuale)
                            . IBAN (parte fissa + numero del conto)
                            . Costruzione oggetto ContoCorrente ad apertura (__init__)
                            . Aggiornamento dinamico del saldo conto corrente
                            . Rappresentazione testuale oggetto
"""

import random

#definizione classe di modellazione oggetto logico ContoCorrente
class ContoCorrente:

    # attributo di classe con valore comune a tutti gli oggetti
    iban_fisso = "IT 07 K 02008 13000 "

    # metodo di inizializzazione
    def __init__(self, intestatario): # in input chiediamo solo il nome ma tutto il resto lo definiamo noi
        self.intestatario = intestatario
        self.saldo = 0 # inizializzato a zero
        self.numero_conto = "".join(str(random.randint(0, 9)) for _ in range(7))
        # crea una stringa e unisci (join) per 7 volte un numero random da 0 a 9 convertito a stringa
        self.iban = ContoCorrente.iban_fisso + self.numero_conto # iban fisso è variabile globale e la devo richiamare


    # metodo di istanza per aggiornamento del nostro saldoo
    def set_saldo(self, importo_operazione):
        #self.saldo += importo_operazione # commentato perchè metodo rischioso che chiederebbe molta validazione dati
        try: # costrutto per eseguire istruzioni da cui potrebbero nascere problemi
            importo_operazione = float(importo_operazione.strip().replace(",",".")) # se passa 100.89 ok, se passa ciao vado nell'Except
            self.saldo += importo_operazione
            return f"Hai registrato un'operazione {importo_operazione:.2f} ed ora hai un salto pari a {self.saldo:.2f}"
        except Exception as e:
            return "L'importo che hai inserito non è corretto"


    # metodo di istanza per rappresentazione testuale
    def __repr__(self):
        return (f"Benvenuto/a {self.intestatario}\nL'IBAN del tuo nuovo conto è {self.iban}\n"
        f"Attualmente il tuo saldo è pari a {self.saldo}€")


# SEZIONE OPERATIVA DEL PROGRAMMA

# definire una funzione di avvio programma e di menu
def pannello_comandi():
    scelta_utente = input("***** La Tua Banca *****\n"
                          "Digita 1 per aprire un nuovo conto\n"
                          "Digita 0 per terminare\n>>> ")
    match scelta_utente:
        case "1":
            apertura_conto()
        case _:
            print("Arrivederci... alla prossima")
            exit(0) # lo zero indica che il programma termina per una condizione pronosticata esatta. 1 in caso sia per problemi

#funzione per gestire l'apertura del conto corrente
def apertura_conto():
    nome_cognome = input("Grazie d'aver scelto di aprire un conto\nDigita il tuo nome e cognome >>> ")
    conto = ContoCorrente(nome_cognome)
    print(conto)
    scelta_utente = input("Desideri effettuare delle operazioni? (SI o NO) >>> ").upper()
    if scelta_utente == "SI":
        registrazione_operazione(conto)
    else:
        print(f"Arrivederci {conto.intestatario}... alla prossima")
        exit(0)

# funzione per gestire registrazione di operazioni
def registrazione_operazione(conto):
    while True:
        importo = input("Digita importo operazione (oppure 0 per terminare) >>> ")
        if importo != "0":
            print(conto.set_saldo(importo))
        else:
            print(f"Arrivederci {conto.intestatario}... alla prossima")
            exit(0)

# invocazione della funzione di avvio programma
pannello_comandi()