
class Contatto:

    def __init__(self, id=None, nome=None, cognome=None, telefono=None, mail=None, indirizzo=None):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
        self.mail = mail
        self.indirizzo = indirizzo

    # metodo di rappresentazione testuale
    def __repr__(self):
        return f"Contatto {self.id} - {self.nome} {self.cognome} - {self.telefono}, {self.mail}, {self.indirizzo}"