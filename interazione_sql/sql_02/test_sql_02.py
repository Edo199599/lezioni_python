from articolo_repository import *
from categoria_repository import *

# funzione per testare elenco articoli
def test_elenco_articoli():
    esito = elenco_articoli_repo()
    if esito is not None:
        for articolo in esito:
            print(articolo)

# funzione per testare elenco categorie
def test_elenco_categorie():
    esito = elenco_categorie_repo()
    if esito is not None:
        for categoria in esito:
            print(categoria)
            for articolo in categoria.articoli:
                print(articolo.stampa_per_categoria())

# invocazioni funzioni
test_elenco_articoli()
test_elenco_categorie()