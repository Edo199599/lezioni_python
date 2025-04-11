from prodotto import Prodotto
import unittest

# scegliamo lo strumento con cui eseguire i test di unità
# c'è un modulo integrato in Python che si chiama unittest
# ci sono altrimenti librerie esterne come pytest

# in un lavoro da fare in team, se un membro del team crea una classe o modifica un __init__
# i test possono essere una validazione

#classe che possieda funzionalità di test automatizzate
class TestProdotto(unittest.TestCase):
    # c'è già la freccetta verde di fianco alla classe per dire che è un test eseguibile

    # metodo per testare la validità delle informazioni Prodotto in fase di creazione
    # obiettivo: verificare che nome e prezzo del Prodotto vengano valorizzati correttamente
    def test_istanziazione(self):
        # anche questo test ha la freccetta. Posso lanciare solo questo come tutti insieme dalla classe
        # creo un oggetto Prodotto
        prodotto = Prodotto("Penna", 1.5)
        # verifico che il nome e il prezzo siano stati valorizzati correttamente con asserzioni
        self.assertEqual(prodotto.nome, "Penna")
        self.assertEqual(prodotto.prezzo, 1.5)
        # il test è andato a buon fine e le asserzioni erano corrette, sono vere
        # se un collega avesse modificato il __init__ di Prodotto, scrivendo self.prezzo = prezzo + 1
        # mi basterebbe lanciare il test e vedrei che non è più uguale a 1.5 avendo il test non superato

    # metodo per testare creazione di un Prodotto con valore non numerico o inferiore a 1
    # obiettivo : verificare che venga lanciato un ValueError (e non altri errori) con un determinato messaggio
    # uguale a quello predisposto
    def test_prezzo_sbagliato(self):
        # verifico che venga lanciato un ValueError
        with self.assertRaises(ValueError) as context:
            # creo un oggetto Prodotto con prezzo non numerico o inferiore a 1
            Prodotto("Penna", 0)
        # verifico che il messaggio di errore sia quello corretto
        self.assertEqual(str(context.exception), "Il prezzo deve essere un numero non inferiore a 1")