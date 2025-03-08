
# dichiarazuibe e istanziazione di liste vuote
lista_uno = [] #literal
print(lista_uno, type(lista_uno))
lista_due = list() # mediante costruttore di classe list
print(lista_due, type(lista_due))


# popolamento delle liste
lista_uno.append(10)
lista_uno.append(20)
print(lista_uno, len(lista_uno))
lista_uno.insert(1, 34) #inserire il valore 34 nella posizione ad indice 1
print(lista_uno, len(lista_uno))

# dichiarazione, istanziazione e popolamento
lista_tre = [3, 5, "ciao", False] #literal
lista_quattrov1 = list() # non si possono passare al costruttore i valori come con literal
lista_quattro = list((4, 10, "bello", 10)) # si inserisce così con tupla
print(lista_quattro, len(lista_quattro))
lista_quattro.append(4 < 8) # passo un espressione che aggiungerà un True alla lista
print(lista_quattro, len(lista_quattro))

# accesso a elementi in una lista (in base a indice posizionale)
print(lista_tre[2]) # stampa elemento a indice 2 (quindi il terzo della lista) (errore se inesistente)
print(lista_tre[0]) # accesso al primo elemento (errore se lista vuota)
print(lista_tre[-1]) # accesso all'ultimo elemento

# modifica di elementi presenti nella lista
lista_quattro[1] = True # non devo riassegnare ma posso agire direttamente su oggetto originale
print(lista_quattro) # ho sostituito il valore ad inidice 1 con un True

# rimozione di elementi presenti in lista
lista_quattro.remove(10) # rimuove il valore indicato alla prima occorrenza (errore se valore assente)
print(lista_quattro)

# concatenazione liste
lista_uno += lista_tre # aggiunge agli elementi di lista_uno gli elementi di lista_tre in coda
print(lista_uno)

# raddoppio degli elementi
lista_uno *= 2
print(lista_uno)

# operazioni di slicing
print(lista_uno[3:]) # stampa da elemento a indice 3 a fine naturale della lista
print(lista_uno[:4]) # parti dall'inizio naturale e arriva a indice 3 (il 4 è escluso)
print(lista_uno[2:5]) #parti da elemento con indice 2 fino a indice 4 (il 5 è escluso)
# anche in questo caso indici negativi partono dalla fine con indice -1 l'ultimo elemento

# principali metodi di classe list
lista_uno.reverse() # anche qui lavoriamo sull'oggetto direttamente invece che riassegnarlo
print(lista_uno)
# lista_uno.sort() commentato per errore ordinamento su lista eterogenea
# print(lista_uno)
lista_cinque = [45, 5, 78, 3]
lista_cinque.sort() # possibile perché la lista_cinque contiene elementi omogenei
print(lista_cinque)
lista_sei = [45, 5, 78, 3]
lista_sei.sort(reverse=True) # riordina gli elementi partendo da criterio opposto
print(lista_sei)

# rimozione di tutti gli elementi presenti
lista_sei.clear()
print(lista_sei, len(lista_sei))

# unpackaging sulle liste
lista_sette = ["ciao", True]
uno, due = lista_sette
print(uno,due)

# scomposizione di una stringa in una lista (in base a carattere separatore)
stringa = "uno,due,tre"
lista_otto = stringa.split(",") # passiamo il carattere separatore per decidere come splittare
print(lista_otto, len(lista_otto))

# ricomposizione di una lista in una stringa
stringa = " ".join(lista_otto) # unisce con un carattere spazio in mezzo
print(stringa)
# lista_otto.append(12) commentato in quanto causa errore. Fattibile solo con str non int
# stringa = " ".join(lista_otto)