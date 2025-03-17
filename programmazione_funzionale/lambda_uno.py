# lista di contenuti
lista = ["Buongiorno", "Buonasera", "Buonanotte"]


# funzione di filtro per stampare contenudi con più di 9 caratteri
def filtro_lunghezza():
    for saluto in lista:
        if len(saluto) > 9:
            print(saluto)

# funzione di filtro per stampare contenuti che terminano con "a"
def filtro_terminale():
    for saluto in lista:
        if saluto.endswith("a"):
            print(saluto)

# funzione di filtro generica
def filtro_generico(filtro): # il parametro filtro sarà a sua volta una funzione
    for saluto in lista:
        if filtro(saluto):
            print(saluto)


# filtro_lunghezza()
# filtro_terminale()

filtro_generico(lambda x: len(x) > 9)
filtro_generico(lambda x: x.endswith("a"))