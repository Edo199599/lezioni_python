"""
CALCOLARE IL PIANO DI AMMORTAMENTO DI UN FINANZIAMENTO (metodo calcolo italiano -> quota capitale costante e rata variabile)
Input utente (da recuperare):
- Importo finanziamento
- Durata finanziamento (in anni)
- Numero delle rate annuali (ad esempio 12 rate/anno
- Tasso di interesse (ad esempio il 5%)

Verifica input utente
Conversione input utente in valori numerici
Calcolo effettivo del piano di ammortamento
Stampa tabella del piano di ammortamento (Rata n.   Totale Rata   Quota interessi   Quota capitale  Rediduo da pagare)
"""

# funzione per acquisizione input utente
def acquisizione_input():
    importo_finanziamento = input("Inserisci l'importo del finanziamento >>> ").strip() #eliminiamo eventuali spazi vuoti inseriti per errore
    durata_funzionamento = input("Inserisci la durata del finanziamento in anni >>> ").strip()
    rate_annuali = input("Inserisci il numero delle rate di rimborso annuali >>> ").strip()
    tasso_interesse = input("Inserisci il tasso di interesse (ad esempio 5 per 5%) >>> ").strip().replace("%", "")
    return importo_finanziamento, durata_funzionamento, rate_annuali, tasso_interesse #ritorna una tupla con tutti i riferimenti

# funzione per controllo e conversione sicura degli imput
def conversione_input(valori):
    if all(valore.isnumeric() for valore in valori):
        #evito il ciclo for con all che restituisce vero se tutti i valori rispettano la condizione posta
        convertiti = [int(valore) for valore in valori] # LIST COMPREHENSION
        return convertiti
    else:
        return None

"""
ESTENSIONE DELLA LIST COMPREHENSION
convertiti = []
for valore in valori
    convertiti.append(int(valore)
"""

#funzione per calcolare il piano di ammortamento (lista bidimensionale)
def calcolo_ammortamnto(valori):
    # unpackaging della lista valori ricevuta
    importo, anni, rate_anno, tasso = valori
    # dati preliminari necessari per il calcolo
    totale_rate = rate_anno * anni
    tasso_effettivo = tasso / 100
    quota_capitale_rata = importo / totale_rate
    # definizione tabella piano ammortamento e riga di intestazione
    piano_ammortamento = [
        ["N° Rata", "Totale Rata", "Quota Capitale", "Quota Capitale", "Capitale Residuo"] # instestazione tabella
    ]
    # popolamento tabella
    for indice in range (1, totale_rate + 1):
        interessi_rata = ((importo * tasso_effettivo) * anni) / totale_rate
        totale_rata = quota_capitale_rata + interessi_rata
        capitale_residuo = importo - quota_capitale_rata
        riga_rata = [
            f"Rata n. {indice}",
            f"{totale_rata:.2f}", # .2f modalità che formatta il valore numero a due decimali ma esegue i calcoli su tutti
            f"{interessi_rata:.2f}",
            f"{quota_capitale_rata:.2f}",
            f"{capitale_residuo:.2f}"
        ]
        piano_ammortamento.append(riga_rata)
        importo = capitale_residuo
    return piano_ammortamento


# funzione per stampare il piano di ammortamento in formato tabellare
def stampa_ammortamento(piano_ammortamento):
    for riga in piano_ammortamento:
        for cella in riga:
            print("{:^20}".format(cella), end = " ") # struttura tabellare con colonne da 20 carattere con ^ sigificante tienile al centro
        print()


# funzione di avvio programma
def start():
    valori_acquisiti = conversione_input(acquisizione_input())
    # print(valori_acquisiti) inserito in fase di scrittura per verificare il funzionamento finora
    if valori_acquisiti:
        piano_ammortamento = calcolo_ammortamnto(valori_acquisiti)
        # non inserisco tutti i calcoli essendo lunghi ma creo una funziona ad hoc
        #print(piano_ammortamento) print di provare per vedere se funziona la funzione
        stampa_ammortamento(piano_ammortamento)
    else:
        print("Hai sbagliato ad inserire qualche dato. Riavvia e riprova")


start()