import tkinter as tk

# faccio ereditare alla mia classe Finestra la classe Tk di tkinter
# altrenti avrei una classe basica ma senza gli strumenti per creare interfacce grafiche

class Finestra(tk.Tk):

    # metodo di inizializzazione
    def __init__(self):
        super().__init__()
        # anche se non passeremo nulla a questo invocatore è obbligatorio inserirlo
        self.title("Finestra Programma")
        # dimensionamento e posizionamento fisso (dimensione in px come x e y partendo dall'angolo superiore sinistro)
        self.geometry("600x600+300+50") # largh x Alt + dist. da sx + dist. da alto
        # il metodo geometry() accetta una stringa che contiene la dimensione della finestra.
        # il posizionamento poi si inserisce come +x+y (rischia di dare problemi su schermi con poca definizione)
        # dimensionamento fisso e posizionamento dinamico al centro dello schermo
        self.geometry(f"600x600+{(self.winfo_screenwidth() - 600) // 2}+{(self.winfo_screenheight() - 600) // 2}")
        # estensione a tutto schermo già al momento del run
        self.state("zoomed")

# istruzione di avvio
# costruiamo un oggetto di tipo Finestra senza passargli nulla
# gli invochiamo il metodo mainloop() che lo rende visibile e interattivo
Finestra().mainloop()
# il codice ora non è più sequenziale ma a eventi
# ovvero ci sono eventi che scatenano delle azioni e non più una sequenza di istruzioni
