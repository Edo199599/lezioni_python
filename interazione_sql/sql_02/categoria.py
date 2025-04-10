
class Categoria:

    def __init__(self, id=None, descrizione=None, articoli=None):
        self.id = id
        self.descrizione = descrizione
        self.articoli = articoli #articoli è una lista di oggetti Articolo per gestione di relazione uno a molti (1:n)
        # Python non tipizza già in partenza quindi uso il plurale per aiutarmi a capirlo

    # metodo di rappresentazione testuale
    def __repr__(self):
        return f"Categoria - id: {self.id} - descrizione: {self.descrizione}"

    # metodo di rappresentazione testuale specifico per inclusione in articolo
    def stampa_per_articolo(self):
        return f"Articolo {self.id} ({self.descrizione})"