# EREDITà MULTIPLA
#creiamo una superclasse superiore a tutte (successivamente alle altre)
from abc import ABC, abstractmethod

# definizione della superclasse astratta Dispositivo (collegamento tra le 2 linee di produzione)
# interfacce ponte tra diverse componenti del programma. (Collegano due linee del programma) - Non esistono in Python
class Dispositivo (ABC):

    # metodo di istanza concreto per una funzionalità non utilizzata da tutti ma con logica comune per chi la utilizza
    def ricarica_batteria(self):
        print("Batteria Scarica... Collega alla presa di corrente")

    # metodo di istanza astratto per una funzionalità che risulti importante per tutti ma con logiche differenti
    @abstractmethod
    def inizializzazione_dispositivo(self):
        pass

