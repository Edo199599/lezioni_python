from datetime import datetime

# definizione classe di modellazione oggetto Prenotazione
# mediante pattern di composizione -> Prenotazione ha un Cliente e ha una Camera
class Prenotazione:

    # metodo di inizializzazione
    def __init__(self, data_arrivo, data_partenza, cliente, camera):
        # non segno anche il costo o il nome del cliente perchè ci accederò dagli oggetti cliente e camera
        self.data_arrivo = datetime.strptime(data_arrivo, "%d-%m-%Y").date() # minuscola = 2 cifre, maiuscola = 4 cifre
        self.data_partenza = datetime.strptime(data_partenza, "%d-%m-%Y").date()
        self.cliente = cliente
        self.camera = camera
        self.importo = self.calcolo_importo()

    # metodo di istanza per logica di calcolo importo
    def calcolo_importo(self):
        differenza_notti = (self.data_partenza - self.data_arrivo).days # .days calcola automaticamente coi formati data
        importo = differenza_notti * self.camera.tariffa_notte # prende in automatico la caratteristica da camera.py
        return round(importo, 2)

    # metodo di istanza per la rappresentazione testuale
    def __repr__(self):
        return (f"Prenotazione dal: {self.data_arrivo.strftime('%d-%m-%Y')} "
                f"al: {self.data_partenza.strftime('%d-%m-%Y')}\n{self.camera}\n{self.cliente}\n"
                f"Totale Soggiorno: {self.importo} €")

