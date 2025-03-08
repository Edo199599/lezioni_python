# dichiarazione e istanziazione di variabili per booleani
booleano_uno = True
booleano_due = False
print(booleano_uno, type(booleano_uno))
print(booleano_due, type(booleano_due))

# analisi logiche di verità
print(bool(12), bool(0)) # True (tutti i numeri tranne lo zero) / False (numero 0)
print(bool(" "), bool("")) # True (ogni stringa con almeno un carattere) / False (stringhe vuote)
print(bool([1,2]),bool([])) #True (strutture con almeno un elemento) / False (struttura vuota)
print(bool(None)) # False (valore booleano implicito di tutto ciò che è nullo)
#es: assegni una variabile a = None per assegnarla successivamente


# operatori logici and e or
print(True and True) #True (Tutte le sotto-espressioni devono essere vere)
print(True and False) #False (Se una delle sotto-espressioni è falsa)
print(True or False) #True (Almeno una delle sotto-espressioni è vera)
print(False or False) #False (Entrambe le sotto-espressioni sono false)

# espressioni con operatori di confronto
espressione_uno = 12 <= 10
print(espressione_uno, type(espressione_uno)) # esegue l'operazione vedendo che è False e la tipizza come booleana
espressione_due = "ciao" == "ciao"
print(espressione_due, type(espressione_due))
espressione_tre = 10 != 10 and 1 < 3
print(espressione_tre, type(espressione_tre))
espressione_quattro = 10 != 10 or 1 < 3
print(espressione_quattro, type(espressione_quattro))

# operatore not (negazione)
espressione_cinque = not (10 == 10)
print(espressione_cinque)

# operatori di identità is per numeri
potenza_uno = 2 ** 2
potenza_due = 2 ** 2
print(potenza_uno == potenza_due) # operatore == controlla il valore
print(potenza_uno is potenza_due) # operatore is controlla la locazione di memoria
# questo is da True. Per numeri piccoli viene allocato lo stesso spazio di memoria
potenza_uno = 2 ** 1000
potenza_due = 2 ** 1000
print(potenza_uno is potenza_due) # ora da False. Numeri >>
potenza_due = potenza_uno # assegno ora potenza_due allo stesso spazio di memoria di potenza_uno
print(potenza_uno is potenza_due) # ora torna ad essere True

#operatore di identità is per stringhe
stringa_uno = "a" * 2
stringa_due = "a" * 2
print(stringa_uno == stringa_due)
print(stringa_uno is stringa_due) #True come nel caso dei numeri per stringhe piccole
stringa_uno = "a" * 200000000
stringa_due = "a" * 200000000
print(stringa_uno is stringa_due)