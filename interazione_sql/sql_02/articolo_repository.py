from repository import get_connection
from articolo import Articolo
from categoria import Categoria

# funzione per ottenere una lista di oggetti Articolo con info complete
def elenco_articoli_repo():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM articoli JOIN categorie ON articoli.id_categoria= categorie.id"
                # buona norma copiarsi la query e provarla su phpMyAdmin
                cursor.execute(sql)
                risultato = cursor.fetchall()
                # print(risultato)
                articoli = []
                for record in risultato:
                    categoria = Categoria(id=record[4], descrizione=record[5])
                    articolo = Articolo(id=record[0], nome=record[1], prezzo=record[2], categoria=categoria)
                    articoli.append(articolo)
                return articoli
    except Exception as e:
        print(e)
        return None


# funzione per ottenere elenco articoli di una determinata categoria
def articoli_categoria_repo(cursor, categoria):
    # non serve il try except perché andrà a chiamarla dentro un altro try except
    sql = "SELECT * FROM articoli WHERE id_categoria = %s"
    valori = categoria.id,
    cursor.execute(sql, valori)
    risultato = cursor.fetchall()
    categoria.articoli = [Articolo(id, nome, prezzo) for id, nome, prezzo, id_cat in risultato]
    # anche se id_cat non lo usiamo dobbiamo comunque scriverlo avendo risultato 4 colonne
