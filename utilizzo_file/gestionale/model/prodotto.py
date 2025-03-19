# definizione classe di modellazione oggetto logico Prodotto
# con struttura conforme al file di archiviazione

class Prodotto:

    def __init__(self, id=None, tipologia=None, marca=None, modello=None, prezzo=None):
        self.id = id
        self.tipologia = tipologia
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo

    # metodo di rappresentazione testuale
    def __repr__(self):
        return (f"Id Prodotto: {self.id} - Tipologia: {self.tipologia}\nMarca: {self.marca} - "
                f"Modello: {self.modello}\nPrezzo: {self.prezzo:.2f} Euro\n----------------------------")


    # metodo di rappresentarsi in formato lista
    def to_list(self):
        return [self.id, self.tipologia, self.marca, self.modello, self.prezzo]