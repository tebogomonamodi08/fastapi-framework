from fastapi import FastAPI #This is the class we will use to create the main object
from pydantic import BaseModel #This is the class we define the structure and types of our request body data 


app = FastAPI()

class Items(BaseModel):
    name : str
    price : float
    quantity : int

@app.post("/products/")
async def get_products(items : Items):
    return {
        'name' : items.name,
        'price' : items.price,
        'quantity' : items.quantity

    }