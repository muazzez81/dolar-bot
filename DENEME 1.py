import requests
import time

TOKEN = "8785816507:AAEWLgcKncfBJiClDQ2X3RcP-u5bECw-yPw"
CHAT_ID = "1531578994"

eski = None

def mesaj_gonder(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

while True:
    data = requests.get("https://open.er-api.com/v6/latest/USD").json()
    dolar = data["rates"]["TRY"]

    print("Dolar:", dolar)

    if eski is not None and dolar != eski:
        mesaj_gonder(f"⚠️ Dolar değişti: {dolar} TL")

    eski = dolar
    time.sleep(10)