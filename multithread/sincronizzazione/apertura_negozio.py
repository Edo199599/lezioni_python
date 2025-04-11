from negozio import Negozio
from cliente import Cliente

# istanziazione oggetto Negozio (comune a tutti i clienti Thread)
negozio = Negozio()

# le risorse di classe come la lista di attesa non possiamo accederle facilmente da qui.
# creiamo una lista locale per creazione e avvio thread cliente e per la gestione della lista di attesa
clienti = [Cliente(nome, negozio) for nome in ["Mario", "Luigi", "Peach", "Yoshi", "Bowser"]]

# popolamento lista attesa ufficiale
Cliente.lista_attesa.extend(clienti)

# apertura del negozio
print("Clienti in attesa: ", Cliente.lista_attesa)
for cliente in clienti:
    cliente.start()
    # avvio del thread cliente
    # il metodo start() chiama il metodo run() della classe Cliente
    # quindi viene eseguito il comportamento del thread

# il programma non è propriamente sequenziale
# ESEMPIO 1
# per un sito ogni thread potrebbe essere adibito alla gestione di una richiesta singola / utente singolo
# ogni persona che si collega ad un sito è un thread che opera in contempornea ma esegue alcune azioni in sequenza
# ESEMPIO 2
# un dipendente da terminale (negozio) vende prima che un altro da un altro terminale possa entrare.
# rischieresti cose simultanee