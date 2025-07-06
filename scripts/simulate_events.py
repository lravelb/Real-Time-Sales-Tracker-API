import json
import random
import time
import requests
from datetime import datetime

# Load product catalog
with open("data/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

API_URL = "http://127.0.0.1:8080/sale"

# simulate a single sale
def send_fake_sale():
    product = random.choice(products)
    event = {
        "timestamp": datetime.now().isoformat(),
        "product_id": product["id"],
        "category": product["category"],
        "price": product["price"],
        "user_id": f"user_{random.randint(100, 999)}"
    }

    try:
        response = requests.post(API_URL, json=event)
        if response.status_code == 200:
            print(f"Sale sent: {event['product_id']} - {event['category']}")
        else:
            print(f"Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Error sending event: {e}")

# Run simulation
print("Starting real-time sale simulation...")
for _ in range(10):  # send 10 events
    send_fake_sale()
    time.sleep(2)  # wait 2 seconds between events
