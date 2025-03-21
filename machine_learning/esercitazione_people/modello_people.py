from machine_learning.esercitazione_people.modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt

class ModelloPeople(ModelloBase):


    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_semplificato = self.dataframe_semplificato_osso()
        self.contingenza_razza = self.tabella_contingenza("Razza", "Reddito")
        self.contingenza_genere = self.tabella_contingenza("Genere", "Reddito")
        self.contingenza_classe_lavorativa = self.tabella_contingenza("Classe lavorativa", "Reddito")
        self.contingenza_educazione = self.tabella_contingenza("Istruzione", "Reddito")
        self.contingenza_stato_civile = self.tabella_contingenza("Stato civile", "Reddito")
        self.grafico_contingenza()
        self.correlazione_spearman("Età", "Reddito")
        self.correlazione_spearman("Ore lavorate", "Reddito")
        self.grafico_spearman("Età")
        self.grafico_spearman("Ore lavorate")

    def dataframe_semplificato_osso(self):
        variabili_da_droppare = ["education-num", "fnlwgt", "relationship", "occupation", "capital-gain", "capital-loss", "native-country"]
        df_sistemato = self.dataframe.drop(variabili_da_droppare, axis=1)
        df_sistemato["sex"] = df_sistemato["sex"].map({"Female":0, "Male":1})
        df_sistemato["race"] = df_sistemato["race"].map({"White": 0, "Black": 1, "Asian-Pac-Islander": 2, "Amer-Indian-Eskimo": 3, "Other": 4})
        df_sistemato["target"] = df_sistemato["target"].map({"<=50K": 0, ">50K": 1})
        df_sistemato["education"] = df_sistemato["education"].map({"Preschool": 0, "1st-4th": 1, "5th-6th": 1,
                                                                   "7th-8th": 2, "9th": 3, "10th": 3, "11th": 3, "12th": 3, "HS-grad": 3,
                                                                   "Some-college": 4, "Assoc-acdm": 4, "Assoc-voc": 3,
                                                                   "Bachelors": 4, "Masters": 5, "Doctorate": 5, "Prof-school": 5})
        df_sistemato["marital-status"] = df_sistemato["marital-status"].map({"Never-married": 0, "Married-civ-spouse": 1, "Married-spouse-absent": 1, "Married-AF-spouse": 1, "Separated": 2, "Divorced": 2, "Widowed": 3})
        moda = df_sistemato["workclass"].mode().iloc[0]
        df_sistemato["workclass"] = df_sistemato["workclass"].replace("?", moda)
        df_sistemato = df_sistemato.rename(columns={
            "workclass": "Classe lavorativa",
            "age": "Età",
            "race": "Razza",
            "education": "Istruzione",
            "marital-status": "Stato civile",
            "sex": "Genere",
            "hours-per-week": "Ore lavorate",
            "target": "Reddito"
        })
        return df_sistemato

    # def valori_non_zero(self, column):
    #     # funzione che data una colonna mi restituisce il numero di valori diverso da 0
    #     counter = 0
    #     for value in column:
    #         if value != 0:
    #             counter += 1
    #     print(counter)

    def tabella_contingenza(self, col, target):
        tabella_contingenza = pd.crosstab(self.dataframe_semplificato[col], self.dataframe_semplificato[target])
        tabella_contingenza.columns = tabella_contingenza.columns.map({0: "<=50K", 1: ">50K"})
        if col == "Razza":
            tabella_contingenza.index = tabella_contingenza.index.map({0: "Bianco", 1: "Nero", 2: "Asiatico", 3: "Minoranze A.", 4: "Altro"})
        elif col == "Istruzione":
            tabella_contingenza.index = tabella_contingenza.index.map({0: "Asilo", 1: "Elementari/Medie", 2: "Superiori", 3: "Triennale", 4: "Magistrale", 5: "Dottorato"})
        elif col == "Stato civile":
            tabella_contingenza.index = tabella_contingenza.index.map({0: "Mai Sposato", 1: "Sposato", 2: "Separato/Divorziato", 3: "Vedovo"})
        elif col == "Genere":
            tabella_contingenza.index = tabella_contingenza.index.map({0: "Femmina", 1: "Maschio"})
        print(f"Tabella di contingenza tra {col}-{target}:", tabella_contingenza, sep="\n")
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f"Il p-value risultante dal test del chi quadro per {col}-{target} è: {p}")
        print(f"Notazione non scientifica del p-value -> {format(p, '.53f')}")
        cramer = contingency.association(tabella_contingenza, method="cramer")
        print(f"L'indice di Cramer per {col}-{target} è pari a: {cramer}")
        return tabella_contingenza
        # dai valori notiamo che i p-value sono tutti attorno allo 0, quindi la correlazione è presente, l'ipotesi nulla viene rigettata
        # l'indice di cramer però ci dice che la correlazione è molto bassa per il secondo caso e quasi nulla per il primo

    def grafico_contingenza(self):
        figura, cella = plt.subplots(2, 2, figsize=(24, 24))
        self.contingenza_razza.plot(kind="bar", ax=cella[0, 0], color=["red", "green"])
        cella[0,0].set_title("Frequenza Reddito per Razza", size=20)
        cella[0,0].set_xlabel("Razza", size=20)
        cella[0,0].set_ylabel("Frequenza", size=20)
        cella[0,0].legend(title="Legenda")
        cella[0,0].tick_params(axis="x", rotation=0)
        self.contingenza_genere.plot(kind="bar", ax=cella[0, 1], color=["red", "green"])
        cella[0,1].set_title("Frequenza Reddito per Genere", size=20)
        cella[0,1].set_xlabel("Genere", size=20)
        cella[0,1].set_ylabel("Frequenza", size=20)
        cella[0,1].legend(title="Legenda")
        cella[0,1].tick_params(axis="x", rotation=0)
        self.contingenza_educazione.plot(kind="bar", ax=cella[1,0], color=["red", "green"])
        cella[1,0].set_title("Frequenza Reddito per Titolo di Studio", size=20)
        cella[1,0].set_xlabel("Titolo di Studio", size=20)
        cella[1,0].set_ylabel("Frequenza", size=20)
        cella[1,0].legend(title="Legenda")
        cella[1,0].tick_params(axis="x", rotation=0)
        self.contingenza_stato_civile.plot(kind="bar", ax=cella[1,1], color=["red", "green"])
        cella[1,1].set_title("Frequenza Reddito per Stato Civile", size=20)
        cella[1,1].set_xlabel("Stato Civile", size=20)
        cella[1,1].set_ylabel("Frequenza", size=20)
        cella[1,1].legend(title="Legenda")
        cella[1,1].tick_params(axis="x", rotation=0)


        plt.tight_layout()
        plt.show()
        # dai grafici è possibile notare che la razza influenza poco il reddito (come ci aspettavamo dalle analisi degli indici)
        # mentre ha un'importanza maggiore per il genere

    def correlazione_spearman(self, col, target):
        # SPEARMAN misura la monotonicità di una relazione tra due variabili, ovvero se una variabile aumenta l'altra aumenta o diminuisce
        # range di valori da -1 a 1, -1 indica una relazione negativa, 0 indica assenza di relazione, 1 indica una relazione positiva
        # la tabella di contingenza non ha senso per valori non categoriali
        spearman_corr, p = spearmanr(self.dataframe_semplificato[col], self.dataframe_semplificato[target])
        print(f"La correlazione di Spearman risultante tra {col} e {target} è pari a {spearman_corr}")
        print(f"Il p-value risultante dal test di Spearman tra {col} e {target} è pari a {p}")
        # per tutte e due le analisi effettuate abbiamo dei p value pari a 0 indicando che la correlazione è presente
        # la correlazione di spearman è per tutti positiva indicando che all'aumentare di una variabile aumenta anche l'altra
        # anche se per le ore lavorate la correlazione è molto bassa mentre per l'età è bassa

    def grafico_spearman(self, col):
        # generazione figura che ospiterà il grafico
        plt.figure(figsize=(8, 5))
        # grafico unico (asse x = età, asse y = sopravvivenza)
        plt.scatter(self.dataframe_semplificato[col], self.dataframe_semplificato["Reddito"], alpha= 0.5, color="blue")
        # scatter crea un grafico a dispersione, i punti sono sparsi e non collegati
        # alpha = 0.5 indica la trasparenza dei punti, 0 è trasparente, 1 è opaco
        # non uso la funzione partendo da correlazione_spearman perché quella mi da solo due valori, non una tabella
        plt.title(f"Distribuzione {col} vs Reddito")
        plt.xlabel(f"{col} della persona")
        plt.ylabel("Reddito (0 = <=50k>, 1 = >50k)")
        # show della figura
        plt.show()
        # nel grafico l'intensità del pallino indica la densità di punti, più è scuro più sono fitti


modello = ModelloPeople("dataset/06_people.csv")
# modello.valori_non_zero(modello.dataframe["native-country"])
# modello.valori_non_zero(modello.dataframe["capital-gain"])



# nel database i titoli rappresentano:
# workclass: classe lavorativa
# fnlwgt: final weight, è il peso finale che indica quante persone rappresenta ogni osservazione
# education-num: numero di anni di istruzione
# capital-gain: guadagno di capitale
# capital-loss: perdita di capitale
# hours-per-week: ore lavorative settimanali
# native-country: paese di origine
# income: reddito annuo

# modello.analisi_valori_univoci(modello.dataframe_semplificato)