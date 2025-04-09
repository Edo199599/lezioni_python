
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

    # metodo per verificare quando due contatti sono uguali (tutti gli attributi sono uguali)
    def __eq__(self, other):
        if isinstance(other, Contatto): # verifica che l'oggetto passato sia un oggetto di tipo Contatto
            return self.nome == other.nome and self.cognome == other.cognome and self.telefono == other.telefono
        else:
            return False

    # metodo di istanza per serializzazione (Contatto -> dict) - (per scrivere su file)
    def serializzazione(self):
        return self.__dict__ # funzione nativa in Python per ottenere un dizionario con gli attributi dell'oggetto in __init__()
