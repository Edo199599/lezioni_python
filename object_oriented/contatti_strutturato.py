 # liste per ospitare i dati
nomi = []
cognomi = []

# acquisiamo gli imput utente per due contatti
for _ in range (2):
    nome = input("Inserire nome contatto >>> ")
    cognome = input("Inserire cognome contatto >>> ")
    nomi.append(nome)
    cognomi.append(cognome)

# lettura dei dati registrati
for indice in range(0, len(nomi)):
    print("CONTATTO")
    print("Nome:", nomi[indice])
    print("Cognome:", cognomi[indice])
    print("----------------------")