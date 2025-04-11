from contatto import Contatto
from indirizzo import Indirizzo
from repository import get_connection

def elenco_contatti_rubrica_repo():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM contatti JOIN indirizzi ON indirizzi.id = contatti.id_indirizzo"
                cursor.execute(sql)
                risultato = cursor.fetchall()
                contatti_rubrica = []
                for record in risultato:
                    indirizzo = Indirizzo(id=record[6], via=record[7], civico=record[8], cap=record[9],
                                          comune=record[10], provincia=record[11])
                    contatto = Contatto(id=record[0], nome=record[1], cognome=record[2], telefono=record[3],
                                        mail=record[4], indirizzo=indirizzo)
                    contatti_rubrica.append(contatto)
                return contatti_rubrica
    except Exception as e:
        print(e)
        return None

# funzione di aggiunta contatto (col concetto di transaction = commit/rollback)
def aggiunta_contatto_rubrica_repo(contatto_rubrica):
    connetion = None
    # lo inizializzo a None per vederlo in tutti i blocchi
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql_1 = "INSERT INTO indirizzi (via, civico, cap, comune, provincia) VALUES (%s, %s, %s, %s, %s)"
            valori_1 = contatto_rubrica.indirizzo.via, contatto_rubrica.indirizzo.civico, contatto_rubrica.indirizzo.cap, contatto_rubrica.indirizzo.comune, contatto_rubrica.indirizzo.provincia
            cursor.execute(sql_1, valori_1)
            id_indirizzo = cursor.lastrowid
            sql_2 = "INSERT INTO contatti (nome, cognome, telefono, mail, id_indirizzo) VALUES (%s, %s, %s, %s, %s)"
            valori_2 = contatto_rubrica.nome, contatto_rubrica.cognome, contatto_rubrica.telefono, contatto_rubrica.mail, id_indirizzo
            cursor.execute(sql_2, valori_2)
            connection.commit()
            return cursor.rowcount
    except Exception as e:
        print(e)
        if connetion and connetion.open:
            # se connection non è più none e la connessione è aperta
            connetion.rollback()
            # rollback per annullare le operazioni in caso di errore in un qualunque punto
            return "Errore durante l'inserimento"
    finally:
        # finally per eseguire la chiusura della connessione in ogni caso
        if connetion and connetion.open:
            connetion.close()
