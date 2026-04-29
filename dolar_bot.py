import requests
import time

TOKEN = "TOKEN"
CHAT_ID = "1531578994"

def dolar_kur():
    url = "https://open.er-api.com/v6/latest/USD"
    data = requests.get(url).json()
    return data["rates"]["TRY"]

def mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mesaj
    })

while True:
    kur = dolar_kur()
    print("Dolar:", kur)

    mesaj_gonder(f"💰 Günlük Dolar Kuru: {kur} TL")

    time.sleep(90400)