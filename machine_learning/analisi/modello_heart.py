from modello_base import ModelloBase
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from kneed import KneeLocator           # per la ricerca del miglior numero di cluster
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans      # raggruppamento dei dati in k cluster basandosi sulla similarità delle osservazioni
import seaborn as sns



# creazione del modello per la predizione della presenza di malattie cardiache
# con clustering e classificazione

class ModelloHeart(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.variabili_quantitative, self.variabili_categoriali, self.scaler, self.encoder, self.dataframe_sistemato = self.sistemazione_dataframe()
        self.pca, self.dataframe_ridotto = self.riduzione_dataframe()
        self.numero_cluster = self.indiduazione_cluster()
        self.livello_rischio = {0: "Basso", 1: "Medio", 2: "Alto"}
        self.modello_clustering = self.clustering()
        self.grafico_cluster()


    # metodo di sistemazione del dataframe
    def sistemazione_dataframe(self):
        # separazione delle variabili categoriali da quelle quantitative
        # così da poterle trattare separatamente:
        # standardizzando le variabili quantitative e applicando il one-hot encoding alle variabili categoriali
        variabili_quantitative = ["age", "trestbps", "chol", "thalach", "oldpeak", "ca"]
        variabili_categoriali = ["sex", "cp", "fbs", "restecg", "exang", "slope", "thal"]
        # standardizzazione delle variabili quantitative
        scaler = StandardScaler()
        df_quantitative = pd.DataFrame(scaler.fit_transform(self.dataframe[variabili_quantitative]), columns=variabili_quantitative)
        # one-hot encoding delle variabili categoriali
        # per ogni variabile categoriale, creiamo un dataframe con le colonne corrispondenti ai valori univoci della variabile
        # esempio per sex = 0,1, viene creato un dataframe con due colonne e tante righe quante sono le righe del dataset
        # processo necessario solo in processi di machine learning con clustering e classificazione
        encoder = OneHotEncoder(sparse_output=False)
        # sparse_output=False per avere un array numpy e non una matrice sparsa da convertire
        df_categoriali = pd.DataFrame(encoder.fit_transform(self.dataframe[variabili_categoriali]))
        # non abbiamo bisogno di rinominare le colonne, in quanto il one-hot encoding crea colonne con nomi numerici nuove
        df_categoriali.columns = encoder.get_feature_names_out(variabili_categoriali)
        # prende i nomi delle colonne create dal one-hot encoding e li assegna come nomi delle colonne del dataframe
        # riunificazione dei due dataframe
        df_sistemato = pd.concat([df_quantitative, df_categoriali], axis = 1)
        # return di vari elementi per il loro utilizzo
        return variabili_quantitative, variabili_categoriali, scaler, encoder, df_sistemato

    # metodo di riduzione della dimensionalità del dataframe
    def riduzione_dataframe(self):
        pca = PCA(n_components=2) # riduzione a due dimensioni. é un numero usato come standard
        # i cluster di immagini per esempio sono a 3 dimensioni, ma per visualizzarli si riducono a 2 dimensioni
        df_ridotto = pd.DataFrame(pca.fit_transform(self.dataframe_sistemato), columns=["PC1", "PC2"])
        return pca, df_ridotto

    # metodo per individuazione numero ottimale di cluster
    def indiduazione_cluster(self):
        # calcolo valori di inerzia per vari cluster
        inertia = [] # lista per i valori di inerzia ovvero la somma delle distanze quadrate delle osservazioni dai centroidi
        cluster_range = range(1, 11) # range di valori per il testing del numero di cluster
        for k in cluster_range: # k è convenzionale
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(self.dataframe_ridotto)
            inertia.append(kmeans.inertia_) # tutti i valori di inerzia, uno per ognuno dei 10 cicli, vengono aggiunti alla lista
        # analisi numero ottimale cluster con strumento automatico
        knee_locator = KneeLocator(cluster_range, inertia, curve="convex", direction="decreasing")
        # quindi gli passiamo il numero di volte che abbiamo fatto il ciclo, i valori di inerzia e la curva di inerzia
        # il valore convex indica che la curva è convessa, direction decreasing indica che la curva è decrescente

        # ad ogni iterazione, l'inerzia diminuisce ovviamente essendo una somma di distanza
        # per questo la curva è comunque convessa e decrescente
        # dobbiamo trovare il punto in cui l'inerzia inizia a diminuire in modo meno significativo (ginocchio)
        # quello è il numero ottimale di cluster
        numero_ottimale_cluster = knee_locator.knee
        print(f"Numero ottimale cluster rilevato da KneeLocator: {numero_ottimale_cluster}")
        # se il numero ottimale stampato è 10 vuol dire che devo aumentare il range di valori di cluster nel cluster_range
        # i cluster rappresentano i gruppi di osservazioni simili tra loro
        # nel nostro caso i cluster sono 3 ipotetici livelli di rischio di malattie cardiache
        # conferma del numero ottimale di cluster mediante visualizzazione grafico a ginocchio
        plt.figure(figsize=(10, 6))
        plt.plot(cluster_range, inertia, marker="o")
        # il marker è un punto che indica il valore di inerzia per ogni cluster. Uso la o in quanto pallino
        plt.xlabel("Numero di cluster")
        plt.ylabel("Inerzia")
        plt.title("Metodo Elbow per selezione numero ottimale cluster")
        plt.show()
        return numero_ottimale_cluster

    # metodo per il clustering delle osservazioni
    def clustering(self):
        # creazione e addestramento del modello di clustering (aggiunta al dataframe una colonna con il cluster di appartenenza)
        kmeans = KMeans(n_clusters=self.numero_cluster, random_state=42)
        self.dataframe_ridotto["cluster"] = kmeans.fit_predict(self.dataframe_ridotto) # fit_predict = addestrati e predici
        # aggiunta nuova colonna al dataframe per sostituzione n° cluster con etichetta testuale
        self.dataframe_ridotto["Rischio"] = self.dataframe_ridotto["cluster"].map(self.livello_rischio)
        # conversione della colonna Rischio in una colonna di tipo categorico ordinato (livelli Basso < Medio < Alto)
        ordine_rischio = [self.livello_rischio[key] for key in sorted(self.livello_rischio.keys())]
        self.dataframe_ridotto["Rischio"] = pd.Categorical(self.dataframe_ridotto["Rischio"], categories=ordine_rischio, ordered=True)
        return kmeans

    # metodo per visualizzazione dei cluster in un grafico
    def grafico_cluster(self, paziente=None):
        plt.figure(figsize=(14, 10))
        # visualizzazione delle osservazioni
        sns.scatterplot(data=self.dataframe_ridotto, x="PC1", y="PC2", hue="Rischio", palette="viridis", style="Rischio", s=100, alpha=0.7)
        # hue crea colori diversi per ciascuna categoria rilevata dentro la colonna Rischio
        # palette è la palette di colori da utilizzare, style è lo stile di visualizzazione, s è la dimensione dei punti, alpha è la trasparenza
        # visualizzazione dei centroidi
        centroidi = self.modello_clustering.cluster_centers_ # otteniamo i centroidi dei cluster
        plt.scatter(centroidi[:, 0], centroidi[:, 1], s=300, c="black", marker="o", label="Centroidi")
        # [:,0] prende tutte le righe della colonna 0, [:,1] prende tutte le righe della colonna 1 (PC1 e PC2)
        #visualizzazione del nuovo paziente (se presente)
        if paziente is not None:
            plt.scatter(paziente["PC1"], paziente["PC2"], c="red", s=200, marker="X", label="Nuovo Paziente")
        # indicazioni testuali
        plt.title("Distribuzione pazienti per livello di rischio cardiaco")
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.legend(title="Livello di Rischio")
        plt.show()

    # metodo per valutazione livelli di rischio di un nuovo paziente
    def valutazione_paziente(self, dati_paziente): # lo chiameremo dall'esterno dando i dati del paziente
        # costruzione dataframe per il nuovo paziente
        df_paziente = pd.DataFrame([dati_paziente])
        # le quadre perché dati_paziente è un singolo elemento e non una lista per cui non servirebbero
        # standardizzazione e one-hot encoding dei dati del paziente
        df_paziente_quant = pd.DataFrame(self.scaler.transform(df_paziente[self.variabili_quantitative]), columns=self.variabili_quantitative)
        # one hot encoding variabili categoriali
        df_paziente_cat = pd.DataFrame(self.encoder.transform(df_paziente[self.variabili_categoriali]))
        df_paziente_cat.columns = self.encoder.get_feature_names_out(self.variabili_categoriali)
        # riunificazione dei due dataframe
        df_paziente_sistemato = pd.concat([df_paziente_quant, df_paziente_cat], axis=1)
        # riduzione dimensionalità del dataframe del paziente
        # dobbiamo ricreare le stesse condizioni del dataframe su cui il modello si è allenato
        df_paziente_ridotto = pd.DataFrame(self.pca.transform(df_paziente_sistemato), columns=["PC1", "PC2"])
        # predizione del livello di rischio del paziente (estrazione dell'unico valore nell'arrey)
        cluster = self.modello_clustering.predict(df_paziente_ridotto)[0]
        livello_rischio = self.livello_rischio[cluster]
        print(f"Livello di rischio del paziente: {livello_rischio}")
        # invocazione metodo per visualizzazione nel grafico
        self.grafico_cluster(df_paziente_ridotto)

# utilizzo modello
modello = ModelloHeart("../dataset/data_07.csv")
# modello.analisi_generali(modello.dataframe_ridotto)
# vogliamo capire se le variabili che sembrano categoriali lo sono effettivamente. Droppiamo quelle che non lo sono già con certezza
# modello.analisi_valori_univoci(modello.dataframe, ["age", "trestbps", "chol", "thalach", "oldpeak"])
# modello.analisi_indici_statistici(modello.dataframe)
# modello.individuazione_outliers(modello.dataframe, ["sex", "cp", "fbs", "restecg", "exang", "slope", "thal"])

# predizione nuovo paziente
nuovo_paziente = {
    "age": 55,
    "sex": 1,
    "cp": 2,
    "trestbps": 130,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.5,
    "slope": 1,
    "ca": 0,
    "thal": 2
}

modello.valutazione_paziente(nuovo_paziente)

# colonne che compongono il dataset
# cp = tipo di dolore toracico - categoriale
# trestbps = pressione sanguigna arteriosa a riposo - quantitativa
# chol = colesterolo sierico  - quantitativa
# fbs = zucchero nel sangue a digiuno (glicemia) - categoriale
# restecg = risultati elettrocardiografici a riposo - categoriale
# thalach = frequenza cardiaca massima raggiunta - quantitativa
# exang = angina indotta da sforzo - categoriale
# oldpeak = depressione ST indotta da esercizio rispetto al riposo - quantitativa
# slope = pendenza del segmento ST di esercizio - categoriale
# ca = numero di vasi principali colorati da fluorosopia - quantitativa
# thal = tipo di talassemia - categoriale