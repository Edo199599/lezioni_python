from modello_base import ModelloBase
import pandas as pd
import pycountry
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
import matplotlib.pyplot as plt


class ModelloImmunizzazione(ModelloBase):


    def __init__(self, dataset_path):
        # in lettura del dataframe devo passare il parametro skiprows=4 per saltare le prime 4 righe che non contengono dati
        self.dataframe = pd.read_csv(dataset_path, skiprows=4)
        self.dataframe_sistemato = self.sistemazione_dataframe()

    # metodo di sistemazione dataframe
    def sistemazione_dataframe(self):
        # 1. drop di colonne con valori duplicati o prive di valori
        df_sistemato = self.dataframe.copy().drop(["Country Code", "Indicator Code", "Unnamed: 68"], axis=1)
        # 2. filtro per indicatori di interesse (operazione avvenuta dopo averli trovati col metodo di individuazione)
        indicatori_interesse = [
            "Mortality rate, under-5 (per 1,000 live births)",
            "Immunization, measles (% of children ages 12-23 months)",
            "Immunization, DPT (% of children ages 12-23 months)",
            "Immunization, HepB3 (% of one-year-old children)"
        ]
        df_sistemato = df_sistemato[df_sistemato["Indicator Name"].isin(indicatori_interesse)]
        # 3. Rimozione osservazioni completamente prive di valori in tutte le colonne degli anni
        anni = [str(anno) for anno in range(1960, 2024)]
        df_sistemato = df_sistemato.dropna(subset=anni, how="all")
        # 4. Sostituzione dei valori NaN in colonne Anni con 0
        df_sistemato[anni] = df_sistemato[anni].fillna(0)
        # ora abbiamo 963 info non nulle
        # 5. Sostituzione colonne anni con un'unica colonna totale anni
        df_sistemato["Total Value (1960-2023)"] = df_sistemato.iloc[:, 2:].sum(axis=1)
        # iloc prende le righe e le colonne in base al loro indice, axis=1 indica che vogliamo sommare le colonne
        # stiamo dicendo quindi: seleziona tutte le righe (:) e tutte le colonne a partire dalla terza (2) fino alla fine naturale
        df_sistemato = df_sistemato.drop(columns=anni, axis=1)
        # 6. Conversione da formato lungo a formato largo (ora 4 osservazione per paese, dopo 1 osservazione per paese in 4 colonne
        df_sistemato = df_sistemato.pivot_table(
            index="Country Name", # riduce le 4 osservazioni per paese a 1
            columns="Indicator Name",
            values="Total Value (1960-2023)",
            fill_value=0 # riempire possibili valori Nan derivanti da ristrutturazione dataframe
        ).reset_index()
        # Togliamo la scritta Indicator Name come intestazione indici di riga
        df_sistemato.columns.name = None
        # 7. Aggiunta colonna Immunizzazione con totale valori delle varie immunizzazioni
        df_sistemato["Immunization (%)"] = df_sistemato.iloc[:, 1:4].sum(axis=1) # per colonne 1, 2 e 3
        # decidiamo se tenere le colonne di immunizzazione singole o meno. Le teniamo ma nel caso si eseguirebbe:
        # df_sistemato = df_sistemato.drop(["Immunization, measles (% of children ages 12-23 months)", "Immunization, DPT (% of children ages 12-23 months)", "Immunization, HepB3 (% of one-year-old children)"], axis=1)
        # 8. Esclusione regioni di aggregazione (non singole nazioni)
        lista_paesi_ufficiali = [country.name for country in pycountry.countries]
        df_sistemato = df_sistemato[df_sistemato["Country Name"].isin(lista_paesi_ufficiali)]
        # 9. Aggiunta colonna mortalità con valori espressi in percentuale (ora è in permille)
        df_sistemato["Mortality rate, under-5 (%)"] = df_sistemato["Mortality rate, under-5 (per 1,000 live births)"] / 10
        return df_sistemato

    # metodo per individuazione degli indicatori di interesse
    def individuazione_indicatori(self):
        parole_chiave = ["Mortality", "Immunization"]
        valori_unici_filtrati = [value for value in self.dataframe_sistemato["Indicator Name"].unique()
                                 if any(parola in value for parola in parole_chiave)]
        # partiamo dai valori univoci, filtriamo quelli che contengono le parole chiave estraendoli con any
        for valore in valori_unici_filtrati:
            print(valore)

    # correlazione e regressione lineare semplice (immunizzazione e mortalità)
    def correlazione_regressione(self):
        # analisi della correlazione
        corr, p = pearsonr(self.dataframe_sistemato["Immunization (%)"], self.dataframe_sistemato["Mortality rate, under-5 (%)"])
        print(f" La correlazione di Pearson risultante tra Immunizzazione e Mortalità Infantile è: {corr}")
        print(f" Il p-value sulla correlazione tra Immunizzazione e Mortalità Infantile è: {p}")
        # definizione variabile target e regressore
        y = self.dataframe_sistemato[["Mortality rate, under-5 (%)"]].values.reshape(-1, 1) # target
        x = self.dataframe_sistemato[["Immunization (%)"]].values.reshape(-1, 1) # regressore
        # creazione e addestramento semplificato modello
        regressione = LinearRegression()
        regressione.fit(x, y)
        # ottenimento della retta di regressione
        retta_regressione = regressione.predict(x)
        # grafico del modello
        plt.scatter(x, y, s=3, color="blue")
        plt.plot(x, retta_regressione, color="red", linewidth=1.1)
        plt.title("Regressione tra Immunizzazione e Mortalità Infantile")
        plt.xlabel("Immunizzazione (%)")
        plt.ylabel("Mortalità Infantile (%)")
        plt.show()



modello = ModelloImmunizzazione("../dataset/data_09.csv")
# modello.analisi_generali(modello.dataframe_sistemato)
# il database è pieno di colonne con solo un terzo dei dati e il resto Nan, pieno di colonne di cui alcune ridondati o inutili

# analisi selettiva dei valori univoci (lavorando per colonna)
# droppo tutte le colonne a meno di Indicator Name
colonne_no_univoci = []
for col in modello.dataframe_sistemato.columns:
    # if col != "Indicator Name":   # prima iterazione di questa funzione
    if col != "Country Name":
        colonne_no_univoci.append(col)
# modello.analisi_valori_univoci(modello.dataframe_sistemato, colonne_no_univoci)
# voglio cercare una specifica informazione. Posso provare a cercare per parole chiave invece che leggendole tutte
# Potrebbero essere Mortality e Immunization (creo un metodo per cercare le parole chiave)
# modello.individuazione_indicatori()

modello.correlazione_regressione()