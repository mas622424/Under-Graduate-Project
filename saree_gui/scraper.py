import requests
from bs4 import BeautifulSoup
import json

sarees = {
    "Banarasi": "https://en.wikipedia.org/wiki/Banarasi_sari",
    "Kanjeevaram": "https://en.wikipedia.org/wiki/Kanchipuram_sari",
    "Chanderi": "https://en.wikipedia.org/wiki/Chanderi_saree",
    "Bandhani": "https://en.wikipedia.org/wiki/Bandhani",
    "Sambalpuri": "https://en.wikipedia.org/wiki/Sambalpuri_saree"
}

def scrape_saree_info():
    saree_data = {}

    for name, url in sarees.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract first 3 non-empty paragraphs for better context
        paragraphs = soup.find_all("p")
        text = " ".join([p.text.strip() for p in paragraphs if p.text.strip()][:3])

        saree_data[name] = text if text else "No data available"

    # Save as JSON
    with open("sarees.json", "w", encoding="utf-8") as f:
        json.dump(saree_data, f, indent=4, ensure_ascii=False)

    return saree_data

if __name__ == "__main__":
    saree_data = scrape_saree_info()
    print("Scraped data saved to sarees.json")

