from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items_db = {}
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 0.0

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in items_db:
        return {"item_id": item_id, "item": items_db[item_id]}
    return {"error": "Item not found"}

@app.post("/items/")
def create_item(item_id: int, item: Item):
    items_db[item_id] = item.dict()
    return {"message": "Item created successfully", "item": items_db[item_id]}

@app.get("/health")
def health_check():
    return {"status": "API is running"}

# Run with: uvicorn main:app --reload