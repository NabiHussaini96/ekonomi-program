from konto import Konto
from api import hämta_valutakurs
import json
konto = Konto()

print("1. Sätt in pengar")
print("2. Ta ut pengar")
print("3. Visa saldo")

val = input("Välj: ")

if val == "1":
    belopp = int(input("hur mycket vill du sätta in? "))
    konto.sätt_in(belopp)
elif val == "2":
    belopp = int(input("hur mycket vill du ta ut? "))
    konto.ta_ut(belopp)
elif val == "3":
    print("Saldo:", konto.visa_saldo())

data = {"saldo": konto.visa_saldo()}

with open("data.json", "w") as f:
    json.dump(data, f)

