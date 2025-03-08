# dobbiamo stampare 10 volte la frase Hello World Tenendo il conteggio delle iterazioni
for contatore in range(10): #0-9
    print(f"Hello World -> a questo giro il contatore vale {contatore}")

print("*******************************************************************")

#dobbiamo stampare 10 volte la frase "Hello World" tenendo il conteggio delle iterazioni (1-10)
for contatore in range(1,11): #1-10
    print(f"Hello World -> a questo giro il contatore vale {contatore}")

print("*******************************************************************")

#iteriamo gli elementi di una lista per stamparli
lista = ["uno", "due", "tre", "quattro"]
for elemento in lista:
    print(elemento)

print("*******************************************************************")

#iteriamo gli elementi di una lista per stampare solo quelli con indice pari
for indice in range(0, len(lista), 2): #indicato il passo
    print(lista[indice])

print("*******************************************************************")

#iteriamo gli elementi di una lista dall'ultimo al primo (iterazione inversa) con funzione range e passo negativo
for indice in range(len(lista) -1, -1, -1): #dalla lunghezza-1 al valore 0 incluso quindi indce -1 con passo -1
    print(lista[indice])

print("*******************************************************************")

#iteriamo gli elementi di una lista dall'ultimo al primo (iterazione inversa) con slicing lista
for elemento in lista[::-1]:
    print(elemento)
print(lista) # no alterazione struttura lista

print("*******************************************************************")

# abbiamo una lista di numeri e li vogliamo stampare ma se nella lista troviamo il numero 5 fermiamo il ciclo
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeri:
    if numero == 5:
        break
    print(numero)
else:
    print("Il ciclo ha terminato il suo lavoro") #utilizzato solo quando le clausole di break non vengono invocate
print("Fine Programma")

print("*******************************************************************")

# abbiamo una lista di numeri e li vogliamo stampare tutti tranne il numero 5
for numero in numeri:
    if numero == 5:
        continue # passa oltre all'iterazione successiva skippando le successive istruzioni
    print(numero) # non viene infatti stampato il 5

