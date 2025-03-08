"""
Partire da una lista vuota e popolarla con 10 valori numerici interi pseudo-casuali
- 1^ lista dove ci potranno essere dei duplicati
- 2^ lista senza duplicati
"""
import random

# lista vuota che ospiterà i numeri casuali
lista = []

# ciclo di popolamento
for _ in range(10):
    casuale = random.randint(1, 10) # sia minimo che massimo sono compresi
    lista.append(casuale)

# stampa della lista popolata
print(lista)

# pulizia lista
lista.clear()

# ciclo di popolamento senza duplicati
contatore = 0
while len(lista) < 10:
    casuale = random.randint(1, 10)
    contatore += 1
    if casuale in lista:
        continue
    else:
        lista.append(casuale)

# stampa lista popolata senza valori duplicati
print(f"{lista} dopo un numero di interazioni pari a {contatore}")