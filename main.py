from konto import Konto
from api import hämta_valutakurs
import json
konto = Konto()

belopp = int(input("Hur mycket vill du sätta in? "))
konto.sätt_in(belopp)
kurs= hämta_valutakurs()

if kurs:
    print ("Valutakurs USD till sek:", kurs)
print("Saldo:", konto.visa_saldo())

data = {"saldo": konto.visa_saldo()}

with open("data.json", "w") as f:
    json.dump(data, f)

