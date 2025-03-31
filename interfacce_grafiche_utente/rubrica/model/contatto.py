
class Contatto:

    # metodo di inizializzazione
    def __init__(self, nome=None, cognome=None, telefono=None):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    # metodo per la rappresentazione testuale (provvisorio)
    # lo vorremo poi mostrare in interfaccia grafica non in console
    def __repr__(self):
        return f"{self.nome} {self.cognome} - Telefono: {self.telefono}"

    # metodo di classe per la deserializzazione
    # trasformare la lista di dizionari, che la funzione in contatto_repository crea, in oggetti Contatto
    @classmethod
    def deserializzazione(cls, dizionario):
        return cls(**dizionario)
    # quando viene invocata le passiamo un dizionario
    # mi ritorna un oggetto Contatto cls() con le chiavi del dizionario trasformate in attributi
    # i ** servono per passare un numero variabile di argomenti (le chiavi del dizionario)

    # metodo di istanza per coversione Contatto -> list
    def lista_attributi(self):
        return [self.nome, self.cognome, self.telefono]