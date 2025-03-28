import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_laptops():
    base_url = "https://www.demoblaze.com/"
    page_url = "https://www.demoblaze.com/index.html"
    laptops = []
    
    while True:
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        items = soup.find_all("div", class_="card")
        for item in items:
            name = item.find("h4", class_="card-title").text.strip()
            price = item.find("h5").text.strip()
            description = item.find("p", class_="card-text").text.strip()
            
            laptops.append({
                "name": name,
                "price": price,
                "description": description
            })
        
        next_button = soup.find("button", id="next2")
        if next_button and "disabled" not in next_button.attrs.get("class", []):
            page_url = base_url + next_button["onclick"].split("'")[1]
            time.sleep(2)  # Prevent excessive requests
        else:
            break
    
    return laptops

def save_to_json(data, filename="laptops.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    laptops_data = scrape_laptops()
    save_to_json(laptops_data)
    print(f"Scraped {len(laptops_data)} laptops and saved to laptops.json")
