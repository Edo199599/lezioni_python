import pandas as pd
import matplotlib.pyplot as plt

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
    # moda variabili quantitative e categoriali
    for col in df.columns:
        #print(f"Moda colonna {col}:", df[col].mode())
        # anche mode ritorna una Series che ci presenta più informazioni
        print(f"Moda colonna {col}:", df[col].mode().iloc[0])
        # di tutte le info che la funzione mode() restituisce prendo la prima (il velore più frequente)
    # invocazione funzione per individuazione outliers
    print("------- Individuazione Outliers -------")
    for col in df_quantitative.columns:
        individuazione_outliers(df_quantitative, col)

# funzione per individuazione outliers nelle variabili quantitative
def individuazione_outliers(df, colonna):
    # calcolo differenza/range interquartile
    q1 = df[colonna].quantile(0.25)
    q3 = df[colonna].quantile(0.75)
    iqr = q3 - q1
    # calcolo limiti inferiore e superiore outliers
    limite_inferiore = q1 - 1.5 * iqr
    limite_superiore = q3 + 1.5 * iqr
    # questi limiti rappresentano i valori oltre i quali i dati sono considerati outliers
    # individuazione outliers della colonna per cui abbiamo invocato la funzione
    # quindi seleziono le righe/osservazioni con valori oltre i limiti. | è l'operatore OR logico
    outliers = df[(df[colonna] < limite_inferiore) | (df[colonna] > limite_superiore)]
    print(f"Nella colonna {colonna} sono presenti n° {len(outliers)} ({len(outliers)/len(df)*100}% di outliers)")
    # generazione grafico boxplot solo per Spese_mensili poiché le altre hanno valori Nan
    if colonna == "Spese_mensili":
        generazione_diagramma_indici(df, colonna, limite_superiore, limite_inferiore)


# funzione per generare un diagramma a scatola degli indici delle variabili quantitative
def generazione_diagramma_indici(df, colonna, limite_superiore, limite_inferiore):
    # potrei inserire questa funzione all'interno della funzione precedente
    # calcolo indici generali colonna
    indici_colonna = df[colonna].describe()
    # generazione grafico - non possiamo eseguirlo per reddito annuo ed età perché contengono valori Nan
    plt.boxplot(df[colonna])


    plt.text(x=1.08, y=indici_colonna["75%"], s=f"Terzo quartile: {indici_colonna['75%']}", color="b", fontsize=8)
    # 1.08 è la posizione sull'asse x del testo, 75% è la posizione sull'asse y all'altezza del terzo quartile
    # s è il testo da inserire, color è il colore del testo
    # le sigle colori più usate sono r = red, b = blue, g = green, k = black, y = yellow, m = magenta, c = cyan
    plt.text(x=1.08, y=indici_colonna["50%"], s=f"Mediana: {indici_colonna['50%']}", color="m", fontsize=8)
    plt.text(x=1.08, y=indici_colonna["25%"], s=f"Primo quartile: {indici_colonna['25%']}", color="k", fontsize=8)

    # rappresentazione massimo e minimo
    plt.text(x=1.08, y=indici_colonna["max"], s=f"Massimo Rilevato: {indici_colonna['max']}", color="c", fontsize=8)
    plt.text(x=1.08, y=indici_colonna["min"], s=f"Minimo Rilevato: {indici_colonna['min']}", color="g", fontsize=8)

    # rappresentazione limiti outliers
    plt.axhline(y=limite_superiore, color="r", linestyle="--", label="Limite Superiore Outliers")
    # le opzioni per linestyle sono: - = line, -- = dashed, -. = dashdot, : = dotted
    plt.text(x=1.08, y=limite_superiore+300, s=f"Limite Superiore Outliers: {limite_superiore}", color="r", fontsize=9)
    plt.axhline(y=limite_inferiore, color="r", linestyle="--", label="Limite Inferiore Outliers")
    plt.text(x=1.08, y=limite_inferiore -1000, s=f"Limite Inferiore Outliers: {limite_inferiore}", color="r", fontsize=9)
    # per modificare lo spessore della riga si può aggiungere il parametro linewidth = 2 (esempio). di default è 1

    # indicazioni testuali (titolo grafico e assi)
    plt.title(f"Analisi indici colonna {colonna}")
    plt.ylabel(colonna)

    # render grafico. in questo caso non serve il comando show() già incluso nel metodo boxplot
    plt.show()

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