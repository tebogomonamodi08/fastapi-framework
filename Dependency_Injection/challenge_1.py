'''
Challenge 1: Pagination Dependency
Create a dependency that accepts two query parameters: skip and limit, both integers. Use them 
to return a slice of a list of 100 items (e.g., "Item 1" to "Item 100"). 
Inject this dependency into a GET route to return paginated results.


'''

from fastapi import FastAPI, Depends


app = FastAPI()

items = ['item '+ str(x) for x in range(1,101)]

async def pagination(limit: int = 10, skip: int = 0 )-> tuple[int,int]:
    if limit>skip:
        return (limit,skip)
    else:
        return (10,0)

@app.get('/')
async def get_items(p: tuple[int,int] = Depends(pagination)):
    limit, skip = p
    return {
        'items' : items[skip:limit]
    }