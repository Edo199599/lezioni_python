# definizione di una classe per modellazione oggetti smartphone

# convenzine Pascal Case per i nomi (Inizio con maiuscola e nuove parole con nuova maiuscola non _)
# le classi inoltre nella convenzione non hanno mai nomi al plurale
class Smartphone:

    # attributo di classe -> raggruppamento oggetti smartphone
    catalogo = [] # al di fuori della costruzione degli oggetti per renderla indipendente da un self ma legato alla classe


    # metodo di inizializzazione -> serve per deinire struttura degli oggetti e costruirli
    #  il self è un riferimento diretto all'oggetto che stiamo costruendo (this in altri linguaggi)
    def __init__(self, marca=None, modello=None, dimensioni_display=None, prezzo=None): #do valori iniziali (leggi riga 70)
        self.marca = marca # valorizza la proprietà .marca con il valore marca ricevuto in costruzione
        self.modello = modello
        self.dimensione_display = dimensioni_display
        self.prezzo = prezzo

    # metodo di istanza -> funzionalità di invio chiamata
    def invio_chiamata(self, numero): # self viene messo di default perché sarà sempre associato all'oggetto
        print(f"Sono un {self.marca} e chiamo il numero {numero}")

    # metodo di istanza -> funzionalità di invio messaggio
    def invio_messaggio(self, destinatario):
        print(f"Sono un {self.marca} ({self.modello}) e invio un messaggio a {destinatario}")

    # metodo di istanza -> funzionalità di rappresentazione testuale (riscritto da metodo esistente)
    # creo questo metodo per far si che gli oggetti smartphone possano descriversi anche via testo più completo
    def __str__(self): # il simbolino vicino dice che il metodo viene da un ambiente superiore riadattato
        return f"{self.marca} ({self.modello}) - display da {self.dimensione_display} pollici - prezzo {self.prezzo}€"

    # metodo di istanza -> funzionalità di rappresentazione testuale in struttura (riscritto)
    def __repr__(self): # da una descrizione testuale migliore nella lista catalogo quando viene stampata
        return f"{self.marca} ({self.modello}) - display da {self.dimensione_display} pollici - prezzo {self.prezzo}€"

    # metodo di classe -> popolamento catalogo
    @classmethod # decoratore che definisce che il metodo seguente è di classe e non come prima di istanza
    def popolamento_catalogo(cls, *args): # il cls che sta per class permette di accedere direttamente alla classe
        for smartphone in args: # tutti gli smarthpone che passo quando definisco i valori al posto di args
            cls.catalogo.append(smartphone) #cls.catalogo per prendere la variabile di classe catalogo[] inizializzata prima



# SEZIONE NON PARTE DELLA CLASSE SMARTPHONE
#SCRIPT
#dichiarazione e istanziazione di 3 variabili a cui assegnare 3 oggetti di tipo Smartphone (3 istanze della classe Smartphone)
smart_uno = Smartphone("NOKIA", "3310", 5.57, 200.68)
smart_due = Smartphone("iPhone", "16 Pro Max", 6.7, 1799)
smart_tre = Smartphone("LG", "A56", 6.6, 589)

print(smart_uno, type(smart_uno)) # ti dice essere oggetto istanza della classe Smartphone definito da __init__
print(smart_due, type(smart_due)) # ad inizio riga invece dice che è un oggetto e assegna una stringa di riferimento
print(smart_tre, type(smart_tre))

# accesso in lettura agli attributi dei vari smartphone
print(smart_uno.prezzo)

#accesso in scrittura dei varti Smartphone
smart_uno.prezzo = 300.55 # ho modificato il valore prezzo dell'oggetto smar_uno
print(smart_uno.prezzo)

# invocazione metodi di istanza (azioni di ciascun Smartphone)
smart_uno.invio_chiamata("+39 3312955350")
smart_due.invio_messaggio("Mario")

Smartphone.popolamento_catalogo(smart_uno, smart_due, smart_tre)
print(Smartphone.catalogo)

#dichiarazione e istanziazione di altri due smartphone senza conoscenza dei valori di alcuni attributi
smart_quattro = Smartphone() # richiede 4 elementi. Senza nulla scritto nelle parentesi da errore
#vado ad assegnare ai valore in __init__ valori iniziali
print(smart_quattro) #stampa infatti i None al posto dei valori
smart_quattro.prezzo = 578
print(smart_quattro) # il prezzo ora è stato sostituito al none

smart_cinque = Smartphone(dimensioni_display=6.45) # posso evitare l'assegnazione se sto definendo solo il primo valore
print(smart_cinque) # tutto il resto è None
