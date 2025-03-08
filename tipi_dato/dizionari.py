# Dichiarazione e istanziazione di un dizionario
# (strutture mutabili, possono contenere tutte le strutture dato, valori organizzati per chiavi, non indici)
#assegnazione chiave:valore

# diz_uno = {1:2, 2:"ciao", "ciao":[1, 2, 3, 4], (1,2,3):True, [1,2]:"mondo"}
#le chiavi di assegnazione valori devono essere immutabili. Per questo la lista [1,2] da errore

diz_due = {1:2, 2:"ciao", "ciao":[1, 2, 3, 4], (1,2,3):True, 1:"mondo"} # doppia chiave 1
print(diz_due, type(diz_due)) # la seconda assegnazione di una stessa chiave sovrascrive la prima

diz_tre = dict(nome = "Mario", cognome="Rossi")
print(diz_tre, type(diz_tre))

# inizializzazione dizionari vuoti tra literal e costruttore
diz_quattro = {} #crea un dizionario e non un set (diz molto più usati)
diz_cinque = dict()
print(type(diz_quattro), type(diz_cinque))

# accesso ai singoli elementi del dizionario
print(diz_due["ciao"]) # devo dare la chiave di associazione non esistendo indici nei dizionari

# unpackaging su dizionari
# usiamo diz 2 che ha 4 elementi
a, b, c, d = diz_due
print(a, b ,c, d) # stampa solo le chiavi e non i valori legati. Le chiavi sono gli elementi importanti

# manipolazione dizionari
diz_due[4] = "nuovo elemento" # tra quadre no indice ma chiave associativa (AGGIUNTA)
print(diz_due)
diz_due[4] = "nuovo elemento modificato" # proviamo a reinserire un valore alla chiave 4 (MODIFICA)
print(diz_due) # nuovo valore a chiave 4 sovrascrive il precedente
print(diz_due.pop(4)) #stampa l'elemento alla chiave associata e lo cancella dal diz (CANCELLARE). Potrei usarlo per assegnare
print(diz_due) # non è più presente nel dizionario
# print(diz_due.pop(4)) da errore perché non esiste più quel valore.
print(diz_due.pop(4, "elemento non trovato")) #evita il crash del punto precedente e restituisce il valore di default

# ispezione dizionari
print(len(diz_due))
print(diz_due.items()) # ritorna una lista di tuple contenenti (chiave, elemento) che rappresentano l'intero dizionario
print(diz_due.keys()) # ritorna una lista delle chiavi del dizionario
print(diz_due.values()) # ritorna una lista con tutti gli elementi del dizionario