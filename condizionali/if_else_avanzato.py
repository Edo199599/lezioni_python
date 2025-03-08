# costanti per confronto credenziali
USERNAME = "Laura"
PASSWORD = "abc"

# recupero credenziali di accesso mediante input utente
username = input("Digita username: ")
password = input("Digita password: ")

# controllo login
if username == USERNAME and password == PASSWORD:
    print("Benvenuto nella tua area riservata")
else:
    print("Credenziali errate")