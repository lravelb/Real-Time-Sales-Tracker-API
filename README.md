# Real-Time Sales Tracker API

A small simulation project that receives real-time sale events and uploads them to AWS S3 using FastAPI.

---

## Project Structure

```
realtime-sales-tracker/
├── app/
│ └── main.py # FastAPI application
├── scripts/
│ ├── get_products.py # Downloads product catalog from DummyJSON
│ └── simulate_events.py # Sends fake sales to the API
├── data/
│ └── products.json # Product data used for simulation
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

1. **Create a virtual environment:**

```
python -m venv venv
venv\Scripts\activate
```

2. **Install dependencies:**

```
pip install -r requirements.txt
```

3. **Run the API:**

```
uvicorn app.main:app --reload --port 8080
```

4. **Simulate Sales:**

```
python scripts/simulate_events.py
```

---

## Next Steps (Planned)

- Process the data stored in S3  
- Build dashboards in Power BI  
- Perform analytics on user behaviour and product categories  
