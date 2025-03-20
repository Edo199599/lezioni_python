from modello_base import ModelloBase
import pandas as pd

class ModelloTitanic(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()

    # metodo di istanza per sistemazione dataframe
    def sistemazione_dataframe(self):
        # 1. drop colonne non utili (essendocene troppe che non ci interessano in generale)
        variabili_da_droppare = ["name","ticket", "fare", "cabin", "embarked", "home.dest", "boat", "body"]
        # aggiungo anche boat e body perchè pieni di Nan e con troppi pochi valori
        df_sistemato = self.dataframe.drop(variabili_da_droppare, axis=1)
        # 2. drop osservazioni (righe) con valori mancanti (tutti Nan)
        df_sistemato = df_sistemato.drop(index=1309, axis=0)
        # salvo la colonna age tutte le colonne hanno 1309 valori non nulli quindi non devo eliminare altro
        # sarebbe da verificare se conviene droppare i dati con i Nan oppure sostituirli con la media o la mediana
        # se avessi un database più grande potrei droppare le righe con Nan (tipo 200 su 10k osservazioni)
        # avendo 250 mancanze su 1300 piuttosto che doverla droppare sostituisco i valori mancanti
        # in caso di molti outliers potrei sostituire con la mediana
        # 3. Sostituzione valori NaN colonna age con la mediana
        # df_sistemato["age"] = df_sistemato["age"].fillna(df_sistemato["age"].median()) #fillna() individua e riempie i valori NaN
        # mettere la mediana generale crea molti outliers. Proviamo un altro tipo di calcolo della mediana:
        df_sistemato["age"] = (df_sistemato.groupby(["pclass", "sex"])["age"].apply(lambda x: x.fillna(x.median())).reset_index(level=[0,1], drop=True))
        # creo gruppi basati su classe del passeggero e sesso e per ciascun gruppo calcolo la mediana (scendo da 101 a 61 outliers)
        # il reset_index serve per eliminare i vecchi indici e avere un unico indice.
        # level=[0,1] indica che voglio annullare la nuova indicizzazione dei due gruppi nuovi, drop=True indica che voglio eliminare i vecchi indici
        return df_sistemato


#colonne del database
# pclass: classe del passeggero
# survived: sopravvissuto o meno
# sibsp: numero di fratelli/sorelle o coniugi a bordo
# parch: numero di genitori o figli a bordo
# embarked: porto di imbarco
# boat: numero del barchino di salvataggio
# body: numero identificativo del corpo se non sopravvissuto
# home.dest: destinazione finale



modello = ModelloTitanic("../dataset/data_04.csv")
modello.analisi_generali(modello.dataframe_sistemato)

# analisi valori univoci solo sulle colonne per cui abbia senso farlo
# differente dal drop delle colonne che non vogliamo proprio analizzare
modello.analisi_valori_univoci(modello.dataframe_sistemato, ["age", "sibsp", "parch"])
# droppo per gli outliers sex perché acquisisce solo due valori
modello.individuazione_outliers(modello.dataframe_sistemato, ["sex"])