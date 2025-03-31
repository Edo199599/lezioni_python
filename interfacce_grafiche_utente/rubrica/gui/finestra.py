import tkinter as tk
from interfacce_grafiche_utente.rubrica.repository.contatto_repository import *
from tkinter import ttk
from tkinter.messagebox import askyesno

class Finestra(tk.Tk):

    # metodo di inizializzazione
    def __init__(self):
        super().__init__()
        self.title("Applicazione Rubrica")
        self.geometry(f"600x600+{(self.winfo_screenwidth() - 600) // 2}+{(self.winfo_screenheight() - 600) // 2}")
        self.frame = self.generazione_frame() # riferimento al contenitore
        self.tabella = self.generazione_tabella()
        self.popolamento_tabella() # invocazione metodo popolamento alla creazione della tabella
        self.config(menu=self.generazione_menu()) # aggiunta della barra menu alla finestra

    # creazione del frame principale
    def generazione_frame(self):
        frame = tk.Frame(master=self)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame

    # metodo per generazione tabella visualizzazione dati
    def generazione_tabella(self):
        # definire una scrollbar verticale (nel caso il numero di contatti ecceda i 660x600)
        scroll = tk.Scrollbar(master=self.frame)
        scroll.pack(side=tk.RIGHT, expand=tk.Y) # si espande solo nella direzione Y e non nella X
        # tabella di visualizzazione e il setting della scrollbar
        tabella = ttk.Treeview(master=self.frame, yscrollcommand=scroll.set, columns=("nome", "cognome", "telefono"))
        # yscrollcommand serve per collegare la scrollbar alla tabella
        # scroll.set() serve per settare che sarà la scrollbar a scorrere la tabella
        # columns assegna gli identificatori delle colonne
        tabella.pack(fill=tk.Y, expand=True)
        scroll.config(command=tabella.yview)
        # configuro la scrollbar per la tabella
        # deve esserci una doppia associazione tra la scrollbar e la tabella (in un verso e nell'altro)
        # definizione colonne (struttura generale della tabella)
        tabella.column("#0", width=0, stretch=tk.NO) # la prima colonna deve essere impostata così
        # la TreeView genera le righe e ci assegna un identificatore particolare (assegnato nella colonna #0)
        # per non visualizzarla la larghezza è 0 e non si può espandere (tramite trascinamento del mouse)
        tabella.column("nome", width=200, stretch=tk.NO)
        tabella.column("cognome", width=200, stretch=tk.NO)
        tabella.column("telefono", width=170, stretch=tk.NO, anchor=tk.CENTER)
        # la scrollbar è associata alla colonna telefono e prende quegli ultimi 30 pixel
        #impostazione headers tabella
        tabella.heading("#0", text="") # colonna invisibile con stringa vuota
        tabella.heading("nome", text="Nome Contatto")
        tabella.heading("cognome", text="Cognome Contatto")
        tabella.heading("telefono", text="Telefono Contatto")
        # stilizzazione header tabella
        style = ttk.Style(master=self) # creo un oggetto stile che per quanto invisibile devo agganciare alla finestra
        style.theme_use("default") # tema di default
        style.configure("Treeview.heading", background="lightgray")
        return tabella

    # metodo di logica per il popolamento tabella
    def popolamento_tabella(self):
        # reset della tabella (per evitare che ad ogni ciclo si creino duplicati)
        for riga in self.tabella.get_children(): # tutti i figli della tabella ovvero tutte le righe
            self.tabella.delete(riga)
        # ottenimento lista contatto dal file e conversione da Contatto a list
        lista_contatti = elenco_contatti_repo() # lista di oggetti Contatto
        righe = [contatto.lista_attributi() for contatto in lista_contatti] # lista di liste
        # popolamento tabella
        for riga in righe:
            self.tabella.insert(parent="", index="end", values=riga)
            # parent="" serve per indicare che non ci sono righe genitore
            # index="end" serve per indicare che la riga deve essere inserita in fondo
            # values=riga serve per indicare i valori da inserire

    # metodo per generazione barra menu
    def generazione_menu(self):
        barra = tk.Menu(master=self) # non la colleghiamo alla finestra ma al frame principale
        item = tk.Menu(master=barra, tearoff=0)
        item.add_command(label="Nuovo", command=self.aggiunta_contatto)
        item.add_command(label="Elimina", command=self.elimina_contatto)
        barra.add_cascade(label="File", menu=item)
        return barra

    # metodo di logica per aggiunta contatto (dovrà aprire una finestra secondaria)
    def aggiunta_contatto(self):
        pass

    # metodo di logica per eliminazione contatto con conferma utente
    def elimina_contatto(self):
        # print(self.tabella.selection()) # ottengo il codice identificativo dell'elemento selezionato
        if self.tabella.selection():
            riga_selezionata = self.tabella.item(self.tabella.selection()[0], "values")
            # trova l'indice della riga selezionata e restituisce il valore dell'item
            print(riga_selezionata)
            conferma = askyesno(title="CONFERMA ELIMINAZINE",
                                message=f"Sei sicuro di voler eliminare il contatto {riga_selezionata[1]}?", parent=self)
            # essendo un dialogue deve essere associato alla finestra da cui è stato aperto
            # askyesno ritorna True o False
            if conferma:
                # eliminazione contatto
                print("Contatto eliminato")


