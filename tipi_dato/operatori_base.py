import math

print(round(10.329893, 2)) #arrotondamento su cifra decimale successiva a quella indicata

print(math.ceil(5.1245)) # arrotondamento ad int sempre per eccesso
print(math.floor(10.67)) # arrotondamento ad int sempre per difetto

# i numeri sono oggetti immutabili
numero = 10
print(numero, id(numero)) #viene allocato alla var numero una casella in memoria con un 10 dentro
numero = numero + 12
print(numero, id(numero)) #alloco un nuovo spazio di memoria, non sovrascrivo il precedente
numero = numero - 12
print(numero, id(numero)) #se prima di un reset di memoria, alloca lo stesso id precedente. Altrimenti nuova

