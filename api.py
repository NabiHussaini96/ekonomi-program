import requests
def hämta_valutakurs():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["rates"]["SEK"]
        else:
            return None
    except Exception:
        print("Fel vid API-anrop")
        return None
