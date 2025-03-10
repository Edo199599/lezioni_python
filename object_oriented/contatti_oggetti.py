# classe di modellazione oggetti di tipo contatto

class Contatto:

    #attributo di classe per collezionamento contatti
    contatti = []

    # metodo di inizializzazione
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        Contatto.contatti.append(self) # aggiungo l'oggetto appena costruito direttamente alla lista contatti creata

    # metodo di rappresentazione testuale
    def __repr__(self): #funziona sia per liste che per oggetti singoli il __repr__
        return f"CONTATTO\nNome: {self.nome}\nCognome: {self.cognome}\n------------------------"


# SEZIONE OPERATIVA

# acquisizione input utente
for _ in range(2):
    n = input("Inserire nome contatto >>> ")
    c = input("inserire cognome contatto >>> ")
    Contatto(n ,c)

# lettura dei dati registrati
for contatto in Contatto.contatti:
    print(contatto)