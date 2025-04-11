import pymysql
from model.contatto import Contatto
from model.indirizzo import Indirizzo

class ContattoRepository:

    # ottenimento connessione al bisogno
    def _get_connection(self):
        return pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="esercizio_rubrica_base"
        )

    # registrazione indirizzo e contatto in transazione
    def registrazione_contatto_repo(self, contatto):
        connection = None
        try:
            connection = self._get_connection()
            with connection.cursor() as cursor:
                sql_1 = "INSERT INTO indirizzi (via, civico, cap, comune, provincia) VALUES (%s, %s, %s, %s, %s)"
                valori_1 = (contatto.indirizzo.via, contatto.indirizzo.civico, contatto.indirizzo.cap,
                            contatto.indirizzo.comune, contatto.indirizzo.provincia)
                cursor.execute(sql_1, valori_1)
                contatto.indirizzo.id = cursor.lastrowid
                sql_2 = ("INSERT INTO contatti (nome, cognome, telefono, mail, id_indirizzo) "
                         "VALUES (%s, %s, %s, %s, %s)")
                valori_2 = (contatto.nome, contatto.cognome, contatto.telefono,
                            contatto.mail, contatto.indirizzo.id)
                cursor.execute(sql_2, valori_2)
                connection.commit()
                return "Contatto Registrato"
        except Exception as e:
            print(e)
            if connection and connection.open:
                connection.rollback()
            return "Errore Registrazione"
        finally:
            if connection and connection.open:
                connection.close()

    # ottenimento elenco contatti in join con indirizzi
    def elenco_contatti_repo(self):
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM contatti JOIN indirizzi ON contatti.id_indirizzo=indirizzi.id"
                    cursor.execute(sql)
                    risultato = cursor.fetchall()
                    contatti = []
                    for record in risultato:
                        indirizzo = Indirizzo(id=record[6], via=record[7], civico=record[8], cap=record[9],
                                              comune=record[10], provincia=record[11])
                        contatto = Contatto(id=record[0], nome=record[1], cognome=record[2], telefono=record[3],
                                            mail=record[4], indirizzo=indirizzo)
                        contatti.append(contatto)
                    return contatti
        except Exception as e:
            print(e)
            return "Errore Lettura"