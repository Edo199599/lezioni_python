from machine_learning.analisi.modello_base import ModelloBase
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

_FILE_PATH = "dataset/pollution.csv"

class ModelloInquinamento(ModelloBase):


    def __init__(self):
        self.dataframe = pd.read_csv(_FILE_PATH)
        self.dataframe_sistemato, self.scaler = self.sistemazione_dataframe()
        self.individuazione_correlazioni()
        self.regressione_lineare_semplice("SO2")
        self.regressione_lineare_semplice("NO2")


    # def valori_non_zero(self, column):
    #     # funzione che data una colonna mi restituisce il numero di valori diverso da 0
    #     counter = 0
    #     for value in column:
    #         if value == None or value == "?" or value == np.nan or value == "0":
    #             counter += 1
    #     print(counter)

    def sistemazione_dataframe(self):
        df_sistemato = self.dataframe.copy()
        # eliminazione osservazioni con "good" or "Hazadous" in "Air Quality"
        df_sistemato = df_sistemato[df_sistemato["Air Quality"] != "Good"]
        df_sistemato = df_sistemato[df_sistemato["Air Quality"] != "Hazardous"]
        df_sistemato = df_sistemato[df_sistemato["SO2"] > 0]
        df_sistemato= df_sistemato.drop(["Air Quality"], axis = 1)
        col_da_standardizzare = df_sistemato.drop(["NO2", "SO2"], axis=1)
        scaler = StandardScaler()
        col_standardizzate= scaler.fit_transform(col_da_standardizzare)
        df_scalato = pd.DataFrame(col_standardizzate, columns=col_da_standardizzare.columns, index=df_sistemato.index)
        df_sistemato = pd.concat([df_scalato, df_sistemato["NO2"], df_sistemato["SO2"]], axis=1)
        return df_sistemato, scaler


    def individuazione_correlazioni(self):
        matrice_correlazione = self.dataframe_sistemato.corr()
        print("******** MATRICE DI CORRELAZIONE ********", matrice_correlazione.to_string(), sep="\n")
        plt.figure(figsize=(20, 10))
        sns.heatmap(matrice_correlazione, annot=True, cmap="Spectral", fmt=".2f", linewidths=0.5)
        plt.xticks(rotation=15, ha="right")
        plt.title("Matrice di correlazione")
        plt.show()

    def regressione_lineare_semplice(self, target):
        y = self.dataframe_sistemato[[target]].values.reshape(-1, 1)
        x = self.dataframe_sistemato[["Population_Density"]].values.reshape(-1, 1)
        regressione = LinearRegression()
        regressione.fit(x, y)
        retta_regressione = regressione.predict(x)
        print(f"******** PUNTEGGIO REGRESSIONE TRA {target} - POPULATION DENSITY *******", regressione.score(x, y), sep="\n")
        col_index = self.dataframe_sistemato.columns.get_loc("Population_Density")
        x_reali = (x * self.scaler.scale_[col_index]) + self.scaler.mean_[col_index]
        plt.scatter(x_reali, y, color="red", s=0.5, label = "Osservazioni")
        plt.plot(x_reali, retta_regressione, color="blue", label="Retta di regressione", linewidth=1.5)
        plt.title(f"Correlazione {target}-Population Density")
        plt.xlabel("Population Density")
        plt.ylabel(target)
        plt.show()


modello = ModelloInquinamento()
# modello.analisi_generali(modello.dataframe_sistemato)
# modello.analisi_generali(modello.dataframe_sistemato)
# modello.analisi_indici_statistici(modello.dataframe_sistemato)
# modello.individuazione_outliers(modello.dataframe_sistemato, ["Air Quality"])
# modello.analisi_valori_univoci(modello.dataframe_sistemato)
# ModelloInquinamento.valori_non_zero(modello.dataframe, modello.dataframe["Air Quality"])