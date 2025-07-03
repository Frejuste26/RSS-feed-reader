import requests
from xml.etree import ElementTree as ET

def fluxReader(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        root = ET.fromstring(response.text)

        print(f"\n🔗 Flux: {url}\n" + "-" * 60)

        for item in root.iter('item'):
            titre = item.find('title').text if item.find('title') is not None else "Sans titre"
            description = item.find('description').text if item.find('description') is not None else "Pas de description"
            lien = item.find('link').text if item.find('link') is not None else "Pas de lien"

            print(f"📰 Titre       : {titre}")
            print(f"📄 Description : {description.strip()[:150]}...")
            print(f"🔗 Lien        : {lien}")
            print("-" * 60)

    except Exception as e:
        print(f"❌ Erreur pour l'URL {url} : {e}")

def main():
    print("=== Lecteur RSS Terminal ===")
    urls = []

    while True:
        url = input("Entrez l'URL d'un flux RSS (ou 'fin' pour démarrer) : ").strip()
        if url.lower() == 'fin':
            break
        urls.append(url)

    # ✅ La boucle ici, une fois que toutes les URLs sont collectées
    for url in urls:
        fluxReader(url)

if __name__ == "__main__":
    main()

