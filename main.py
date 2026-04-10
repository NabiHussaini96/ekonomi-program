from konto import Konto
from api import hämta_valutakurs
import json
try:    
    with open("data.json", "r") as f:
        data = json.load(f)
        saldo = data.get("saldo", 0)
except FileNotFoundError:
    saldo = 0
konto = Konto(saldo)

while True:
    print("1. Sätt in pengar")
    print("2. Ta ut pengar")
    print("3. Visa saldo")
    print("4. Avsluta")
    val = input("Välj: ")
    if val == "1":
        belopp = int(input("hur mycket vill du sätta in? "))
        konto.sätt_in(belopp)
    elif val == "2":
        belopp = int(input("hur mycket vill du ta ut? "))
        konto.ta_ut(belopp)
    elif val == "3":
        print("Saldo:", konto.visa_saldo())
    elif val == "4":
        print("programmet avslutas")
        break
    else:
        print("Ogiltigt val")
        
    data = {"saldo": konto.visa_saldo()}
    with open("data.json", "w") as f:
     json.dump(data, f)
     