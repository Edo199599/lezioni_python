# definizione superclasse Persona
class Persona:

    # metodo di inizializzazione
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    # metodo di istanza per funzionalità generica che abbia una logica comune con le future sottoclassi
    def camminare(self):
        print(f"{self.nome} cammina")

    # metodo di distanza per una funzionalità generica per una logica generica (non comune)
    def fare_qualcosa(self):
        print(f"{self.cognome} sta facendo qualcosa")

    # riscrittura completa del metodo di rappresentazione testuale di object (principio di polimorfismo)
    def __str__(self):
        return f"{self.nome} {self.cognome} - {self.eta} anni"

