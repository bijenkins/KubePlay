from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Customer(BaseModel):
    id: int
    name: str
    label: Optional[List[str]]
    engine: str
    output: str

class Product(BaseModel):
    name: str
    description: Optional[str] = None


@app.get("/")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
async def read_root():
    
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Product, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    
    if q:
        result.update({"q": q})
    return result