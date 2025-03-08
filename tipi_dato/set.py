# dichiarazione e istanziazione set (struttura mutabile)

# set_uno = {1, "ciao", True, (1,2,3), [1, 2, 3]} i set non possono contenere elementi mutabili (come le listi)
set_due = {1, "ciao", True, (1,2,3)}
print(set_due, type(set_due))
# perde il concetto di ordinamento
# cancella True perché 1 ha valore intrinsecamente True. E non ammette duplicati

set_tre = set([1, 3, 3, 4, 4, 2])
print(set_tre, type(set_tre))
# tolti i duplicati  e ordina in maniera naturale i numeri

# set vuoto
set_vuoto_uno = set()
print(set_vuoto_uno, type(set_vuoto_uno)) #con costruttore crea un set vuoto
set_vuoto_due = {}  # i set non hanno assegnazioni literal. Crei un dizionario in questo modo
print(set_vuoto_due, type(set_vuoto_due))

# aggiunte e rimozioni di elementi di un set
set_vuoto_uno.add(34) # .appen e .insert non funzionano per i set (bisogna aggiungere solo elementi immutabili)
print(set_vuoto_uno, type(set_vuoto_uno))
set_due.add("ciao")
print(set_due) # istruzione ignorata (non da errore) perché duplicato di elemento già presente
set_due.remove(1) # non sto puntando alla posizione ma all'elemento preciso
print(set_due)
# set_due.remove(1) commentato perché da errore essendo elemento assente dentro il set