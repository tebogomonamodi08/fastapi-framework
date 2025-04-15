'''This is a products CRUD application with different endpointd'''
from fastapi import FastAPI  #This is a class used to institiate the main object
from pydantic import BaseModel #This class will be use to validate and define the structure of the request body

app = FastAPI()

stock = {}

class Items(BaseModel):
    product_id : int
    product_name : str
    price : float
    availability : bool = True

#Index endpoint to view all the products(home)
@app.get('/')
async def index():
    return stock

#Create a new product endpoint(Create)
@app.post('/create')
async def create(items : Items ):
    stock[items.product_id] = items.dict()
    return {f'product {items.product_id} succesfully created'}


#Update a product
@app.put('/update')
async def update(items : Items):
    if items.product_id in stock:
        stock[items.product_id] = items.dict()
        return f'Product ID {items.product_id} has been updated'
    else:
        return f'Product ID {items.product_id} is not found'
    
    
#Delete an product from the dictionary
@app.delete('/delete')
async def delete(items: Items):
    if items.product_id in stock:
        del stock[items.product_id]
        return f'{items.product_name} has been succefully deleted.'
    else:
        return f'{items.product_id} is not found.'


@app.get('/search/{name}')
async def find(name: str):
    results =  [info for info in stock.values() if info['product_name'].lower()==name.lower()]
    return results or {'message': f'{name} is not found'}

@app.get('/filter')
async def filter(skip: int, limit: int, availability : bool = None):
    if skip and limit and availability:
        result = [info for info in stock.values() if skip<info['price']<limit and info['availability']==True]
    elif skip and limit and not availability:
        result = [info for info in stock.values() if skip<info['price']<limit]
    else:
        result = [info for info in stock.values() if info['availability']==True]
        
    return result or {'message' : 'No such range'}