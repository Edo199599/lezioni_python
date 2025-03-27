from machine_learning.analisi.modello_base import ModelloBase
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, contingency

_FILE_PATH = "dataset/docenti.csv"

class ModelloDocenti(ModelloBase):

    def __init__(self):
        self.dataframe = pd.read_csv(_FILE_PATH)
        self.df_pulito = self.pulizia_dataframe()
        self.tabella_contingenza("Qualifica")
        self.tabella_contingenza("Genere")

    def pulizia_dataframe(self):
        df_pulito = self.dataframe.copy()
        df_pulito = df_pulito.dropna(axis=1, how="all")
        colonne_unico_valore = []
        for col in df_pulito.columns:
            if df_pulito[col].nunique() < 2:
                colonne_unico_valore.append(col)
        df_pulito = df_pulito.drop(colonne_unico_valore, axis = 1)
        df_pulito = df_pulito.drop(["TIME_PERIOD"], axis = 1)
        indici_righe_eliminare = df_pulito.index[(df_pulito["SEX"] == 9) | (df_pulito["FACULTY_TYPE"] == 99) |
                                                 (df_pulito["TYPE_UNIV_MANAGEMENT"] == 9) | (df_pulito["TITLE"] == 9)]
        df_pulito = df_pulito.drop(indici_righe_eliminare, axis = 0)
        df_pulito = df_pulito.rename(columns = {"TYPE_UNIV_MANAGEMENT":"Tipo Università", "FACULTY_TYPE":"Facoltà",
                                                "SEX": "Genere", "TITLE": "Qualifica", "OBS_VALUE": "Valore Osservato"})
        return df_pulito

    def tabella_contingenza(self, col):
        tabella_contingenza = pd.crosstab(self.df_pulito[col], self.df_pulito["Facoltà"], values=self.df_pulito["Valore Osservato"], aggfunc="sum")
        tabella_contingenza.columns = tabella_contingenza.columns.map({
            1: "Agraria", 2: "Architettura", 3: "Chimica Industriale", 4: "Beni Culturali",
            5: "Economia", 6: "Farmacia", 7: "Giurisprudenza", 8: "Ingegneria", 9: "Lettere e Filosofia",
            10: "Lingue e Lett. Straniere", 11: "Medicina", 12: "Veterinaria",
            13: "Psicologia", 14: "Scienze Ambientali", 15: "Sc. d. Formazione",
            16: "STEM", 17: "Scienze Motorie", 18: "Scienze Politiche",
            19: "Scienze Statistiche", 20: "Sociologia", 21: "Altro"
        })
        if col == "Qualifica":
            tabella_contingenza.index = tabella_contingenza.index.map({
                1: "Professore Ordinario", 2: "Professore Associato", 3: "Ricercatore"
            })
        else:
            tabella_contingenza.index = tabella_contingenza.index.map({
                1: "Maschi", 2: "Femmine"
            })
        print(f"****************** TABELLA CONTINGENZA ({col}-Facoltà) ******************", tabella_contingenza.transpose().to_string(), sep="\n")
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f"****************** TEST CHI-QUADRO ({col}-Facoltà) ******************", f"Chi-quadro: {chi2}", f"P-value: {format(p, '.53f')}", sep="\n")
        cramer = contingency.association(tabella_contingenza, method="cramer")
        print(f"****************** INDICE DI CRAMER ({col}-Facoltà) ******************", f"Cramer: {cramer}", sep="\n")
        self.grafico_contingenza(tabella_contingenza, col)
        return tabella_contingenza

    @staticmethod
    def grafico_contingenza(tabella_contingenza, col):
        tabella_contingenza.transpose().plot(kind="bar")
        plt.title(f"{col} per Facoltà")
        plt.ylabel("Valore Osservato")
        plt.legend(title=col, loc="upper left")
        # per allineare la legenda a sinistra a legend si passa il parametro loc="upper left"
        # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.tick_params(rotation=90, axis="x", labelsize=6)
        plt.tight_layout()
        plt.show()


modello = ModelloDocenti()
# modello.analisi_generali(modello.df_pulito)
# modello.analisi_valori_univoci(modello.df_pulito)





