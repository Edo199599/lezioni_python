import os
import shutil


# creazione di una directory nella directory di lavoro corrente
os.makedirs("cartella", exist_ok=True) #dopo la prima run da errore essendoci già, con quel exist permetto nel caso di ignorare il comando

# creazione di una struttura di directory annidate
os.makedirs("Cartella2/sottocartella", exist_ok=True)

# creazione di un file di sottodirectory "sottocartella"
open("cartella2/sottocartella/file.txt", "w")
# primo parametro: percorso assoluto o relativo fino al file + nome del file da creare con estensione
# secondo parametro, modo in cui fare operare la funzione open. DI DEFAULT LAVORA IN LETTURA
# passiamo il carattere "w" per far capire che se il file non c'è lo si crea da WRITE e lo apre

# rinomina directory
# os.rename("cartella", "nuova_cartella") la commento perché dal secondo ciclo darebbe errore

# copia di singoli elementi o intere strutture (import shutil)
# shutil.copytree("cartella2", "copia") # file da copiare e nome del recipiente in cui copiare
# si crea una nuova struttura chiamata copia che è la copia della directory
# anche questo commentato perché al secondo ciclo la cartella copia esiste già

# metodi di interrogazione
print(os.path.exists("copia")) #ritorna vero se la cosa ricercata esiste
print(os.path.isdir("nuova_cartella")) # ritorna True se l'elemento è una directory, False se file o non esistente
print(os.path.isfile("cartella2/sottocartella/file.txt")) # True se file


# cancellazione di file, directory e strutture
# os.remove("copia/sottocartella/file.txt") # rimozione file sempre possibile se esiste
# os.rmdir("nuova_cartella") # rimozione directory nuova sempre possibile
# os.rmdir("copia") # la rimozione di una directory non vuota non è possibile con questa funzione
# os.removedirs("copia") # specifico per la rimozione di strutture ma da comunque errore se non specifico altro che il nome
# os.removedirs("copia/sottocartella") # rimozione struttura directory senza file eliminando l'intero percorso scritto
shutil.rmtree("cartella2") # questa funzione elimina tutto senza preoccuparsi di cosa ci sia dentro

