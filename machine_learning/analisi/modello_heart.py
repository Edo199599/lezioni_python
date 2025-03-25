from modello_base import ModelloBase
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA

# creazione del modello per la predizione della presenza di malattie cardiache
# con clustering e classificazione

class ModelloHeart(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.variabili_quantitative, self.variabili_categoriali, self.scaler, self.encoder, self.dataframe_sistemato = self.sistemazione_dataframe()
        self.pca, self.dataframe_ridotto = self.riduzione_dataframe()


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
        pca = PCA(n_components=2) # riduzione a due dimensioni
        df_ridotto = pd.DataFrame(pca.fit_transform(self.dataframe_sistemato), columns=["PC1", "PC2"])
        return pca, df_ridotto



# utilizzo modello

modello = ModelloHeart("../dataset/data_07.csv")
modello.analisi_generali(modello.dataframe_ridotto)
# vogliamo capire se le variabili che sembrano categoriali lo sono effettivamente. Droppiamo quelle che non lo sono già con certezza
# modello.analisi_valori_univoci(modello.dataframe, ["age", "trestbps", "chol", "thalach", "oldpeak"])
# modello.analisi_indici_statistici(modello.dataframe)
# modello.individuazione_outliers(modello.dataframe, ["sex", "cp", "fbs", "restecg", "exang", "slope", "thal"])

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