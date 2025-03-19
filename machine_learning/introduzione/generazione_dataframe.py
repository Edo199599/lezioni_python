import pandas as pd
# convenzione importare intera libreria e gli si assegna un alias

# dichiarazione di 2 liste + un dizionario di inclusione
nomi = ["Mario", "Gianni", "Laura", "Sara"]
eta = [50, 32, 24, 18]
utenti = {"nome":nomi, "eta":eta}

# creazione del DataFrame mediante dizionario
df_uno = pd.DataFrame(utenti)
print("DataFrame Uno: ", df_uno, sep="\n") # premere il pallino rosso è un breakpoint, interrompe l'esecuzione qui per testare


# generazione dataframe mediante liste con iterazione (list comprehension) MENO USATA, PIù SCOMODA
df_due = pd.DataFrame([[nomi[i], eta[i]] for i in range(len(nomi))], columns=["nome", "eta"])
print("DataFrame Due: ", df_due, sep="\n")


# generazione dataframe mediante liste (con trasposizione)
# df_tre = pd.DataFrame([nomi, eta])
# print("DataFrame Tre: ", df_tre, sep="\n") # ha creato una colonna (non riga) per ogni elemento e gli attributi sono diventati le righe

df_tre = pd.DataFrame([nomi, eta]).T # il punto t sta per transpose, trasforma le colonne in righe e viceversa
df_tre.columns = ["nome", "eta"] # assegna i nomi alle colonne (intestazione)
print("DataFrame Tre: ", df_tre, sep="\n")

#generazione dataframe mediante file csv (con intestazione originale)
df_quattro = pd.read_csv("../dataset/data_01.csv")
print("DataFrame Quattro: ", df_quattro, sep="\n")

# generazione dataframe mediante file csv (con intestazione personalizzata)
df_cinque = pd.read_csv("../dataset/data_01.csv", skiprows=1, names=["i", "n", "c", "u", "p"]) # skiprows salta la prima riga, names assegna i nomi alle colonne
#names e columns sono sinonimi ma rispettivamente per read_csv e per DataFrame

print("DataFrame Cinque: ", df_cinque, sep="\n")

# generazione dataframe mediante file json (con intestazione originale)
# json = JavaScript Object Notation (formato per database non relazionali) - formato più comune in ambiente web
# array json = lista in python, oggetto json = dizionario in python
# formato facile da creare, facile da leggere per ogni linguaggio.
# più leggero il file a parità di informazioni rispetto al csv (per questo usato in ambito web)
# in ambito dati per dataset però csv è più usato (formato già tabellare)
# ES: csv lo rivedremo in SQL, json lo rivedremo in NoSQL
df_sei = pd.read_json("../dataset/data_02.json")
print("DataFrame Sei: ", df_sei, sep="\n")

# generazione dataframe mediante file json (con intestazione personalizzata)
df_sette = pd.read_json("../dataset/data_02.json")
df_sette.columns = ["i", "n", "c", "u", "p"] # assegna i nomi alle colonne
df_sette.rename(columns={"p":"psw"}, inplace=True) # rinomina la colonna p in password. inplace=True modifica il dataframe originale
print("DataFrameSette: ", df_sette, sep="\n")