# dichiarazione e istanziazione tuple (Simili alle liste ma non modificabili)
tupla_uno = (1, 2, ["Ciao", "Mondo"], True, "bello") #literal (Le tonde sono opzionali. Migliorano la leggibilità)
print(tupla_uno, type(tupla_uno))

tupla_due = tuple([1, 2, 3, 4]) #con costruttore (Vuole un iterabile. Senza lista non la accetterebbe)
print(tupla_due, type(tupla_due))

#tupla_tre = tuple(1) commentato perché un solo oggetto int non è un oggetto iterabile come le liste

tupla_quattro = tuple("ciao") #ritorna tupla con tutti i caratteri che compongono la stringa separati
print(tupla_quattro, type(tupla_quattro))

tupla_cinque = 1, # per un singolo elemento assegnamo literal e con la virgola. Sarebbe variabile altrimenti
print(tupla_cinque, type(tupla_cinque))

tupla_vuota_uno = () #literal, tupla vuota. Essendo immodificabile non ha molto senso crearla così in ogni caso
print(tupla_vuota_uno, type(tupla_vuota_uno))
tupla_vuota_due = tuple() #tupla vuota mediante costruttore
print(tupla_vuota_due, type(tupla_vuota_due))



#accesso agli elementi (analogo ad una lista con indici che partono da zero)
print(tupla_uno[2]) #print del terzo elemento della tupla uno
print(len(tupla_uno), len(tupla_vuota_due))


#slicing su tuple
tupla_sei = tupla_uno[1:4] # per avere i 3 centrali essendo il secondo valore escluso sempre
print(tupla_sei)

# unpackagin
a, b, c = tupla_sei # con questo metodo devo assegnare x variabili pari a x numero valori della tupla
print(a, b, c)
