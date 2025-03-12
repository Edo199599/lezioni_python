"""
Creare struttura ad oggetti per un'azienda che produce dispositivi elettronici
Computer: Computer Fissi (desktop) e Computer Portatili (laptop)
Telefoni: Smartphone e Cordless
"""
from object_oriented.full_oo.model.cordless import Cordless
from object_oriented.full_oo.model.desktop import Desktop
from object_oriented.full_oo.model.laptop import Laptop
from object_oriented.full_oo.model.smartphone import Smartphone

# dichiarazione e istanziazione dei nostri oggetti concreti
desktop = Desktop("Windows", True)
laptop = Laptop("MAC-OS", False)
smartphone = Smartphone(12, "Nano-SIM")
cordless = Cordless(30, 7)


print(desktop)
print(laptop)
print(smartphone)
print(cordless)

#invocazioni possibili da superclassi base
desktop.istallazione_software("PyCharm")
laptop.istallazione_software("Eclipse")
desktop.sospensione_sistema()
laptop.sospensione_sistema()

smartphone.invio_chiamata("+39 33129")
cordless.invio_chiamata("+39 3427979")
smartphone.connessione()
cordless.connessione()

#invocazioni possibili da superclasse Dispositivo
desktop.inizializzazione_dispositivo()
cordless.ricarica_batteria()
laptop.inizializzazione_dispositivo()
smartphone.ricarica_batteria()

# uguaglianza oggetti
smartphone_due = Smartphone(12, "Nano-SIM") # stesse caratteristiche di smart_uno
print(smartphone_due == smartphone) # esce false
# nelle classi int, str, float è stato fatto un override della funzione uguaglianza
# negli oggetti l'unico modo per confrontarli è che puntino allo stesso oggetto in memoria
# es: smartphone_due = smartphone (in questo caso punterebbero allo stesso spazio di memoria
