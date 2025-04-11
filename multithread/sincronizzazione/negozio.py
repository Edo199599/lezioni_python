import threading

class Negozio:

    # metodo di inizializzazione
    def __init__(self):
        self.occupato = False
        # quando viene creato l'oggetto negozio l'attributo occupato è false
        self.condition = threading.Condition()
        # creiamo un oggetto condition per la sincronizzazione dei thread
        # otteniamo così l'uso di wait() e notify() per la gestione della lista di attesa

    # metodo per la gestione dell'ingresso nel negozio (risorsa)
    # per risorsa si intende un oggetto che può essere condiviso tra più thread
    def ingresso(self, cliente):
        with self.condition:
            while self.occupato:
                self.condition.wait()
                # fintanto che occupato è true il thread cliente aspetta
        self.occupato = True
        print(f"{cliente} entra nel negozio.")

    # metodo per la gestione dell'uscita dal negozio (risorsa)
    def uscita(self, cliente):
        with self.condition:
            self.occupato = False
            print(f"{cliente} esce dal negozio.")
            self.condition.notify_all()
            # quando il cliente esce dal negozio viene notificato che la risorsa è libera