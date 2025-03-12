from object_oriented.full_oo.model.computer import Computer
from object_oriented.full_oo.model.dispositivo import Dispositivo


# definizione di una sottoclasse concreta Desktop
class Desktop(Computer, Dispositivo):
# prima di ridefinire sospensione_sistema era sottolineato perché bisogna definire tutte le classi astratte

    #metodo di inizializzazione
    def __init__(self, sistema_operativo, monitor_incluso):
        super().__init__(sistema_operativo)
        self.monitor_incluso = monitor_incluso

    #override obbligatorio del metodo astratto della superclasse computer
    def sospensione_sistema(self): # tasto destro e implement method invece che override
        print("Seleziona SOSPENSIONE dal menu Start")

    #override obbligatorio del metodo astratto della superclasse Dispositivo
    def inizializzazione_dispositivo(self):
        print("Collega alla presa di corrente e configura account")

    # override del metodo di rappresentazione testuale da superclasse per integrazione logica
    def __repr__(self):
        return super().__repr__() + f" Tipo: Desktop - Monito Incluso: {self.monitor_incluso}"


