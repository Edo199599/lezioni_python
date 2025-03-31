import tkinter as tk
from tkinter import ttk # importo il modulo ttk per le combobox
from calendar import month_name

class FinestraDue(tk.Toplevel):
    # TopLevel è una finestra secondaria che viene aperta sopra la finestra principale
    # la classe Toplevel è una sottoclasse di Tk
    # se avessi usato solo Tk avrei creato una finestra principale

    def __init__(self, principale):
        super().__init__(master=principale)
        # l'inserimento dei due principali specifica che questa è una finestra secondaria
        # che discende da quella principale
        self.title("Finestra Secondaria")
        self.geometry(f"400x400+{(principale.winfo_width() - 400) // 2}+{(principale.winfo_height() - 400) // 2}")
        self.contenitore = self.generazione_contenitore()
        # gestione del check singolo
        self.controllo_check_singolo = tk.BooleanVar()
        self.check_singolo = self.generazione_check_singolo()
        self.schema_check_multipli = {
            "Cinema": tk.BooleanVar(),
            "Musica": tk.BooleanVar(),
            "Teatro": tk.BooleanVar()
        }
        self.check_multipli = self.generazione_check_multipli(60)
        # gestione radio button
        self.controllo_genere = tk.StringVar()
        self.controllo_genere.set("Uomo") # valore di default
        self.generazione_radio_button()
        # gestione combobox
        self.combobox = self.generazione_combobox()

    # metodo per generazione di frame contenitore
    def generazione_contenitore(self):
        # creazione di un frame contenitore
        frame = tk.Frame(master=self)
        frame.pack(expand=True, fill=tk.BOTH)
        return frame

    # metodo per la generazione di un singolo check
    def generazione_check_singolo(self):
        check = tk.Checkbutton(master=self.contenitore, text="Accetta La Privacy",
                               command=self.selezione_check_singolo, variable=self.controllo_check_singolo)
        # aggiungo variabile di controllo al check tracciando il suo stato con un booleano (definito in __init__)
        check.place(x = 20, y = 20, width = 200, height = 25)
        return check

    # metodo di logica invocato a selezione/deselezione del check singolo
    def selezione_check_singolo(self):
        print("Azione registrata sul check singolo")
        if self.controllo_check_singolo.get(): # true
            print("Check singolo selezionato")
        else: # false
            print("Check singolo deselezionato")

    # metodo per la generazione di check multipli
    def generazione_check_multipli(self, posizione_y):
        lista_check = []
        for testo, variabile in self.schema_check_multipli.items():
            check = tk.Checkbutton(master=self.contenitore, text = testo, variable = variabile)
            check.place(x = 20, y = posizione_y, width = 200, height = 25)
            posizione_y += 25
            lista_check.append((check, variabile)) # aggiungo una tupla con check e variabile alla lista
        # pulsante di servizio (per generare l'evento)
        button = tk.Button(master=self.contenitore, text="Invia", command=self.recupero_stati_check_multipli)
        button.place(x = 20, y = 140, width = 100, height = 25)
        return lista_check

    # metodo di logica invocato a selezione/deselezione del check multipli (recupero preferenze)
    def recupero_stati_check_multipli(self):
        preferenze_utente = []
        for check, variabile_controllo in self.check_multipli:
            if variabile_controllo.get():
                preferenze_utente.append(check["text"]) # recupera il testo del check
        print(preferenze_utente)

    # metodo per generazione di 2 radio button (uomo/donna)
    def generazione_radio_button(self):
        radio_uomo = tk.Radiobutton(master=self.contenitore, text="Uomo", value="Uomo", variable=self.controllo_genere)
        # passando il parametro value si fa si che i due tasti possano assumere una sola selezione
        radio_uomo.place(x = 20, y = 180, width = 200, height = 25)
        radio_donna = tk.Radiobutton(master=self.contenitore, text="Donna", value="Donna", variable=self.controllo_genere)
        radio_donna.place(x=20, y=205, width=200, height=25)
        # pulsante di servizio (per generare l'evento)
        button = tk.Button(master=self.contenitore, text="Invia", command=self.recupero_selezione_radio)
        button.place(x=20, y=240, width=100, height=25)

    # metodo di logica invocato al click sul button di servizio dei radio (recupero genere utente)
    def recupero_selezione_radio(self):
        print(f"L'utente è {self.controllo_genere.get()}")

    # metodo per generazione combobox (select in ambito web)
    def generazione_combobox(self):
        lista_mesi = [month_name[mese] for mese in range(1,13)] # lista dei 12 mesi
        combo = ttk.Combobox(master=self.contenitore, state="readonly", values=lista_mesi)
        combo.set("Seleziona un mese") # intestazione del combobox
        # a state vuoto la combobox è editabile, mentre a state="readonly" non lo è
        combo.bind("<<ComboboxSelected>>", self.selezione_item_combo)
        # ComboboxSelected è l'evento che viene generato quando l'utente seleziona un item
        # il binding permette di associare un evento ad un metodo
        # event si usa solo per eventi non ordinari (non click su pulsanti)
        combo.place(x=20, y=290, width=200, height=25)
        # pulsante di servizio (per generare l'evento)
        button = tk.Button(master=self.contenitore, text="Invia", command=self.controllo_item_combo)
        button.place(x=20, y=320, width=100, height=25)
        return combo

    # metodo di logica attivato alla selezione di ogni item del combobox
    def selezione_item_combo(self, event):
        print(f"Selezionato il mese {self.combobox.get()}")

    # metodo di logica attivato al click sul button di servizio del combobox (recupero mese selezionato)
    def controllo_item_combo(self):
        print(f"L'utente è nato nel mese di {self.combobox.get()}")


