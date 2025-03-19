import pandas as pd

#prima cosa da fare con un dataframe è ottenere le sue info generali
def analisi_generali(df):
    # print("Dataframe Completo: ", df, sep="\n") # stampa il dataframe con i ... in mezzo se è troppo grande scrivendo [n righe x m colonne]
    # print("Dataframe Completo: ", df.to_string(), sep="\n") # rappresentazione testuale completa (può essere inutile per dataframe molto grandi)
    # stampa Nan se il dato è mancante. Nan = Not a Number
    # solitamente si preferisce stampare come segue:
    print("Prime cinque osservazioni:", df.head().to_string(), sep="\n")
    print("Ultime cinque osservazioni:", df.tail().to_string(), sep="\n")
    print("Informazioni generali:")
    df.info() # ci dice il numero di righe, colonne, il tipo di dato, il numero di valori non nulli e la memoria utilizzata

# funzione per effettuare analisi delle singole colonne (variabili)
def scomposizione_dataframe_colonne(df):
    print("Scomposizione in colonne:")
    for colonna in df.columns: # per ogni colonna del dataframe
        print(f"Colonna {colonna}:", df[colonna], type(df[colonna]), sep="\n") # stampa il nome della colonna, i valori e il tipo di dato
    # il type delle singole colonne è una serie (Series), ovvero una lista con un indice (come un dizionario)
    # il type dell'intero dataframe è un dataframe
        print("Valori Colonna:")
        for valore in df[colonna]:
            print(valore, type(valore)) # stampa il valore e il tipo di dato

# le righe vengono chiamate osservazioni, le colonne vengono chiamate variabili
# definiamo una funzione per analisi delle singole righe (osservazioni)
def scomposizione_dataframe_righe(df):
    print("Scomposizione in righe:")
    for index, obs in df.iterrows(): # iterrows() restituisce l'indice e l'osservazione di appartenenza
        print(f"Riga {index}", obs, type(obs), sep="\n") # stampa l'indice, l'osservazione e il tipo di dato
        # anche il type delle singole righe è una serie (Series)
        print("Valori Riga:")
        for valore in obs:
            print(valore, type(valore)) # stampa il valore e il tipo di dato

# funzione per filtro dataframe su colonne (prendo intere colonne e creo un nuovo dataframe)
def filtro_dataframe_colonne(df):
    df_filtrato_colonne = df[["Reddito_annuo", "Soddisfazione"]] # seleziona solo le colonne Reddito_annuo e Soddisfazione
    print(df_filtrato_colonne.to_string())
    # questo df è un sottoinsieme del df originale
    # per una maggiore sicurezza dovremmo invocare il metodo .copy() per creare una copia del dataframe originale

# funzione per filtro dataframe su valori osservazioni (
def filtro_dataframe_osservazioni(df):
    valori = ["Laurea triennale", "Laurea magistrale"] # ipotizzo analisi su studenti universitari
    df_filtrato_osservazioni = df[df["Titolo di studio"].isin(valori)] # seleziona solo le righe con i valori presenti nella lista precedente
    print(df_filtrato_osservazioni.to_string())
    # controlli che ha senso fare su valori qualitativi

# funzione per controllo valori univoci variabili categoriali (qualitative - per evitare errori della funzione precedente)
# funzione utile per capire se una variabile è categoriale o meno (se ha pochi valori univoci è categoriale)
def analisi_valori_univoci(df):
    df_categoriali = df.drop(["Età", "Reddito_annuo", "Spese_mensili"], axis = 1)
    # axis = 1 indica che sto eliminando colonne altrimenti 0 per le righe
    # se mettessi inplace = True eliminerei le colonne dal dataframe originale non solo da quello temporaneo
    # elimino le variabili quantitative invece scegliere le qualitative
    for col in df_categoriali.columns:
        print(f"In colonna {col} abbiamo {df_categoriali[col].nunique()} valori univoci:")
        #nunique() restituisce il numero di valori univoci presenti nella colonna
        for value in df_categoriali[col].unique():
            print(value)
        # unique() restituisce i valori univoci presenti nella colonna
        # printa anche Nan ma non li conta come valori univoci

# funzione per analisi indici statistici per le variabili quantitative
def analisi_indici_statistici(df):
    # indici generali delle variabili quantitative del dataframe
    indici_generali = df.describe()
    print("Indici statistici generali delle variabili quantitative:", indici_generali, sep="\n")
    # esegue solo per le variabili quantitative riconoscendole automaticamente
    # ATTENZIONE: la deviazione standard è calcolata sul campione e non sulla popolazione
    # se ci fosse una colonna numerica da non considerare dovrei fare un filtro come sopra:
    # estrazione variabili quantitative
    df_quantitative = df.drop(["Soddisfazione", "Stato_civile", "Titolo di studio"], axis=1)
    # deviazione standard sulla popolazione
    for col in df_quantitative:
        deviazione_standard_pop = df_quantitative[col].std(ddof=0)
        # ddof è un parametro che indica il grado di libertà
        # se 0 calcola la deviazione standard sulla popolazione, se 1 calcola la deviazione standard sul campione
        print(f"Deviazione standard sulla popolazione di {col}: {deviazione_standard_pop}")

# generazione dataframe da file csv
dataframe = pd.read_csv("../dataset/data_03.csv")


# invocazioni delle funzioni
# analisi_generali(dataframe)
# scomposizione_dataframe_colonne(dataframe)
# scomposizione_dataframe_righe(dataframe)
# filtro_dataframe_colonne(dataframe)
# filtro_dataframe_osservazioni(dataframe)
# analisi_valori_univoci(dataframe)
analisi_indici_statistici(dataframe)