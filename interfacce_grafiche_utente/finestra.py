import tkinter as tk
from finestra_due import FinestraDue


# faccio ereditare alla mia classe Finestra la classe Tk di tkinter
# altrenti avrei una classe basica ma senza gli strumenti per creare interfacce grafiche

class Finestra(tk.Tk):

    # schema composizione menu
    schema_menu = {
        "File": ["Apri", "Nuovo", "Salva", "Nuova Finestra"],
        "Edit": ["Seleziona", "Seleziona Tutto"]
        }

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
        # generazione frame contenitore unico
        #self.generazione_contenitore()
        # generazione frame di sezione con riferimento
        self.laterale, self.superiore, self.inferiore, self.centrale = self.generazione_sezioni()
        # generazione componenti all'interno del frame laterale
        self.label, self.entry, self.button, self.label_due = self.generazione_componenti_laterali()
        # configurazione barra menu
        # .config() serve per configurare la finestra a cui passiamo il menu da visualizzare
        self.config(menu=self.generazione_menu())


    # i tasti vengono solitamente creati su un pannello di controllo e questo viene aggiunto alla finestra
    # non vengono messi direttamente sulla finestra
    # METODO: creazione di un frame contenitore
    def generazione_contenitore(self):
        frame = tk.Frame(master=self, background="lightyellow")
        # master serve per specificare il contenitore padre, background serve per specificare il colore di sfondo
        frame.pack(fill=tk.BOTH, expand=True)
        # il metodo pack() serve per posizionare il frame all'interno della finestra
        # fill serve per specificare che il frame deve occupare tutto lo spazio disponibile
        # fill può essere tk.X, tk.Y o tk.BOTH, None se vogliamo che non possa espandersi
        # expand serve per specificare che il frame deve espandersi per occupare tutto lo spazio disponibile

    # metodo per genrare 4 frame contenitori (sezioni di interfaccia)
    def generazione_sezioni(self):
        laterale = tk.Frame(master= self, background="lightblue", width=300)
        superiore = tk.Frame(master= self, background="lightyellow", height=150)
        inferiore = tk.Frame(master= self, background="lightgreen", height=150)
        centrale = tk.Frame(master= self, background="lightgrey")
        # per l'ultimo non specifico dimensioni perché si andrà a prendere quello che resta
        laterale.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        # mettiamo false per evitare che si espanda ma usiamo BOTH per occupare tutto lo spazio disponibile
        superiore.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        inferiore.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
        centrale.pack(fill=tk.BOTH, expand=True)
        return laterale, superiore, inferiore, centrale

    # metodo per la generazione di componenti da inserire nel frame laterale (label - caselle editabili - pulsanti)
    def generazione_componenti_laterali(self):
        # label: ovvero una etichetta che mostra un testo statico
        label = tk.Label(master=self.laterale, text="Testo iniziale di default", background="lightblue",
                         foreground="red", font = "Arial 12 bold")
        # background serve per specificare il colore di sfondo, foreground serve per specificare il colore del testo
        # font serve per specificare il tipo di carattere, la dimensione e lo stile (bold, italic, underline)
        # per il colore del font lo inseriamo come foreground
        # label.pack()
        label.bind("<Button-2>", self.ripristino_testo)
        # .bind() serve per associare un evento ad un metodo
        # il primo parametro è l'evento da associare (Button-2 = tasto destro), il secondo è il metodo da invocare (senza ())
        # Su Windows il tasto destro è Button-3
        label.place(x=50, y=30, width= 200, height=25)
        # casella editabile: ovvero una casella di testo in cui l'utente può inserire del testo
        entry = tk.Entry(master=self.laterale, background="white", font = "Arial 12", foreground="black")
        # entry.pack()
        entry.bind("<Key>", self.recupero_testo)
        entry.place(x=50, y=65, width=200, height=25)
        # il .pack() serve per posizionare il widget all'interno del frame
        # pulsante cliccabile
        button = tk.Button(master=self.laterale, text="Cliccami", background="white", foreground="black",
                           font= "Arial 12 bold", cursor="hand2", command=self.modifica_testo)
        # cursor serve per specificare il tipo di cursore da visualizzare quando si passa sopra il pulsante
        # opzioni per cursor sono "hand2", "cross", "circle", "plus", "arrow", "xterm"
        # command serve per specificare il metodo da invocare quando si preme il pulsante
        # non mettiamo le parentesi perché non vogliamo invocare il metodo ma passarlo come riferimento da invocare
        # button.pack()
        button.place(x=100, y=100, width=100, height=25)
        # ulteriore label di output
        label_due = tk.Label(master=self.laterale, background="lightblue", font="Arial 12 bold")
        label_due.place(x=50, y=140, width=200, height=25)
        # esternalizzazione degli oggetti
        return label, entry, button, label_due
    # elimino i pack perché hanno ridimensionato il frame laterale in base alla grandezza dei widget (COSA NON VOLUTA)

    # metodo di logica attivato al click del pulsante
    def modifica_testo(self):
        # il metodo viene invocato quando il pulsante viene premuto
        # .get() serve per ottenere il testo inserito nella casella editabile
        # che viene sovrascritto nella label al posto di text
        self.label["text"] = self.entry.get()
        # delete() serve per eliminare il testo inserito nella casella editabile
        # il primo parametro serve per specificare la posizione del primo carattere da eliminare
        # il secondo parametro serve per specificare la posizione dell'ultimo carattere da eliminare
        self.entry.delete(0, tk.END)

    # metodo di logica attivato al click mouse dx sulla label stessa
    def ripristino_testo(self, event):
        # il metodo viene invocato quando si preme il tasto destro del mouse sulla label
        # event serve per specificare l'evento che ha scatenato il metodo
        # in questo caso il click del mouse destro sulla label
        self.label["text"] = "Testo iniziale di default"
        self.label_due["text"] = "" # ripristino label_due a stato originale
        # print(event)
        # ripristino del testo iniziale

    # metodo di logica attivato alla digitazione nella casella di input
    def recupero_testo(self, event):
        # il metodo viene invocato quando si digita un carattere nella casella editabile
        # event serve per specificare l'evento che ha scatenato il metodo
        if event.keysym != "BackSpace":
            # in questo caso la digitazione di un carattere nella casella editabile
            self.label_due["text"] += event.char
            # il metodo char serve per ottenere il carattere digitato
            # e viene aggiunto alla label_due
        else:
            # se uso il backspace mi mantiene tutto il testo tranne l'ultimo carattere (eliminato)
            self.label_due["text"] = self.label_due["text"][:-1]

    # metodo per generazione e popolamento del menu
    def generazione_menu(self):
        # creazione menu
        barra_menu = tk.Menu(master=self)
        # la barra dei menu non viene agganciata a un frame ma alla finestra principale
        # generazione item principali
        for nome_item, lista_nomi_sottoitem in Finestra.schema_menu.items():
            item_menu = tk.Menu(master=barra_menu, tearoff=0)
            # tearoff serve per specificare se il menu deve essere staccabile o meno. 0 significa che non è staccabile
            # di default è 1 e il menu può essere staccato (EVITA)
            barra_menu.add_cascade(label=nome_item, menu=item_menu)
            # generazione sottoitem
            for nome_sottoitem in lista_nomi_sottoitem:
                # item_menu.add_command(label=nome_sottoitem, command=self.gestione_menu)
                # non posso passare gestione_menu senza parentesi perché non potrei darci il comando che richiede
                # ma non posso passarlo nemmeno con le parentesi per evitare che venga invocato subito
                # quindi creo una lambda che mi permette di passare il comando
                item_menu.add_command(label=nome_sottoitem, command= lambda c=nome_sottoitem: self.gestione_menu(c))
        return barra_menu

    # metodo di logica per gestione generale dei comandi menu
    def gestione_menu(self, comando):
        # print(comando)
        if comando == "Nuova Finestra": # apertura finestra secondaria
            FinestraDue(self)
            # avendole messe come principale e secondaria, se chiudo la principale chiudo anche la secondaria


# istruzione di avvio
# costruiamo un oggetto di tipo Finestra senza passargli nulla
# gli invochiamo il metodo mainloop() che lo rende visibile e interattivo
Finestra().mainloop()
# il codice ora non è più sequenziale ma a eventi
# ovvero ci sono eventi che scatenano delle azioni e non più una sequenza di istruzioni
