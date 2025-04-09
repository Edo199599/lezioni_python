# classe di modellazione oggetto logico Persona (interazione con tabella persone)
class Persona:

    # metodo di inizializzazione
    def __init__(self, id=None, nome=None, cognome=None, eta=None):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __repr__(self):
        return f"Persona - id: {self.id} - {self.nome} {self.cognome} di anni {self.eta}"