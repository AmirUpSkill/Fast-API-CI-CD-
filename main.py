from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
#Data Model 
class Item(BaseModel):
    id: int 
    name: str
    description: str
# In-memory "database"
items: List[Item]=[]

#Create an item
@app.post("/items/",response_model=Item) 
def create_item(item: Item):
    items.append(item)
    return item 
# Read all items
@app.get("/items/",response_model=List[Item])
def read_items():
    return items
