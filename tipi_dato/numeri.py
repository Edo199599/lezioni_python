
# dichiarazione e istanziazione di variabili per numeri interi
intero_uno = 24 #literal (nome del valore assegnato)

print("\nintero_uno")
print(intero_uno)

# aggiungo: per far capire che variabile sia intero_uno posso usare type() che ora mi stamperà int per intero
print(intero_uno, type(intero_uno))

# posso usare anche la funzione int per costruire la variabile int. può essere anche solo int(12), senza apici
intero_due = int("12")
print(intero_due, type(intero_due))

# assegnare ad una variabile il valore zero può essere fatto nei due modi seguenti
intero_tre = 0
intero_quattro = int()

# dichiarazione e instanziazione di variabili per numeri decimali
decimale_uno = 10.25 #literal
print(decimale_uno, type(decimale_uno))
decimale_due = float(2.1) #analogamente a int() c'è la funzione (float) che prende anche float("2.1")
decimale_tre = '0' #oppure = float() in entrambi i casi crea un valore 0.0

#utilizzo operatori + - x tra interi decimali
risultato_somma = intero_uno + decimale_uno
print(risultato_somma, type(risultato_somma)) #tipo float in quanto intero più decimale

# utilizzo operatore / (divisione naturale) tra interi
risultato_divisione = intero_uno / intero_due
print(risultato_divisione, type(risultato_divisione)) # 2.0 risultato float

# utilizzo operatore // (divisione intera) tra interi
risultato_divisione_intera = intero_due // intero_uno
print(risultato_divisione_intera, type(risultato_divisione_intera)) # 0 (parte decimale troncata) tipo int

# utilizzo operatore // (divisioni intera) tra decimali
risultato_divisione_intera_decimali = decimale_uno // decimale_due
print(risultato_divisione_intera_decimali, type(risultato_divisione_intera_decimali)) #4.0 (parte decimale troncata) tipo float

#utilizzo operatore % (resto o modulo)
print(5 % 2) # 1 essendo il resto della divisione dei due valori

#utilizzo operatore ** (elevazione a potenza)
print(5 ** 2) # ovviamente 25

#ordine precedenza operatori aritmetici
print(5 + 2 * 2) # 9 poiché segue il classico ordine di precedenza delle operazioni PEMDAS
print((5 + 2) * 2) # otteniamo 14

# arrotondamento/troncamento dei valori decimali
print(round(10.51)) # non avendo passato il numero di cifre decimali da mantenere arrotonda direttamente all'intero più vicino
print(round(10.5)) # il .5 con primo numero pari viene arrotondato per difetto
print(round(9.5)) # il .5 con primo numero dispari arrotonda per eccesso

