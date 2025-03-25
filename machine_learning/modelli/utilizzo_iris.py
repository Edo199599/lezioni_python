import joblib # per poter recuperare il modello e lo scaler
import pandas as pd


# dichiarazione di un nuovo fiore (che potrebbe essere da input utente)
new_flower = {
    "sepal_length": 5.8,
    "sepal_width": 2.7,
    "petal_length": 4.1,
    "petal_width": 1.0
}

# conversione del dizionario in un DataFrame
df_nuovo_fiore = pd.DataFrame([new_flower]) # parentesi quadre in quanto singola osservazione

#recupero modello predittivo e scaler dai file
modello_predittivo = joblib.load("modello_iris.joblib")
scaler_modello = joblib.load("scaler_iris.joblib")

# standardizzazione del nuovo fiore
df_nuovo_fiore_std = scaler_modello.transform(df_nuovo_fiore)

print(f"Classe Predetta: {modello_predittivo.predict(df_nuovo_fiore_std)[0]}")
# il [0] serve a estrarre il valore dalla lista che la funzione predict() restituisce. Ovvero il nome