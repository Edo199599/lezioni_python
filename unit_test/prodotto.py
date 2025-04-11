class Prodotto:

    # metodo di inizializzazione
    def __init__(self, nome, prezzo):
        if not isinstance(prezzo, (int, float)) or prezzo < 1:
            raise ValueError("Il prezzo deve essere un numero non inferiore a 1")
        # definiamo questi controlli ancora prima di andare a definire i self
        # per bloccare sul nascere la creazione dell'oggetto Prodotto
        self.nome = nome
        self.prezzo = prezzo


