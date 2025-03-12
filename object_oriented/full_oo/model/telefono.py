from abc import ABC, abstractmethod

# definizione superclasse astratta Telefono
# 1. Non si possono creare oggetti di questo tipo
# 2. Si possono definire metodi astratti
# 3. Modello generale di aggregazione

class Telefono(ABC):

    # metodo di inizializzazione
    def __init__(self, durata_batteria):
        self.durata_batteria = durata_batteria

    # metodo di istanza contreto per funzionalità con logica comune a Smartphone e Cordless
    def invio_chiamata(self, numero):
        print(f"{self} - invio chiamata a {numero}")

    # metodo di istanza astratto per funzionalità importante con logica differente tra Smartphone e Cordless
    @abstractmethod
    def connessione(self):
        pass

    # override del metodo di rappresentazione testuale per riscrittura completa
    def __repr__(self):
        return f"Linea Telefoni - Durata Batteria: {self.durata_batteria}"



