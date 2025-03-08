# acquisizione età utente in input
eta = input("Digita la tua età: ")

# controllo dato in input
if eta.isnumeric():
    eta = int(eta)
    print("Sei maggiorenne" if eta >= 18 else "Sei minorenne")
    messaggio = "Sei maggiorenne" if eta >= 18 else "Sei minorenne"
    print(messaggio)