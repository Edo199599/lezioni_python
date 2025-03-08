# dichiarazione e istanziazione di una variabile globale
variabile_globale = 10

# funzione che dichiara una variabile locale e legge la variabile globale
def funzione_uno():
    variabile_locale = 12
    print(variabile_globale + variabile_locale)

# funzione che modifica la variabile globale
def funzione_due():
    variabile_globale += 13 #cerca di analizzarla come una variabile locale a cui modificare il valore
    print(variabile_globale)

def funzione_tre():
    global variabile_globale # recupera la variabile globale da fuori per poterla modificare
    variabile_globale += 13 #cerca di analizzarla come una variabile locale a cui modificare il valore
    print(variabile_globale)

# proviamo a leggere le variabili
# scope: ambito da cui è possibile accedere alla variabile stessa.
print(variabile_globale) # possibile
# print(variabile_locale) impossibile
# variabile_locale ha uno scope limitato alla funzione stessa. Viene distrutta alla fine della funzione


# invocazione funzione di lettura
funzione_uno() # una funzione di sola lettura riesce ad usare le variabili globali senza errori
# funzione_due()# impossibile perché le variabili globali se si cercano di modificare e non leggere e basta danno errore
funzione_tre() # funziona per la definizione interna di global, METODO PERICOLOSO E SCONSIGLIATO


# definizione di una funzione anonima
anonima = lambda x, y: x + y # assegno funzione ad una variabile, le dico che cosa deve ricevere : cosa deve fare
print(type(anonima)) # tipo function

#utilizzo della funzione anonima
print(anonima(2,5))
print(anonima("Ciao ", "Mondo"))