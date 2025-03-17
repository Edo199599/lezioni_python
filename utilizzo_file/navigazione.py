import os

#capire come lavora lo script in esecuzione
print(os.getcwd()) # print della current work directory, percorso assoluto del lavoro script attuale
print(os.listdir()) # ritorna una lista con nomi di file e directory nella directory di lavoro


# risalita di 3 livelli
os.chdir("../../../") # change directory. Si usa un ../ per ogni livello da salire
print(os.getcwd())
print(os.listdir())


# ingresso in una directory specifica
os.chdir("pitone")
print(os.getcwd())
print(os.listdir())

# ispezionamento contenuto completo directory di lavoro
for cartella, sottocartelle, files in os.walk(os.getcwd()): #esplora tutte le c. sottoc. e file della direcotry corrente
    print(f"Analizzando la cartella {cartella}, troviamo le sottocartelle {sottocartelle} e i files {files}")