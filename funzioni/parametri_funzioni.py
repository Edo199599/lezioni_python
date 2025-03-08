# funzioni che riceve un oggetto immutabile ( ad esempio stringhe e numeri)
def modifica_immutabile(ricevuto):
    ricevuto = "Buonasera"
    print(f"Nella funzione, ricevuto vale {ricevuto}")

# funzioni che riceve un oggetto mutabile (ad esempio una lista)
def modifica_mutabile(ricevuto):
    ricevuto[1] = 50
    print(f"Nella funzione, la lista contiene {ricevuto}")



#INVOCAZIONE FUNZIONI

# gestione immutabile
saluto = "Buongiorno" # assegnamo
print(f"Dopo istanziazione, saluto vale {saluto}") # stampo la variabile assegnata
modifica_immutabile(saluto) # invochiamo la funzione passando la variabile saluto e stampando
print(f"Dopo invocazione funzione, saluto vale {saluto}") # l'oggetto immutabile saluto in memoria non cambia

#gestione mutabile
lista = [12, 10, 15, 78]
print(f"Dopo istanziazione, la lista contiene {lista}")
modifica_mutabile(lista)
print(f"Dopo invocazione, la lista contine {lista}") # l'oggetto mutabile lista in memoria è stato cambiato
