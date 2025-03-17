from functools import reduce

# definizione di una lista di numeri interi
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ottenimento di una nuova lista con numeri di quella originale raddoppiati
lista_raddoppiati = list(map(lambda x: x * 2, lista)) # funzione map, primo parametro la funzione lambda e come secondo l'iterabile
print(lista_raddoppiati)

# ottenimento di una nuova lista con numeri dispari di quella originale
lista_dispari = list(filter(lambda x: x%2 != 0, lista)) # a differenza di map, filter filtra secondo una condizione definita da lambda
print(lista_dispari)

# ottenimento del prodotto generale della lista
prodotto = reduce(lambda x,y: x*y, lista) # richiede import ma permette uso di operatori per ottenere valori da una lista
print(prodotto)