# importo la classe persona
from object_oriented.principi.model.persona import Persona
# non scriverlo manualmente ma auto quando appare il consiglio Persona dentro class Studente(...)

# definizione Classe Studente, come sottoclasse di Persona (inserita quindi tra parentesi)
class Studente(Persona):

    def __init__(self, nome, cognome, eta, media_voti):
        # nome, cognome ed età non andranno però gestiti qua ma nel metodo di iniziaizzazione della superclasse
        super().__init__(nome, cognome, eta) # così settiamo i 3 attributi per Persona e Studente
        self.media_voti = media_voti

    # metodo di istanza per una funzionalità specifica dello studente
    def annotazione_appunti(self):
        print(f"{self.nome} prende appunti")

    #override metodo di superclasse per riscrittura completa della logica
    def fare_qualcosa(self):
        print(f"{self.cognome} studia")

    def __str__(self): # recuperato sempre da generate dal tasto destro
        # return super().__str__() riga importata per mantenere il metodo uguale alla Superclasse
        return super().__str__() + f" (Studente) Media Voti: {self.media_voti}" # aggiungo solo quello che serve alla stringa

