import threading
import time

# funzione target per compito del thread secondario
def archiviazione():
    # archiviazione
    try:
        with open("file.txt", "a") as file:
            file.write("a" * 1_000_000_000)
        print(f"Archiviazione terminata alle {time.time()}")
    except Exception as e:
        print(e)

# stampa di avvio programma
print(f"Avvio programma alle {time.time()}")

# # archiviazione
# try:
#     with open("file.txt", "a") as file:
#         file.write("a" * 1_000_000_000)
# except Exception as e:
#     print(e)
# processo lungo che ti blocca il procedere nel programma
# creo un thread che lo svolga in parallelo mentre tu puoi continuare a lavorare

#istanziazione e comunicazione di avvio del thread secondario
thread_archiviazione = threading.Thread(target=archiviazione)
thread_archiviazione.start()


# liberazione programma
print("Adesso procedi con la prossima operazione")