from konto import Konto
from api import hämta_valutakurs
import json
konto = Konto()

konto.sätt_in(100)
kurs= hämta_valutakurs()

if kurs:
    print ("Valutakurs USD till sek:", kurs)
print("Saldo:", konto.visa_saldo())

data = {"saldo": konto.visa_saldo()}

with open("data.json", "w") as f:
    json.dump(data, f)

