from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import boto3
import uuid
import json

app = FastAPI()

# Define the structure of a sale event
class SaleEvent(BaseModel):
    timestamp: str
    product_id: int
    category: str
    price: float
    user_id: str

# Temporary in-memory storage
sales = []

s3 = boto3.client("s3")
BUCKET_NAME = "realtime-sales"

@app.get("/")
def read_root():
    return {"message": "Real-Time Sales Tracker API!"}

@app.post("/sale")
def receive_sale(event: SaleEvent):
    sales.append(event)
    print(f"New sale received: {event}")

    # upload to S3
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"sale_{timestamp}_{uuid.uuid4().hex}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=event.json(),
        ContentType="application/json"
    )

    return {"message": "Sale event received and uploaded to S3", "filename": filename}

