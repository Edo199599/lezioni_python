# acquisizione input utente
genere = input("Difita F per femmina o M per maschio >>> ")

bastardo = True
while bastardo:
    if genere.upper() == "F":
        print("Benvenuta!")
        bastardo = False
        break
    elif genere.upper() == "M":
        print("Benvenuto!")
        bastardo = False
        break
    elif not genere: #perchè se non si mette nulla in input a stringa vuota viene assegnato il booleano False
        print("Non hai digitato nulla")
    else:
        print("Inserisci un valore accettato (M/F)")
    genere = input("Difita F per femmina o M per maschio >>> ")
