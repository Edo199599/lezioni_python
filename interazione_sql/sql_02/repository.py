import pymysql

# funzinoe invocabile al bisogno per ottenere la connessione al db
# non è necessario chiamarla con _ iniziale perché la useremo sia per articolo che per categoria
# non è fatta, come in sql_01 per essere usata solo in questo file
def get_connection():
    return pymysql.connect(
        host = 'localhost', # potremmo anche inserire l'IP come "127.0.0.1"
        port = 3306,
        user = 'root', # standard user per MySQL
        password = '',
        database = 'db_magazzino' # nome del DB
    )
