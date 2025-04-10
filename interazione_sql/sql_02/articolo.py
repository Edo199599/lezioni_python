
class Articolo:

    def __init__(self, id=None, nome=None, prezzo=None, categoria=None):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.categoria = categoria # gestione della relazione molti a uno (n:1)
        # molti articoli possono appartenere alla stessa categoria

    # metodo di rappresentazione testuale
    def __repr__(self):
        return f"Articolo {self.id} ({self.categoria.stampa_per_articolo()}) - {self.nome}, {self.prezzo:.2f} Euro"
        # potrei anche scrivere quella funzione come solo self.categoria.descrizione

    # metodo di rappresentazione testuale specifico per inclusione in categoria
    def stampa_per_categoria(self):
        return f"Articolo {self.id} - {self.nome}, {self.prezzo:.2f} Euro"