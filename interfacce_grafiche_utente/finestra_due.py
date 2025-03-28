import tkinter as tk

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

    # metodo per generazione di frame contenitore
    def generazione_contenitore(self):
        # creazione di un frame contenitore
        frame = tk.Frame(master=self)
        frame.pack(expand=True, fill=tk.BOTH)
        return frame

