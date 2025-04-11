import threading
import time
from threading import Thread

# riferimento al thread principale
main_thread = threading.main_thread()

# definizione di una funzione target che definisce il compito di un thread secondario
def compito_thread_uno(nome):
    print(f"Salve sono il thread secondario {nome}")

class ThreadDue(threading.Thread):

    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    # ovveride del metodo che ci permette di definire il compito del thread
    def run(self):
        for i in range(1,11):
            time.sleep(1)
            print(f"Sono il thread {self.nome} e stampo il numero {i}")




# ESECUZIONE PROGRAMMA
# avvio programma
print(f"{main_thread.name} ha avviato il programma")

# istanziazione e comunicazione di avvio del thread secondario uno
thread_uno = threading.Thread(target = compito_thread_uno, args=("Mario",))
# il target è la funzione che il thread eseguirà. Senza le () per non eseguirla subito
# args sono gli argomenti che passiamo alla funzione, in questo caso il nome del thread
# usiamo una tupla per passare gli argomenti, anche se sono uno solo
thread_uno.start() # non avvia il thread (Comunichiamo allo scheduler che thread_uno è pronto a partire)
# è l'interprete python e lo scheduler che decidono quando thread_uno comincerà a svolgere il suo compito
# infatti a volte finisce prima il thread principale a stampare il messaggio di chiusura del thread secondario a mettere il \n
thread_uno.join()
# il join serve a far si che il thread principale aspetti la fine del thread secondario.
# così però non ha più senso usare il multi threading perché siamo tornati a lavorare in modo sequenziale


# istanziazione e comunicazione di avvio thread secondario due
thread_due = ThreadDue("Gianni")
thread_due.start()
thread_due.join()

# istanziazione e comunicazione di avvio vari thread secondari
nomi_thread = ["Mario", "Sara", "Pippo", "Pluto"]
vari_thread = [ThreadDue(nome) for nome in nomi_thread]
for thread in vari_thread:
    thread.start()
    thread.join()
    # join fa si che ogni thread venga eseguito uno alla volta


# termine del programma
print(f"{main_thread.name} ha terminato il programma")