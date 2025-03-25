from modello_base import ModelloBase
import pandas as pd
from sklearn.model_selection import train_test_split                    # per la suddivisione del dataset
from sklearn.linear_model import Perceptron                             # modello Perceptron
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix       # metodi per la valutazione del modello
from sklearn.preprocessing import StandardScaler                        # per la standardizzazione delle variabili
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

class ModelloIris(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.scaler, self.modello_classificazione = self.classificazione()

    # metodo per generazione di modello Perceptron
    # classificatore lineare, combina i dati in input (le nostre 4 colonne) e assegna un etichetta a quella osservazione (la classe)
    # si autocorregge in addestramento modificando di modifica in modifica il peso dei dati in input che vengono combinati
    def classificazione(self):
        # suddivisione dataframe in variabili e target (no bidimensionale)
        y = self.dataframe["class"] # target
        x = self.dataframe.drop(["class"], axis=1) # variabili
        # suddivisione delle osservazioni in addestramento e test (70% all'addestramento e 30% al test - essendo il dataset piccolo)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
        # standardizzazione dei valori delle variabili
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)
        # non faccio il fit sul test set per non influenzare il modello con informazioni che non dovrebbe avere
        # uso la stessa standardizzazione del train set per il test set per avere una comparazione corretta
        # creazione e addestramento del modello di classificazione Perceptron
        classificazione = Perceptron()
        classificazione.fit(x_train, y_train)
        # predizione del modello
        predizioni = classificazione.predict(x_test)
        # valutazione del modello
        print("******** VALUTAZIONE MODELLO CLASSIFICAZIONE ********")
        print(f"L'accuratezza delle predizioni del modello è pari a {accuracy_score(y_test, predizioni)}")
        print("Il report di classificazione del modello è pari a: ", classification_report(y_test, predizioni), sep="\n")
        # l'accuratezza indica la percentuale di osservazioni correttamente classificate.
        # Sopra il 90% è un buon modello, sotto il 70% è un modello da scartare
        # precision indica che il modello non assegna mai una classe a un'osservazione che non appartiene a quella classe
        # recall indica che il modello è in grado di trovare tutte le osservazioni di una classe
        # f1-score è una media armonica tra precision e recall
        # iris setosa viene catalogata bene, le altre due classi vengono confuse tra loro ma il dataset è piccolo da cui imparare
        # potremmo standardizzare le variabili per migliorare il modello (potrei creare un metodo apposito)
        # post standardizzazione il modello è migliorato noteovolmente dando un'accuratezza del 97%
        # MATRICE PREDIZIONI MODELLO
        matrice_predizioni = confusion_matrix(y_test, predizioni)
        print("****** MATRICE PREDIZIONI MODELLO ******", matrice_predizioni, sep="\n")
        # si legge come segue:
        # 42 fiori su 42 alla classe 0 (iris setosa) sono stati classificati correttamente tutti
        # 43 fiori su 46 alla classe 1 (iris versicolor) sono stati classificati correttamente, 3 sono stati classificati come classe 2
        # 46 fiori su 47 alla classe 2 (iris virginica) sono stati classificati correttamente, 1 è stato classificato come classe 1
        # la diagonale principale indica le osservazioni correttamente classificate
        # generiamo una heatmap per una migliore visualizzazione (nel caso avessimo più classi) della matrice di confusione
        plt.figure(figsize=(8, 6))
        sns.heatmap(matrice_predizioni, annot=True, cmap="Blues", fmt="d", xticklabels=classificazione.classes_,
                    yticklabels=classificazione.classes_, cbar=False)
        # fmt="d" indica che i valori sono interi senza decimali
        # xticklabels indica le etichette delle colonne prendendo i nomi delle classi dal modello di classificazione utilizzato
        # il _ indica che non mi interessa il valore di ritorno della funzione
        # cbar=False indica che non voglio la barra laterale
        plt.title("Matrice di Predizione")
        plt.xlabel("Classi predette", fontsize=12)
        plt.ylabel("Classi reali", fontsize=12)
        plt.show()
        # generazione di un grafico di distribuzione delle predizioni
        self.grafico_predizioni(matrice_predizioni)
        return scaler, classificazione

    # Metodo per generale un grafico delle predizioni
    @staticmethod
    def grafico_predizioni(matrice_predizioni):
        plt.bar([0, 1.4, 2.8], matrice_predizioni[:,0], color="blue", width=0.4, label="Iris Setosa")
        # la matrice indica la distanza delle barre dall'origine, width indica la larghezza delle barre
        # :,0 indica che prendo tutte le righe della prima colonna
        plt.bar([0.4, 1.8, 3.2], matrice_predizioni[:, 1], color="green", width=0.4, label="Iris Versicolor")
        # :,1 indica che prendo tutte le righe della seconda colonna
        plt.bar([0.8, 2.2, 3.6], matrice_predizioni[:, 2], color="red", width=0.4, label="Iris Virginica")
        plt.xticks([0,1.8,3.6]), ["Setosa", "Versicolor", "Virginica"]
        # posiziono le etichette delle classi nel punto in cui ogni classe è rappresentata dai propri stessi valori
        plt.xlabel("Specie")
        plt.ylabel("Numero di predizioni")
        plt.legend()
        plt.show()


    # metodo di esportazione su file del modello e dello scaler (serializzazione)
    def esportazione(self):
        joblib.dump(self.modello_classificazione, "../modelli/modello_iris.joblib")
        joblib.dump(self.scaler, "../modelli/scaler_iris.joblib")




# utilizzo del modello
modello = ModelloIris("../dataset/data_06.csv")
# modello.analisi_generali(modello.dataframe)
# # vediamo i valori univoci sulla colonna classe
# modello.analisi_valori_univoci(modello.dataframe, ["sepal_length", "sepal_width", "petal_length", "petal_width"])
# modello.analisi_indici_statistici(modello.dataframe)
# modello.individuazione_outliers(modello.dataframe, ["class"])
modello.esportazione()