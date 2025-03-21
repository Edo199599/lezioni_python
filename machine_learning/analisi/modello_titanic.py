from modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt

class ModelloTitanic(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        # riga successiva commentata perché ho creato un nuovo dataset sistemato in una nuova directory da usare come base
        #self.dataframe_sistemato = self.sistemazione_dataframe()
        self.contingenza_classe = self.tabella_contingenza("Classe Passeggero", "Sopravvissuto")
        self.contingenza_genere = self.tabella_contingenza("Genere", "Sopravvissuto")
        self.correlazione_spearman("Età", "Sopravvissuto")
        self.grafici_contingenza()
        self.grafico_spearman()
        self.grafico_ripartizione()

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
        # in previsione di machine learning è meglio trasformare database testuali in numerici. ES:
        # 4. Rimappatura valori colonna sex (0: female - 1: male)
        df_sistemato["sex"] = df_sistemato["sex"].map({"female":0, "male":1})
        # map funziona con un dizionario con chiavi i valori originali ed elementi delle chiavi quelli da sostituire
        # 5. Modifica nomi colonne
        df_sistemato = df_sistemato.rename(columns={
            "pclass": "Classe Passeggero",
            "survived": "Sopravvissuto",
            "sex": "Genere",
            "age": "Età",
            "sibsp": "Fratelli/Coniugi",
            "parch": "Genitori/Figli"
        })
        # 6. Conversione di tipo float in tipo int
        for col in df_sistemato:
            df_sistemato[col] = df_sistemato[col].astype(int)
        return df_sistemato

# metodo per ottenere tabelle di contingenza - test chi quadro e Cramer (correlazione tra variabili categoriali)
    def tabella_contingenza(self, column, target):
        # generazione e stampa tabella di contingenza
        tabella_contingenza = pd.crosstab(self.dataframe[column], self.dataframe[target])
        # sostituzione label
        tabella_contingenza.columns = tabella_contingenza.columns.map({0:"Deceduti", 1:"Sopravvissuti"})
        if column == "Classe Passeggero":
            tabella_contingenza.index = tabella_contingenza.index.map({1:"Prima Classe", 2:"Seconda Classe", 3:"Terza Classe"})
        else:
            tabella_contingenza.index = tabella_contingenza.index.map({0:"Femmine", 1:"Maschi"})
        print(f"TABELLA DI CONTINGENZA TRA {column}-{target}:", tabella_contingenza, sep="\n")
        # test chi quadro e stampa esito
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f"Il p-value risultante dal test del chi quadro sulla tabella di contingenza {column}-{target} è: {p}")
        print(f"Notazione non scientifica del p-value -> {format(p, '.53f')}") #53 sono le cifre decimali massime mostrabili
        # si ottengono valori molto prossimi allo zero quindi si rifiuta l'ipotesi nulla e c'è correlazione tra le variabili
        # visto che esiste una correlazione, cerchiamo con Cramer la forza di questa correlazione
        # calcolo INDICE DI CRAMER e stampa del risultato
        cramer = contingency.association(tabella_contingenza, method="cramer")
        # method = "cramer" indica che voglio calcolare l'indice di Cramer
        # il metodo di cramer è un metodo per calcolare la correlazione tra variabili categoriali
        # pearson si sarebbe usato le variabili fossero state quantitative
        print(f"L'indice di Cramer calcolato sulla tabella di contingenza {column}-{target} è pari a -> {cramer}")
        # di base da 0 a 0.1 è una correlazione debole, da 0.1 a 0.3 è una correlazione bassa, da 0.3 a 0.5 è una correlazione moderata
        # da 0.5 a 0.7 è una correlazione alta, da 0.7 a 0.9 è una correlazione molto alta, da 0.9 a 1 è una correlazione perfetta
        # SPEARMAN misura la monotonicità di una relazione tra due variabili, ovvero se una variabile aumenta l'altra aumenta o diminuisce
        # range di valori da -1 a 1, -1 indica una relazione negativa, 0 indica assenza di relazione, 1 indica una relazione positiva
        return tabella_contingenza

    # metodo per ottenere correlazione di SPEARMAN (correlazione tra variabile quantitativa e variabile categoriale)
    def correlazione_spearman(self, column, target):
        # SPEARMAN misura la monotonicità di una relazione tra due variabili, ovvero se una variabile aumenta l'altra aumenta o diminuisce
        # range di valori da -1 a 1, -1 indica una relazione negativa, 0 indica assenza di relazione, 1 indica una relazione positiva
        # la tabella di contingenza non ha senso per valori non categoriali
        spearman_corr, p = spearmanr(self.dataframe[column], self.dataframe[target])
        print(f"La correlazione di Spearman risultante tra {column} e {target} è pari a {spearman_corr}")
        print(f"Il p-value risultante dal test di Spearman tra {column} e {target} è pari a {p}")

    # metodo per generare grafici a barre partendo da tabelle di contingenza
    def grafici_contingenza(self):
        # generazione figura che ospiterà i due grafici
        figura, cella = plt.subplots(1, 2, figsize=(12, 5)) # 1 riga, 2 colonne, dimensioni 12x5 della figura
        # 1. Primo grafico - sopravvivenza per classe passeggero
        self.contingenza_classe.plot(kind="bar", ax=cella[0], color=["red", "green"])
        # kind = "bar" indica che voglio un grafico a barre, ax = cella[0] indica che voglio il grafico nella prima cella
        # le alternative a bar sono line, barh, hist, box, kde, density, area, pie, scatter, hexbin
        # e stanno per barre, linee, barre orizzontali, istogramma, boxplot, densità, area, torta, scatterplot, esagoni
        cella[0].set_title("Frequenza di Sopravvivenza per Classe Passeggero")
        cella[0].set_xlabel("Classe Passeggero")
        cella[0].set_ylabel("Frequenza")
        cella[0].legend(title="Legenda")
        cella[0].tick_params(axis="x", rotation=0) # ruoto le etichette dell'asse x di 0 gradi. Disposizione in orizzontale. Di default sono a 90 gradi
        # cella 0 è la prima cella della figura che è stata divisa in due parti (per 2 grafici)
        # 2. Secondo grafico - sopravvivenza per genere passeggero
        self.contingenza_genere.plot(kind="bar", ax=cella[1], color=["red", "green"])
        # kind = "bar" indica che voglio un grafico a barre, ax = cella[0] indica che voglio il grafico nella prima cella
        # le alternative a bar sono line, barh, hist, box, kde, density, area, pie, scatter, hexbin
        # e stanno per barre, linee, barre orizzontali, istogramma, boxplot, densità, area, torta, scatterplot, esagoni
        cella[1].set_title("Frequenza di Sopravvivenza per Genere Passeggero")
        cella[1].set_xlabel("genere Passeggero")
        cella[1].set_ylabel("Frequenza")
        cella[1].legend(title="Legenda")
        cella[1].tick_params(axis="x",rotation=0)  # ruoto le etichette dell'asse x di 0 gradi. Disposizione in orizzontale. Di default sono a 90 gradi
        # show della figura
        plt.tight_layout() # aggiustamento spaziature per evitare sovrapposizioni
        plt.show()

    # metodo per generare un grafico a dispersione per dimostrare correlazione di Spearman
    def grafico_spearman(self):
        # generazione figura che ospiterà il grafico
        plt.figure(figsize=(8, 5))
        # grafico unico (asse x = età, asse y = sopravvivenza)
        plt.scatter(self.dataframe["Età"], self.dataframe["Sopravvissuto"], alpha= 0.5, color="blue")
        # scatter crea un grafico a dispersione, i punti sono sparsi e non collegati
        # alpha = 0.5 indica la trasparenza dei punti, 0 è trasparente, 1 è opaco
        # non uso la funzione partendo da correlazione_spearman perché quella mi da solo due valori, non una tabella
        plt.title("Distribuzione Età vs Sopravvivenza")
        plt.xlabel("Età del passeggero")
        plt.ylabel("Sopravvissuto (0 = No, 1 = Sì)")
        # show della figura
        plt.show()

    # metodo per generare grafico a torta per ripartizione sopravvissuti-deceduti
    def grafico_ripartizione(self):
        # conteggio generale sopravvissuti e deceduti
        sopravvissuti_deceduti = self.dataframe["Sopravvissuto"].value_counts() # restituisce un oggetto Series con i valori unici e le frequenze
        sopravvissuti_deceduti.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["red", "green"],
                                    labels=sopravvissuti_deceduti.index.map({0:"Deceduti", 1:"Sopravvissuti"}))
        # autopct="%1.1f%%" indica che voglio la percentuale con una cifra decimale e un solo numero decimale
        # startangle=90 indica che voglio la prima detta di torta parta da 90 gradi
        plt.title("Distribuzione Sopravvissuti vs Deceduti")
        plt.ylabel("") # non vogliamo titoli sull'asse
        # show della figura
        plt.show()

