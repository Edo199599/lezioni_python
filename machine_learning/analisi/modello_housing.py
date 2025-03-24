from modello_base import ModelloBase
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split # per suddividere il dataset in training e test set
from sklearn.metrics import mean_absolute_error, mean_squared_error



# REGRESSIONE LINEARE
# regressione lineare semplice, una sola variabile influenza il target
# regressione lineare multipla, più variabili influenzano il target

class ModelloHousing(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato, self.scaler = self.sistemazione_dataframe() # unpacking della tupla
        # self.individuazione_correlazioni()
        # self.regressione_lineare_semplice()
        self.regressione = self.regressione_lineare_multipla()


    # metodo di sistemazione dataframe
    def sistemazione_dataframe(self):
        # 1. copia del dataframe (sempre meglio per evitare di rovinarlo)
        df_sistemato = self.dataframe.copy()
        # 2. sostituzione outliers con i loro rispettivi limiti
        colonne_con_outliers = ["Distanza_Metro_m", "Distanza_Tangenziale_m"]
        for col in colonne_con_outliers:
            # calcolo dei limiti
            q1 = df_sistemato[col].quantile(0.25)
            q3 = df_sistemato[col].quantile(0.75)
            iqr = q3 - q1
            limite_inferiore = q1 - 1.5*iqr
            limite_superiore = q3 + 1.5*iqr
            # sostituzione outliers
            df_sistemato[col] = np.where(df_sistemato[col] < limite_inferiore, limite_inferiore, df_sistemato[col])
            # passiamo alla funzione where il valore da sostituire se la condizione è vera e il valore da mantenere se la condizione è falsa
            df_sistemato[col] = np.where(df_sistemato[col] > limite_superiore, limite_superiore, df_sistemato[col])
            # la funzione where non ha bisogno di un ciclo for per scorrere tutte le righe, ma lo fa in automatico
        # 3. Sostituzione colonna Anno_Costruzione con una colonna Età_Immobile (più significativa per la regressione)
        df_sistemato["Età_Immobile"] = datetime.now().year - df_sistemato["Anno_Costruzione"] # calcolo dell'età usando oggi come riferimento
        df_sistemato = df_sistemato.drop(["Anno_Costruzione"], axis=1) # eliminazione della colonna Anno_Costruzione
        # 4. Scaling colonne variabili - ovvero standardizzazione delle variabili
        colonne_da_scalare = df_sistemato.drop(["Prezzo_Vendita"], axis=1)
        scaler = StandardScaler() # creazione di un oggetto StandardScaler ovvero uno standardizzatore
        colonne_scalate = scaler.fit_transform(colonne_da_scalare) # fit_transform calcola media e deviazione standard e standardizza i dati
        df_scalato = pd.DataFrame(colonne_scalate, columns=colonne_da_scalare.columns) # ricreo il dataframe riaggiungendo le intestazioni
        df_sistemato = pd.concat([df_scalato, df_sistemato["Prezzo_Vendita"]], axis=1) # ricongiungo la colonna Prezzo_Vendita
        # vengono segnati nuovi outliers, ma non ci sono più outliers veri avendoli già eliminati
        return df_sistemato, scaler
    # faccio ritornare anche lo scaler per poterlo utilizzare in seguito per la riconversione della standardizzazione dei dati di test

    # metodo per individuazione correlazioni
    def individuazione_correlazioni(self):
        matrice_correlazione = self.dataframe_sistemato.corr()
        print("********** MATRICE DI CORRELAZIONE **********", matrice_correlazione.to_string(), sep="\n")
        # da 0 a 0.3 correlazione debole, da 0.3 a 0.7 correlazione media, da 0.7 a 0.9 correlazione forte, da 0.9 a 1 correlazione molto forte
        plt.figure(figsize=(16, 10))
        sns.heatmap(matrice_correlazione, annot=True, cmap = 'Spectral', fmt=".2f", linewidths=0.5)
        #annot = True per mostrare i valori all'interno dei quadrati, cmap = 'coolwarm' per cambiare il colore
        # fmt = ".2f" per mostrare i valori con due decimali
        # alternative a coolwarm sono: 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Spectral', 'turbo', 'rocket'
        # che stanno per scale di colore più o meno calde
        plt.xticks(rotation=30, ha="right") # ruotiamo le etichette sull'asse x di 30 gradi e le allineiamo a destra
        plt.title("Heatmap delle correlazioni")
        plt.show()
        # controllo correlazioni variabili - target
        self.verifica_correlazioni()

    # metodo per conferma correlazioni variabili (ALTERNATIVA AL PRECEDENTE MA RIDONDANTE, UNO O L'ALTRO SOLITAMENTE)
    def verifica_correlazioni(self):
        # predisposizione dizionario per informazioni
        risultati_verifica = {
            "variabile": [],
            "correlazione": [],
            "p-value": [],
            "p-value-ns": [] # in notazione non scientifica
        }
        # popolamento del dizionario
        for col in self.dataframe_sistemato.columns:
            if col != "Prezzo_Vendita":
                corr, p = pearsonr(self.dataframe_sistemato[col], self.dataframe_sistemato["Prezzo_Vendita"])
                risultati_verifica["variabile"].append(col) # inseriamo il nome della colonna
                risultati_verifica["correlazione"].append(corr) # inseriamo il valore di correlazione
                risultati_verifica["p-value"].append(p) # inseriamo il valore di p-value in notazione scientifica
                risultati_verifica["p-value-ns"].append(format(p, ".53f")) # inseriamo il valore di p-value in notazione non scientifica
        # trasformazione del dizionario in dataframe
        df_correlazione = pd.DataFrame(risultati_verifica)
        print("********** CORRELAZIONI VARIABILI-TARGET **********", df_correlazione.to_string(), sep="\n")

    # metodo per determinare la regressione lineare semplice sfruttando la variabile con correlazione migliore (Superficie_mq) e Prezzo_Vendita
    def regressione_lineare_semplice(self):
        # definizione target e regressore (y  e x)
        y = self.dataframe_sistemato[["Prezzo_Vendita"]].values.reshape(-1, 1) # il target lo scriviamo per convenzione y
        # il target è il Prezzo_Vendita. Il reshape serve per trasformare il vettore in una matrice.
        # Se avessimo una singola osservazione quel reshape con il -1, 1 ci mantiene comunque la struttura bidimensionale
        # lo si mette comunque per evitare problemi anche se ora con 2000 osservazioni non dovremmo averne
        # il codice per le regressioni lavora con array bidimensionali, quindi dobbiamo trasformare il vettore in una matrice
        x = self.dataframe_sistemato[["Superficie_mq"]].values.reshape(-1, 1) # il regressore lo scriviamo per convenzione x
        # creazione e addestramento semplificato del modello di regressione lineare
        regressione = LinearRegression() # creazione modello
        regressione.fit(x, y)
        # fit è il metodo per addestrare il modello, prende in input x e y e restituisce il modello addestrato
        # ottenimento punteggio del modello (prima ancora di fare predizioni)
        # vicino a 1 è un buon modello, vicino a 0 è un modello pessimo
        # un modello con R^2 pari a 1 non va comunque bene perché significa che il modello è troppo complesso e si è adattato troppo ai dati
        print("****** PUNTEGGIO MODELLO REGRESSIONE ********", regressione.score(x, y), sep="\n")
        # ottenimento retta di regressione
        retta_regressione = regressione.predict(x)
        # il valore in realtà è ancora standardizzato. Dobbiamo riportarlo alla scala originale
        # reinversione valori standardizzati colonnq Supercifie_mq
        col_index = self.dataframe_sistemato.columns.get_loc("Superficie_mq") # ottenimento indice colonna Superficie_mq
        x_reali = (x * self.scaler.scale_[col_index]) + self.scaler.mean_[col_index] # formula inversa di standardizzazione
        # scale è la deviazione standard, mean è la media, il _ indica che sono attributi dell'oggetto scaler
        # grafico modello
        plt.scatter(x_reali, y, label ="Osservazioni", s=1, color="blue") # s sta per size, dimensione dei punti
        plt.plot(x_reali, retta_regressione, color="red", label="Regressione Lineare", linewidth=1.1)
        plt.title("Regressione Lineare tra Superficie e Prezzo Vendita")
        plt.xlabel("Superficie (mq)")

        plt.ylabel("Prezzo di Vendita (Euro)")
        plt.show()


    # metodo per determinare regressione lineare multipla e ottenere un modello di previsione
    def regressione_lineare_multipla(self):
        # definizione target e regressori
        regressori = self.dataframe_sistemato.drop(["Prezzo_Vendita"], axis=1).columns # prendiamo tutte le colonne tranne Prezzo_Vendita
        y = self.dataframe_sistemato[["Prezzo_Vendita"]].values.reshape(-1, 1)
        # per la x ora abbiamo già una struttura bidimensionale stando utilizzando tutte le colonne meno Prezzo_Vendita
        x = self.dataframe_sistemato[regressori]
        # creazione e addestramento modello di regressione lineare multipla con un step preliminare:
        # suddivisione osservazioni dataframe in addestramento e test
        # con dataset grossi (dai 10k osservazioni in su usiamo una ripartizione delle osservazioni 90-10%
        # con dataset piccoli usiamo un 70-30%
        # in questo siamo nel mezzo quindi utilizziamo un 80-20%
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=42)
        # 0.2 è la percentuale di test
        # random_state è il seed per la randomizzazione, se non lo mettiamo ogni volta che eseguiamo il codice otteniamo una ripartizione diversa
        # mettendolo la partizione rimane uguale perché random state fissa il seed del generatore di numeri casuali
        # fa in modo che il criterio di disordinamento sia uguale in tutte le fasi di esecuzione
        # 42 in particolare è un numero scelto a caso, ma è un numero molto usato per convenzione
        # creazione e addestramento modello di regressione lineare multipla
        regressione = LinearRegression()
        regressione.fit(x_train, y_train)
        # predizione modello
        y_pred_train = regressione.predict(x_train)
        y_pred_test = regressione.predict(x_test)
        # valutazione modello
        print("****** VALUTAZIONE MODELLO REGRESSIONE LINEARE MULTIPLA ******")
        print(f"Punteggio del modello (test): {regressione.score(x_test, y_test):.4f}")
        print(f"Punteggio del modello (train): {regressione.score(x_train, y_train):.4f}")
        print(f"Errore Assoluto Medio (test): {mean_absolute_error(y_test, y_pred_test):.2f} Euro")
        # mean_absolute_error calcola l'errore medio tra i valori reali e le predizioni
        # l'errore medio è definito come la media della differenza tra i valori reali e le predizioni
        print(f"Errore Assoluto Medio (train): {mean_absolute_error(y_train, y_pred_train):.2f} Euro")
        print(f"Errore Quadratico Medio (test): {np.sqrt(mean_squared_error(y_test, y_pred_test)):.2f} Euro")
        # mean_squared_error calcola l'errore quadratico medio tra i valori reali e le predizioni
        # l'errore quadratico medio è definito come la media della differenza tra i valori reali e le predizioni al quadrato
        print(f"Errore Quadratico Medio (train): {np.sqrt(mean_squared_error(y_train, y_pred_train)):.2f} Euro")
        # i valori sono tutti coerenti tra loro
        # se avessi avuto un Punteggio test al 99% ed un punteggio train al 50% avrei avuto un problema di overfitting
        # se avessi avuto un Punteggio test al 50% ed un punteggio train al 99% avrei avuto un problema di underfitting
        # ISTOGRAMMA DISTRIBUZIONE ERRORI DI PREDIZIONE (test essendo più significativo)
        errori = y_test.flatten() - y_pred_test.flatten() # differenza tra prezzi reali e predizioni
        # flatten trasforma un array bidimensionale in un array monodimensionale per poterlo graficare
        plt.figure(figsize=(10, 6))
        plt.hist(errori, bins=50, color="red", alpha=0.7, edgecolor= "black")
        # bins è il numero di barre dell'istogramma, più è alto più l'istogramma è dettagliato
        # alpha è la trasparenza delle barre, più è basso più le barre sono trasparenti
        # edgecolor è il colore del bordo delle barre
        plt.axvline(x=0, color="blue", linestyle="--", linewidth=1.1)
        # per disegnare una linea verticale ad errore zero così da avere da una parte le sovrastime e dall'altra le sottostime
        plt.title("Distribuzione Errori di Predizione")
        plt.xlabel("Errore di Predizione (Euro)")
        plt.ylabel("Numero di Immobili")
        plt.show()
        # restituiamo il modello per poterlo utilizzare in seguito
        return regressione


    # pretodo per predire il valore di un immobile partendo dai suoi dati
    # in input passeremo un dizionario con i dati dell'immobile
    def predizione_valore(self, immobile):
        # creazione DataFrame per un nuovo immobile
        df_immobile = pd.DataFrame([immobile]) # singola osservazione quindi doppia parentesi quadra
        # standardizzazione variabili mediante scaler utilizzato per il modello
        df_immobile_scalato = self.scaler.transform(df_immobile)
        df_immobile_scalato = pd.DataFrame(df_immobile_scalato, columns=df_immobile.columns) # per riaggiungere le intestazioni
        # predizione valore immobile
        prezzo_predetto = self.regressione.predict(df_immobile_scalato)[0][0]
        # [0][0] per ottenere il valore effettivo, altrimenti avremmo un array bidimensionale
        # stampa rosultato
        print(f"Il prezzo predetto per l'immobile è di {prezzo_predetto:.2f} Euro")




