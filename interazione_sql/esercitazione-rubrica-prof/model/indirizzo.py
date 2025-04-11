class Indirizzo:

    # inizializzazione oggetto e struttura
    def __init__(self, id=None, via=None, civico=None, cap=None, comune=None, provincia=None):
        self.id = id
        self.via = via.title()
        self.civico = civico.lower()
        self.cap = cap
        self.comune = comune.title()
        self.provincia = provincia.upper()

    # rappresentazione testuale
    def __repr__(self):
        return f"{self.via}, {self.civico} - {self.cap} {self.comune} ({self.provincia})"