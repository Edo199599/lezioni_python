from object_oriented.composizione.model.camera import Camera
from object_oriented.composizione.model.cliente import Cliente
from object_oriented.composizione.model.prenotazione import Prenotazione


# funzione per creare una camera
def creazione_camera():
    return Camera(103, "Matrimoniale", 89.55)

# funzione per registrare un cliente
def registrazione_cliente():
    nome = input("Inserire nome cliente >>> ")
    cognome = input("Inserire cognome cliente >>> ")
    cliente = Cliente(nome, cognome)
    print(f"{cliente} registrato con successo!")
    return cliente

# funzione per registrate una prenotazione
def registrazione_prenotazione():
    # ottenimento camera (unica disponibile)
    camera = creazione_camera()
    #arriva la telefonata del Cliente
    cliente = registrazione_cliente()
    data_arrivo = input("Inserire data di arrivo in formato gg-mm-aaaa >>> ")
    data_partenza = input("Inserire data di partenza in formato gg-mm-aaaa >>> ")
    # registrazione della prenotazione
    prenotazione = Prenotazione(data_arrivo, data_partenza, cliente, camera)
    print(prenotazione, "Registrata con successo!", sep = "\n")


# invocazione funzione di avvio
registrazione_prenotazione()