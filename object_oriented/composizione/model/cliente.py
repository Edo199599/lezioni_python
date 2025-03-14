# definizione classe di modellazione oggetto Cliente

class Cliente:

    #metodo di inizializzazione
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    #metodo di istanza per rappresentazione testuale
    def __repr__(self):
        return f"Cliente: {self.nome} {self.cognome}"