# utilizzo modello
modello = ModelloHousing("../dataset/data_05.csv")
# modello.analisi_generali(modello.dataframe_sistemato)
# osserviamo che tutte le variabili sono quantitative (divise tra int e float) e non ci sono valori nulli
# I valori univoci non hanno senso da ricercare in quanto ci sono tutti valori differenti

# commento le due linee successive che da dopo standardizzazione non servono più
# modello.analisi_indici_statistici(modello.dataframe_sistemato)
# modello.individuazione_outliers(modello.dataframe_sistemato)
# se ci sono molti outliers, ai modelli di regressione lineare danno davvero fastidio
# in prima analisi però vediamo media e mediana molto vicine tra loro, quindi possiamo ipotizzare che non ci siano molti outliers
# per eliminare quei pochi che ci sono dobbiamo scegliere che indice considerare per sostituirli
# potremmo trovare i due limiti inferiori e superiori che definiscono gli outliers per usarli come valori di rimpiazzo e tenere al meglio la veridicità
# ho utilizzato i limiti nella creazione del dataframe sistemato che poi ho sostituito nel richiamo dei metodi

# ai modelli di machine learning fanno comunque schifo i valori categorici in scale differenti (unità di misura diverse)
# quindi dobbiamo fare una standardizzazione dei dati o una normalizzazione
# standardizzazione = sottrarre la media e dividere per la deviazione standard
# normalizzazione = sottrarre il minimo e dividere per la differenza tra massimo e minimo
# la standardizzazione è più usata, ma la normalizzazione è più robusta agli outliers

# predizione prezzo per nuovo immobile
nuovo_immobile = {
    "Superficie_mq": 85,
    "Num_Camere": 3,
    "Num_Bagni": 2,
    "Piano": 4,
    "Distanza_Metro_m": 500,
    "Rumorosita_Area_dB": 45,
    "Distanza_Tangenziale_m": 2500,
    "Età_Immobile": 20
}


nuovo_immobile_due = {
    "Superficie_mq": 160,
    "Num_Camere": 3,
    "Num_Bagni": 2,
    "Piano": 4,
    "Distanza_Metro_m": 5,
    "Rumorosita_Area_dB": 45,
    "Distanza_Tangenziale_m": 100,
    "Età_Immobile": 15
}

modello.predizione_valore(nuovo_immobile_due)