# definizione di una funziona di pura esecuzione (non restituisce nulla)
# Prima riga chiamata Firma della funzione
def stampa_saluto():  # def sta per define. Quindi definisci la funzione chiamata di seguito.
    print("Ciao a tutti!")

#definizione di una funziona che restituisce un valore (un oggetto)
def torna_saluto():
     return "Ciao a tutti!" # ultima istruzione di una funzione. é la chiusura della stessa

# definizione di una funzione che accetta un parametro ed esegue una funzione
def salutami(nome):
    print(f"Ciao {nome}!")

# definizione di una funzione che accetta due parametri e ritorna un valore
def contatena(a,b):
    return a + b

# definizione di una funzione che accetta due parametri e ritorna un valore
def contatena_due(a,b):
    return str(a) + str(b) # questo risolve il caso di numeri dati che altrimenti verrebbero sommati

# funzione che accetta tre parametri (di cui 1 facoltativo) e ritorna un valore
def somma(a, b, c=0): # C è facoltativo perché ha già una definizione. Se no viene dato gli si assegna zero
    return a + b + c  # i facoltativi sono o tutti o gli ultimi parametri. Non il primo e il terzo.

# definizione di una funzione che accetta due parametri e ritorna un valore
def concatena_tre(a, b):
    return a + str(b)

# funzione che accetta tre parametri (tutti facoltativi) e ritorna un valore
def somma_due(a=0, b=0, c=0): # Assegnati tutti a zero così facoltativi. Posso passare qualsiasi numero di parametri
    return a + b + c

# definizione di una funziona che accetta n parametri ed esegue un'istruzione (PIù USATA DELLA SUCCESSIVA)
def itera(*args): # *args (solo l'asterisco è obbligatorio) unisce elementi nell'ordine dato
    print(args, type(args)) # genera una tupla. Con *args quindi non posso nella funzione modificare la struttura
    for elemento in args:
        print(elemento, end=" ")

#definizione di una funzione che accetta n parametri nominali ed esegue un'istruzione (MENO USATA)
def stampa(**kwargs): # anche qua contano solo i due asterischi. kwargs è una convenzione ma potrei scrivere napoli
    print(kwargs, type(kwargs)) #genera un dizionario con i valori nominali assegnati come chiave:valore



# INVOCAZIONE FUNZIONI
stampa_saluto()

torna_saluto() # non produce nulla a terminale perché le manca l'istruzione per usare quel return
#metodo 1
saluto = torna_saluto()
print(saluto)
#metodo 2
print(torna_saluto())

salutami("Edo")

print(contatena("Ciao ", "Mondo"))
print(contatena(1, 3)) # restituisce la somma e non la concatenazione
# print(contatena(2, "ciao")) commentato. da errore perché i valori inseriti sono di tipo diverso
print(contatena([1,2],[3,4])) # unisce le due liste

print(somma(1,2, 3))
print(somma(1,2)) # non da errore perché ho inizializzato c a 0 nella funzione

print(concatena_tre("Ciao", 10)) # printa bene perché cambia 10 in stringa e lo aggiunge a "Ciao"
# print(concatena_tre(10, "ciao")) errore perché al contrario non funziona avendo valori di tipo diverso
print(concatena_tre(b=10, a="ciao")) # se voglio comunque scrivere prima b per non avere errore li assegno direttamente

print(somma_due()) # passo zero parametri e non da errori essendo facoltativi in funzione, Ritona 0
print(somma_due(1,3,5)) # fa la normale somma
print(somma_due(67)) # il parametro viene ovviamente passato ad "a" e ritorna 67
print(somma_due(b=57, c=56)) #assegno solo i parametri che preferisco in maniera nominale e "a" rimane a 0 di default


itera(1,4,6,7) # viene generata una tupla (poi stampata per il for ma questo importa poco)
itera("ciao", "mondo")

stampa(nome="Mario", cognome="Rossi") #creato un dizionario con chiavi nome e cognome e valori assegnati Mario Rossi
stampa(nome="Mario", cognome="Rossi", eta=40)