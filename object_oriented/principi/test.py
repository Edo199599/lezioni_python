# script eseguibile della nostra applicazione.
# I moduli e classi di modellazione sono definiti dentro model

from model.studente import Studente
from model.lavoratore import Lavoratore

# dichiarazione e istanziazione oggetti da gestire
studente = Studente("Edoardo", "Bergamaschi", 29, 26.7)
lavoratore = Lavoratore("Alberto", "Biggiogero", 50, 1300.55)

print(studente) # la modalità in cui viene stampata viene ereditata dal __repr__ della superclasse + modifica in classe
print(lavoratore)

# invocazione metodi e attributi
print(studente.eta) # legati alla classe persona quindi ha quegli attributi
# print(lavoratore.media_voti) non c'è nessuna connesione tra lavoratore e studente
print(studente.media_voti)

studente.camminare() # ereditato dalla superclasse
studente.fare_qualcosa() # ereditato dalla superclasse ma in override nella sua classe
studente.annotazione_appunti() # suo metodo personale
# studente.richiesta_permesso() # non accedibile
lavoratore.camminare()  # ereditato dalla superclasse
lavoratore.fare_qualcosa() # ereditato dalla superclasse ma in override nella sua classe

