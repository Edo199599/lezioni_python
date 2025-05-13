import requests
# requests è una libreria per effettuare richieste HTTP in Python
# fare richieste HTTP è fondamentale per interagire con le API


# definizione classe di modellazione oggetto logico Post
class Post:

    def __init__(self, id=None, title=None, body=None, userId=None):
        self.id = id
        self.title = title
        self.body = body
        self.userId = userId

    # metodo per la rappresentazione testuale dell'oggetto di tipo Post
    def __repr__(self):
        return f"Post Id: {self.id}\nId Utente: {self.userId}\nTitolo: {self.title}\nContenuto: {self.body}"

    # metodo di deserializzazione (da oggetto json estraiamo le proprietà per creare un oggetto Python di tipo Post)
    @classmethod
    def deserializzazione(cls, json):
        # cls è una variabile che rappresenta la classe stessa
        # json è un dizionario che contiene i dati del post
        return cls(**json)
        # posso scrivere **json per passare tutti i parametri
        # oppure
        # return cls(
        #     id=json.get("id"),
        #     title=json.get("title"),
        #     body=json.get("body"),
        #     userId=json.get("userId")
        # )

    # metodo di serializzazione (da oggetto Python di tipo Post a oggetto json)
    def serializzazione(self):
        # metodo di istanza perché ora lavori sull'oggetto direttamente
        return self.__dict__
        # ogni oggetto python ha nascosto un dizionario che contiene le proprietà dell'oggetto

# funzione per acquisizione dati da un web service
def acquisizione_dati():
    try:
        # invio richiesta e ottenimento risposta
        risposta = requests.get("https://jsonplaceholder.typicode.com/posts")
        # .get perché vogliamo ottenere dati
        # .post se volessimo inviare dati
        print(risposta)
        # analisi dati ricevuti (body - corpo della risposta)
        dati_ricevuti = risposta.json()
        # .json() per convertire la risposta in formato JSON in un oggetto Python
        print(dati_ricevuti, type(dati_ricevuti))
        print(dati_ricevuti[0], type(dati_ricevuti[0]))
        print(dati_ricevuti[0]["title"])
        # trasformazione da lista di dizionari a lista di oggetti Python di tipo Post
        lista_post = [Post.deserializzazione(dato) for dato in dati_ricevuti]
        # list comprehension con dato = post
        for post in lista_post:
            print(post)
    except Exception as e:
        print(e)

# funzione per invio dati ad un web service
def invio_dati():
    # costruzione oggetti Post recuperati da utente
    post = Post(title="Il mio primo post", body="Contenuto del mio post", userId=23)
    # immagino che l'id sia progressimo dove lo voglio inserire e venga creato automaticamente
    try:
        # invio richiesta e ottenimento risposta
        risposta = requests.post("https://jsonplaceholder.typicode.com/posts", post.serializzazione())
        # .post perché vogliamo inviare dati
        print(risposta)
        # otteniamo <Response [201]> perché il post è stato creato. 201 è il codice di stato HTTP per la creazione riuscita
        # analisi contenuto della risposta per capire cosa ci sia dentro l'oggetto Response
        print(risposta.json())
    except Exception as e:
        print(e)


# invocazione della funzione
# acquisizione_dati()
invio_dati()