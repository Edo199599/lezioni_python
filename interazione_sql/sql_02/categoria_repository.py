from repository import get_connection
from categoria import Categoria
from articolo_repository import articoli_categoria_repo

# funzione per ottenere una lista di oggetti Categoria con info complete (anche una lista di Articoli per ciascuna)
def elenco_categorie_repo():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM categorie"
                cursor.execute(sql)
                risultato = cursor.fetchall()
                categorie = []
                for record in risultato:
                    categoria = Categoria(id=record[0], descrizione=record[1])
                    articoli_categoria_repo(cursor, categoria)
                    categorie.append(categoria)
                return categorie
    except Exception as e:
        print(e)
        return None