#colonne del database
# pclass: classe del passeggero
# survived: sopravvissuto o meno
# sibsp: numero di fratelli/sorelle o coniugi a bordo
# parch: numero di genitori o figli a bordo
# embarked: porto di imbarco
# boat: numero del barchino di salvataggio
# body: numero identificativo del corpo se non sopravvissuto
# home.dest: destinazione finale

# modello = ModelloTitanic("../dataset/data_04.csv")
# lo commento perché ho creato un nuovo dataset sistemato in una nuova directory
modello = ModelloTitanic("../dataset_sistemati/data_04.csv")
#modello.analisi_generali(modello.dataframe_sistemato)

# analisi valori univoci solo sulle colonne per cui abbia senso farlo
# differente dal drop delle colonne che non vogliamo proprio analizzare
# modello.analisi_valori_univoci(modello.dataframe_sistemato, ["age", "sibsp", "parch"])
# droppo per gli outliers sex perché acquisisce solo due valori
# .individuazione_outliers(modello.dataframe_sistemato, ["sex"])

# creo un nuovo dataframe con dataset sistemato come nuova base di partenza e lo salvo
# lo commento per non crearlo ad ogni passaggio

#modello.dataframe_sistemato.to_csv("../dataset_sistemati/data_04.csv", index=False)