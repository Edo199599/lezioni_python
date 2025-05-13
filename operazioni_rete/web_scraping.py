import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql


# voglio recuperare titoli dei tutorial e link corrispondenti

try:
    # invio richiesta per ottenimento del documento HTML
    risposta = requests.get("https://www.gdapplicazioni.it/views/tutorial-gratuiti.php")
    # non abbiamo un json sta volta ma un html che viene paragonato più ad un testo
    # uso quindi risosta.text
    html = risposta.text
    # print(html)
    # istanziazione oggetto scraper (riesce ad eseguire un parsing del documento HTML)
    # dove parsing significa che riesce a leggere il documento HTML e a convertirlo in un oggetto
    scraper = BeautifulSoup(html, "html.parser")
    # passiamo allo scraper il documento HTML su cui lavorare e il parser da usare

    # ottenimento dei tag div contenenti i testi dei titoli
    # è però quasi tutto dentro i div quindi devo aggiungere un filtro ulteriore
    # guardando il file html ho visto che i titoli sono dentro un div con classe "col-md-9 mt-3"
    div_titoli = scraper.find_all(name="div", class_="col-md-9 mt-3")
    # print(div_titoli)
    # ottenimento dei testi dei tag div dei titoli
    titoli = []
    for div in div_titoli:
        titolo = div.get_text().strip()
        titoli.append(titolo)
    # print(titoli)

    # ora ricominciamo col parsing per cercare i link
    # ottenimento dei tag <a> contenenti i link
    # anche qui solo la a non basta ma vediamo che ogni link ha il suo bottone tutoria
    # la classe comune da usare come filtro è "btn btn-primary btn-sm mt-3"
    a_url = scraper.find_all(name="a", class_="btn btn-primary btn-sm mt-3")
    # print(a_url)
    # ottenimento dei valori href dei tag a contententi gli url dei tutorial
    urls= []
    for a in a_url:
        url = a.get("href")
        urls.append(url)
        # l'url non è il text che in questo caso sarebbe solo la parola "tutorial" sul pulsante
    # print(urls)

    # generazione dataframe con i dati acquisiti mediante scraping
    dataframe = pd.DataFrame({"titoli": titoli, "url": urls})
    print(dataframe.to_string())

    # registrazione intero dataframe nel database
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="scraping"
    )
    with connection.cursor() as cursor:
        sql = "INSERT INTO tutorials (titoli, urls) VALUES (%s, %s)"
        for _, row in dataframe.iterrows():
            cursor.execute(sql, tuple(row))
            # oppure
            # cursor.execute(sql, (row['titoli'], row['url']))
        connection.commit()
        # prima del run dobbiamo andare su phpmyadmin e creare il database scraping con la tabella tutorials

except Exception as e:
    print(e)

