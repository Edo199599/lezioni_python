# classi astratte: utilizzate per creare un modello generale, funzionalità comuni per le sue sottoclassi
# impossibile però gestire qua oggetti della classe astratta creata, perché generica.
# metodi astratti creati per definire obblighi per le sottoclassi

from abc import ABC, abstractmethod
# libreria da importare per creare classi astratte (da ABC) e metodi astratti (da abstractmethod)

# definizione della superclasse astratta Computer
class Computer(ABC):

    # metodo di inizializzazione
    def __init__(self, sistema_operativo):
        self.sistema_operativo = sistema_operativo

    # metodo di istanza concreto per funzionalità con logica comune (a desktop e laptop che creeremo)
    def istallazione_software(self, nome_software):
        print(f"Istallazione di {nome_software} nel sistema operativo: {self.sistema_operativo}")

    # metodo di istanza astratto per funzionalità importante ma con logica diversa tra desktop e laptop
    @abstractmethod
    def sospensione_sistema(self):
        pass # metodo che ora non fa nulla perché verrà profondamente modificato nelle due sottoclassi

    # override del metodo di rappresentazione testuale per riscrittura completa
    def __repr__(self):
        return f"Linea Computer - Sistema Operativo: {self.sistema_operativo}"