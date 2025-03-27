from modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt



class ModelloAlcolici(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()
        self.tabella_contingenza("AGE")
        self.tabella_contingenza("SEX")

    # metodo di sistemazione dataframe
    def sistemazione_dataframe(self):
        # 1. copia dataframe
        df_sistemato = self.dataframe.copy()
        # 2. drop colonne completamente prive di valori
        df_sistemato = df_sistemato.dropna(axis=1, how="all")
        # how = "all" indica che la colonna viene eliminata solo se tutti i valori sono mancanti
        # 3. drop delle colonne con valore unico
        colonne_unico_valore = []
        for col in df_sistemato.columns:
            if df_sistemato[col].nunique() < 2:
                colonne_unico_valore.append(col)
        df_sistemato = df_sistemato.drop(colonne_unico_valore, axis=1)
        # 4. eliminazione righe con valori MEASURE=HSC - SEX=9 - AGE=Y_GE11
        indici_righe_da_eliminare = df_sistemato.index[(df_sistemato["MEASURE"] == "HSC") |
                                                       (df_sistemato["SEX"] == 9) |
                                                       (df_sistemato["AGE"] == "Y_GE11")]
        df_sistemato = df_sistemato.drop(indici_righe_da_eliminare, axis=0)
        # non è servito un ciclo for perché index è un iterabile e analizza riga per riga creando una lista di indici
        return df_sistemato

    # metodo per ottenere tabelle di contingenza - test chi-quadro - indici Cramer
    def tabella_contingenza(self, column):
        # la tabella di contingenza serve a visualizzare le frequenze con cui si presentano le combinazioni di valori
        # generazione tabella contingenza
        tabella_contingenza = pd.crosstab(self.dataframe_sistemato[column],
                                          self.dataframe_sistemato["DATA_TYPE"],
                                          values=self.dataframe_sistemato["OBS_VALUE"],
                                          aggfunc="sum")
        # values specifica quale colonna considerare per il conteggio delle osservazioni
        # aggfunc specifica quale funzione di aggregazione applicare alle osservazioni, in questo caso la somma
        # sostituzione label tabella di contingenza
        tabella_contingenza.columns = tabella_contingenza.columns.map({
            "11_ALCF_1VOL": "Cons_Alc_F_Pasto -1/Settimana",
            "11_ALC_FUORI": "Cons_Alc_F_Pasto",
            "11_ALC_NFUORI": "No_Cons_Alc_F_Pasto"
        })
        if column == "SEX":
            tabella_contingenza.index = tabella_contingenza.index.map({1: "Maschi", 2: "Femmine"})
        # stampa tabella contingenza
        print(f"***** TABELLA CONTINGENZA {column}-DATA_TYPE *****", tabella_contingenza.to_string(), sep="\n")
        # test del chi-quadro e stampa esito (p-value)
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f"Il p-value risultante da test del chi-quadro tra {column}-DATA_TYPE è {format(p, ".53f")}")
        # calcolo dell'indice di Cramer e stampa esito
        totale_osservazioni = tabella_contingenza.sum().sum()
        # .sum().sum() somma tutti i valori della tabella di contingenza (somma tutti i valori per ogni colonna e poi somma i risultati)
        # se ne mettono due perché il primo .sum() somma le righe e il secondo .sum() somma per colonne (o viceversa)
        dimensione_minima = min(tabella_contingenza.shape) - 1 # valore minimo in una tupla righe-colonne tabella contingenza
        # si aggiunge il -1 perché l'indice di Cramer è calcolato come radice quadrata del rapporto tra chi2 e (n * (min(righe, colonne) - 1))
        cramer = np.sqrt(chi2 / (totale_osservazioni * dimensione_minima))
        print(f"L'indice di Cramer calcolato sulla tabella di contingenza {column}-DATA_TYPE e {cramer}")
        # invocazione metodo per generazione grafici di contingenza
        self.grafico_contingenza(tabella_contingenza, "Fascia età" if column == "AGE" else "Genere")


    # metodo per generazione grafici di distribuzione a barre
    @staticmethod
    def grafico_contingenza(tabella_contingenza, colonna):
        tabella_contingenza.plot(kind="bar", stacked = "True", color = ["yellow", "red", "green"])
        plt.title(f"Frequenza di consumo per {colonna}")
        plt.xlabel(colonna)
        plt.ylabel("Persone")
        plt.legend(title="Tipo di consumo")
        plt.tick_params(rotation=45, axis="x")
        plt.tight_layout()
        # il comando precedente serve per evitare che le etichette siano sovrapposte
        plt.show()

# utilizzo modello
modello = ModelloAlcolici("../dataset/data_08.csv")
# modello.analisi_generali(modello.dataframe)
# modello.analisi_generali(modello.dataframe_sistemato)
# modello.analisi_valori_univoci(modello.dataframe_sistemato)

#Valori nel database
# THV sta per "Total Heavy Volume" e indica il volume totale di alcolici consumati
# THV_1VOL indica il volume totale di alcolici consumati da chi beve alcolici 1 volta a settimana
# HSC sta per High School Completion e indica il numero di persone che hanno completato la scuola superiore
# obs_value indica il numero di persone che hanno consumato alcolici