"""
Realizzare, sfruttando il paradigma Object Oriented e le specifiche del modulo tkinter, un applicativo dotato di
interfaccia grafica che permetta di convertire un valore indicato dall'utente in metri nelle corrispondenti misurel
espresse in pollici e miglia.
Il software dovra anche prevedere una modalita di reset e si raccomanda di prestare particolare attenzione
alla prevenzione di potenziali eccezioni.
"""



import tkinter as tk


class Convertitore(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Convertitore")
        self.geometry(f"800x800+{(self.winfo_screenwidth()-600) // 2}+{(self.winfo_screenheight()-600) // 2}")
        # self.state("zoomed")
        self.frame = self.generazione_contenitore()
        self.label, self.entry, self.button, self.button_reset , self.label_conversione_miglia, self.label_conversione_pollici = self.generazione_elementi()


    def generazione_contenitore(self):
        frame = tk.Frame(master=self, background="grey")
        frame.pack(expand=True, fill=tk.BOTH)
        return frame

    def generazione_elementi(self):
        label = tk.Label(master=self.frame, text="Inserire valore in metri (m) da convertire:", font="Arial 16 bold", background="white", foreground="black", highlightthickness=3)
        # posiziono la label in mezzo alla finestra
        label.place(x=150, y=280, width=500, height=25)
        entry = tk.Entry(master=self.frame, font="Arial 18", background="white", foreground="black", justify="center")
        entry.place(x=150, y=320, width=500, height=30)
        button = tk.Button(master=self.frame, text="Converti", font="Arial 18 bold", background="white", foreground="black", command=self.conversione)
        button.place(x=350, y=360, width=100, height=30)
        button_reset = tk.Button(master=self.frame, text="Reset", font="Arial 18 bold", background="white", foreground="black", command=self.reset)
        button_reset.place(x=350, y=550, width=100, height=30)
        label_conversione_pollici = tk.Label(master=self.frame, text="Pollici:", font="Arial 18 bold", background="grey", foreground="black")
        label_conversione_pollici.place(x=330, y=440)
        label_conversione_miglia = tk.Label(master=self.frame, text="Miglia:", font="Arial 18 bold", background="grey", foreground="black")
        label_conversione_miglia.place(x=330, y=470)
        return label, entry, button, label_conversione_miglia, label_conversione_pollici, button_reset


    def conversione(self):
        try:
            valore = float(self.entry.get())
            pollici = valore * 39.37
            miglia = valore / 1609.34
            self.label_conversione_pollici.config(text=f"Pollici: {pollici:.2f}")
            self.label_conversione_miglia.config(text=f"Miglia: {miglia:.5f}")
        except Exception:
            self.label_conversione_pollici.config(text="Pollici: Errore")
            self.label_conversione_miglia.config(text="Miglia: Errore")


    def reset(self):
        self.label_conversione_pollici.config(text="Pollici:")
        self.label_conversione_miglia.config(text="Miglia:")
        self.entry.delete(0, tk.END)









Convertitore().mainloop()

