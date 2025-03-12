from object_oriented.full_oo.model.dispositivo import Dispositivo
from object_oriented.full_oo.model.telefono import Telefono


# definizione sottoclasse concreta Smartphone

class Smartphone(Telefono, Dispositivo):

    # metodo di inizializzazione
    def __init__(self, durata_batteria, tipo_sim):
        super().__init__(durata_batteria) # il richiamo alla sottoclasse è sempre la prima istruzione
        self.tip_sim = tipo_sim

    # override obbligatorio metodo astratto di superclasse Telefono
    def connessione(self):
        print("Inserire SIM")

    #override obbligatorio del metodo astratto della superclasse Dispositivo
    def inizializzazione_dispositivo(self):
        print("Acquisisci connessione e configura account Google")

    # override del metodo di rappresentazione testuale da superclasse per integrazione logica
    def __repr__(self):
        return super().__repr__() + f" Tipo: Smartphone - Tipo SIM: {self.tip_sim}"


    # override metodo per personalizzare il criterio di uguaglianza da classe Object
    def __eq__(self, __value):
        # self è il valore prima dell'==, __value è il valore dopo l'==
        #return super().__eq__(__value) #lasciando solo questa riga il criterio di uguaglianza rimane uguale
        #aggiungo:
        if isinstance(__value, Smartphone):
        # isinstance funzione che prende un oggetto e una classe e da True se l'oggetto è istanza della classe
            return self.durata_batteria == __value.durata_batteria and self.tip_sim == __value.tip_sim
            # se prima è vero, ritorna vero solo se le due indicazioni sopra sono equivalenti
        return False
