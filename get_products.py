import requests
import json

# Fetch product catalog from DummyJSON API
url = "https://dummyjson.com/products?limit=100"
response = requests.get(url)

if response.status_code == 200:
    products = response.json()["products"]

    # Save product data to local JSON file
    with open("data/products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(products)} products to data/products.json")
else:
    print(f"Failed to fetch products. Status code: {response.status_code}")
    
