
class Indirizzo:

    def __init__(self, id=None, via=None, civico=None, cap=None, comune=None, provincia=None):
        self.id = id
        self.via = via
        self.civico = civico
        self.cap = cap
        self.comune = comune
        self.provincia = provincia


    # metodo di rappresentazione testuale
    def __repr__(self):
        return f"Indirizzo {self.id} - {self.via} {self.civico}, {self.cap} {self.comune} ({self.provincia})"
