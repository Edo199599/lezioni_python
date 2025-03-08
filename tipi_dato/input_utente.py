
# acquisizione input utente e stoccaggio in variabili
nome = input("Digita il tuo nome >>> ")
cognome = input("Digita il tuo cognome >>> ")
eta = input("Digita la tua età >>> ")

# analisi dati ricevuti
print(nome, type(nome))
print(cognome, type(cognome))
print(eta, type(eta)) # valore str non int

# conversione input età in valore numerico
eta = int(eta)
print(eta, type(eta))

# output finale
if eta == 1:
    print(f"Ti chiami {nome} {cognome} e hai {eta} anno")
else:
    print(f"Ti chiami {nome} {cognome} e hai {eta} anni")

'''
num = False
while num == False:
    eta_vera = input("Inserisci la tua età >>> ")
    eta_vera = int(eta_vera)
    if eta_vera == int(eta_vera):
        num = True
    else:
        print("coglione")
'''