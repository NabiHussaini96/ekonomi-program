# Ekonomi Program 
- Detta är ett enkelt ekonomi-program skrivet i Python där användaren kan hantera sitt saldo.

## Funktioner
- Sätta in pengar
- Ta ut pengar
- Visa aktuellt saldo
- Hämta valutakurs (USD till SEK) via API
- Spara saldo i en JSON-fil
- Läsa saldo från fil vid start (persistent lagring)


## Hur programmet fungerar
När programmet startar:
 - Det försöker läsa tidigare saldo från data.json
 - Om ingen fil finns startar saldot på 0


Användaren får sedan en meny:
 - Sätt in pengar
 - Ta ut pengar
 - Visa saldo
 - Avsluta

Alla ändringar sparas automatiskt.



## Installation & körning
- Se till att Python är installerat
### Installera paket: 
 ```bash
pip install requests
```
### Kör programmet:
```bash
python main.py
```
## Filstruktur
- main.py – huvudprogram
- konto.py – klass för konto
- api.py – hämtar valutakurs
- data.json – sparar saldo


## Tekniker som används
- Python
- OOP (klasser och objekt)
- API-anrop
- JSON (filhantering)
- Git & GitHub



## Författare
Nabi Hussaini
