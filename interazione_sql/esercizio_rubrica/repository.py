import pymysql


# funzione invocabile al bisogno per ottenere la connessione al db
def get_connection():
    return pymysql.connect(
        host='localhost',  # potremmo anche inserire l'IP come "127.0.0.1"
        port=3306,
        user='root',  # standard user per MySQL
        password='',
        database='esercizio_rubrica_base'  # nome del DB
    )