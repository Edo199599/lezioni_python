from object_oriented.principi.model.persona import Persona


# definizione classe Lavoratore
class Lavoratore(Persona):

# metodo di inizializzazione
# genero il __init__ con tasto destro su class, generate e seleziono cosa creare dai metodi esistenti in Persona
    def __init__(self, nome, cognome, eta, reddito): # aggiungo poi io reddito a quello generato automaticamente
        super().__init__(nome, cognome, eta)
        self.reddito = reddito

    # metodo di istanza per una funzionalità specifica di un lavoratore
    def richiesta_permesso(self):
        print(f"{self.cognome} chiede un permesso")

    #override metodo di superclasse per riscrittura completa della logica
    def fare_qualcosa(self):
        print(f"{self.cognome} lavora")

    def __str__(self): # recuperato sempre da generate dal tasto destro
        # return super().__str__() riga importata per mantenere il metodo uguale alla Superclasse
        return super().__str__() + f" (Lavoratore) Reddito: {self.reddito}" # aggiungo solo quello che serve alla stringa
