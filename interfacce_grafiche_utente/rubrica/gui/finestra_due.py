import tkinter as tk

from interfacce_grafiche_utente.rubrica.model.contatto import Contatto
from interfacce_grafiche_utente.rubrica.repository.contatto_repository import aggiunta_contatto_repo


# definizione classe di modellazione Finestra Secondaria (form)
class FinestraDue(tk.Toplevel):

    def __init__(self, principale):
        super().__init__(master = principale)
        self.principale = principale # riferimento alla finestra principale in tutta la classe
        self.title("Nuovo Contatto")
        # dimensionamento e posizionamento
        posizione_x = principale.winfo_rootx() + ((principale.winfo_width() - 300) // 2)
        posizione_y = principale.winfo_rooty() + ((principale.winfo_height() - 300) // 2)
        self.geometry(f"300x300+{posizione_x}+{posizione_y}")
        # riferimento al frame contenitore
        self.frame = self.generazione_frame()
        self.generazione_label("Nome Contatto: ", 20)
        self.entry_nome = self.generazione_entry(42)
        self.generazione_label("Cognome Contatto: ", 77)
        self.entry_cognome = self.generazione_entry(99)
        self.generazione_label("Telefono Contatto: ", 134)
        self.entry_telefono = self.generazione_entry(156)
        self.generazione_button("Abbandona", 45, 210, False)
        self.generazione_button("Registra", 155, 210, True)
        self.label_errore = self.generazione_label("", 250)

    # metodo per la generazione del frame contenitore (non si aggiungono i componenti alla finestra direttamente)
    def generazione_frame(self):
        frame = tk.Frame(master=self)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame

    # metodo per la generazione label
    def generazione_label(self, testo, posizione_y):
        label = tk.Label(master=self.frame, text=testo, anchor="w") # allineamento a sinistra (anchor), w = west
        label.place(x=50, y=posizione_y, width=200, height=20)
        return label

    # metodo per la generazione entry (caselle editabili)
    def generazione_entry(self, posizione_y):
        entry = tk.Entry(master=self.frame)
        entry.place(x=50, y=posizione_y, width=200, height=20)
        return entry

    # metodo per la generazione del bottone di conferma
    def generazione_button(self, testo, posizione_x, posizione_y, azione):
        bottone = tk.Button(master=self.frame, text=testo, command=lambda a=azione: self.gestione_pulsanti(a))
        bottone.place(x=posizione_x, y=posizione_y, width=100, height=25)
        return bottone

    # metodo di logica per gestione pulsanti
    def gestione_pulsanti(self, azione): # True = registra, False = abbandona
        if not azione:
            self.destroy() # chiude la finestra secondaria
        else:
        # recupero i dati dalle entry
            if self.entry_nome.get() and self.entry_cognome.get() and self.entry_telefono.get():
                # se quindi tutti i campi sono stati compilati
                contatto = Contatto(self.entry_nome.get(), self.entry_cognome.get(), self.entry_telefono.get())
                risultato = aggiunta_contatto_repo(contatto)
                if risultato:
                    self.principale.popolamento_tabella() # aggiorno la tabella della finestra principale
                    self.destroy() # chiudo la finestra secondaria
                else:
                    self.label_errore["text"] = "Errore di registrazione"