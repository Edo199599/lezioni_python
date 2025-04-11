import threading
import random # per determinare il tempo casuale di attesa per l'ingresso nel negozio
import time # per determinare il tempo di attesa per l'uscita dal negozio


class Cliente(threading.Thread):

    # attributo di classe per rappresentare la lista di attesa
    lista_attesa = []

    # metodo di inizializzazione
    def __init__(self, nome, negozio):
        super().__init__()
        self.nome = nome
        self.negozio = negozio
        # l'attributo negozio rappresenta l'oggetto negozio per poter gestire l'ingresso e l'uscita
        # rimarrà sempre lo stesso per ogni cliente

    # metodo di rappresentazione testuale
    def __repr__(self):
        return self.nome
    # giusto per printare il cliente ottenendone il nome

    # ovveride del metodo run da superclasse Thread per assegnare il comportamento del thread
    def run(self):
        tempo_casuale = random.randint(5, 15)
        self.negozio.ingresso(self)
        Cliente.lista_attesa.remove(self)
        # per ogni cliente che entra nel negozio viene rimosso dalla lista di attesa
        print("Clienti in attesa: ", Cliente.lista_attesa if len(Cliente.lista_attesa) > 0 else print("Lista di attesa vuota"))
        time.sleep(tempo_casuale)
        self.negozio.uscita(self)
