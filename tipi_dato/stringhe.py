#dichiarazione e istanziazione variabili per stringhe (sequenze di caratteri)

string_uno = "Ciao Mondo" # literal
print(string_uno, type(string_uno))

string_due = str("Ciao Mondo") # mediante costruttore di classe str
print(string_due, type(string_due))

string_tre = str(100.56)
print(string_tre, type(string_tre))

string_quattro = 'ciao' # apici singoli o doppi non cambia nulla

string_cinque = '''
Sono una stringa
    su più linee
e supporto indentazione
'''
print(string_cinque, type(string_cinque))

# stringa formattata
numero = 20
# string_sei = "Il valore della variabile numero è " + numero # da errore. Solo stringhe sono concatenabili
string_sei = f"Il valore della variabile numero è {numero}"
print(string_sei)

# stringa con valutazione di espressionoi matematiche
print(eval("15 * (4-2) ** 2 +1"))

# operatori utilizzati sulle stringhe
string_sette = "Ciao"
string_otto = "Mondo"
print(string_sette + " " + string_otto)
print(string_sette * 3) # si possono usare operatori matematici sulle stringhe

#alcuni metodi e funzioni utilizzabili sulle stringhe
print(len(string_uno)) # ritorna il numero di caratteri di cui è composta la stringa
print(string_uno.find("i")) #ritorna la prma posizione nella stringa del valore cercato. -1 se assente
print(f"L'indice della prima i nella stringa è {string_uno.find('i')}")
string_uno.replace("o", "*")
print(string_uno) # anche le stringhe come i numeri sono immutabili
string_uno = string_uno.replace("o","*")
print(string_uno)

#slicing su stringhe
stringa_lunga = "supercalifragilistichespiralidoso"
print(stringa_lunga[2:9]) # stampa solo caratteri da indice 2 (compreso) a 9 (escluso)
print(stringa_lunga[3:]) # stampa solo caratteri da indice 3 (compreso) fino alla fine
print(stringa_lunga[:5]) #stampa solo caratteri da inizio stringa fino a indice 5 (escluso)
print(stringa_lunga[3]) #stampa carattere ad un determinato indice della stringa
stringa_minore = stringa_lunga[:6]
print(stringa_minore)
print(stringa_lunga[-4:]) # l'indice -1 è in automatico l'ultimo della stringa. E via dicendo da -2 a scendere
print(stringa_lunga[::2]) # solo caratteri con indice di posizione pari. (Primo : tutta stringra, secondo : il passo)
print(stringa_lunga[1::2]) # analogamente per i caratteri con indice di posizione dispari
print(stringa_lunga[::-1]) # stampa tutta la stringa partendo dal valore con indice ultimo