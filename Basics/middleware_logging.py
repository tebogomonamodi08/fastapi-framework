''''
Requirements:
Log:
-Request URL
-Time it took to respond (in ms)

Sample - Request to http://127.0.0.1:8000/items took 14.21ms
'''

from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware('http')
async def get_header(request : Request, call_next):

    '''This function will receive the request object and get the URL of the the request and time the response'''
    request_start = time.time()
    response = await call_next(request)
    duration = round((time.time() - request_start) * 1000, 2)
    print(f'Request to {request.url} took {duration}ms')
    

    return response

@app.get('/')
async def get_info():
    return {'message':'Yep this is the info.'}
   
    
    



