import requests

# Liste von API-URLs
urls = [
    "https://dgm.stac.lgln.niedersachsen.de/collections/dgm1/items/dgm1_32_374_5950_1_ni_2022",
    "https://dgm.stac.lgln.niedersachsen.de/collections/dgm1/items/dgm1_32_374_5949_1_ni_2022",
    # Weitere URLs hinzufügen...
]

# Liste für extrahierte href-Links
extracted_urls = []

# Durch die URLs iterieren
for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # JSON-Antwort parsen

        # URL aus "assets" extrahieren
        extracted_url = data.get("assets", {}).get("dgm1-tif", {}).get("href", None)

        if extracted_url:
            extracted_urls.append(extracted_url)  # URL zur Liste hinzufügen
        else:
            print(f"Keine URL in den Assets gefunden für: {url}")
    else:
        print(f"Fehler beim Abrufen der API {url}: {response.status_code}")

# Ergebnis ausgeben
print("Extrahierte URLs:", extracted_urls)
