''' This program uses the middleware to get the request method, url path and time
    The middleware is the function between the client and the url operator it receives the request and the 
    function between the response and the client.
'''
from fastapi import FastAPI, Request
import time
logs = {}
app = FastAPI()

@app.middleware('http')
async def get_logs(request: Request, call_next):
    start_time = time.time()
    logs['request_method'] = request.method
    logs['url_path'] = request.url.path
    response = await call_next(request)
    end_time = time.time()
    logs['duration'] = round(end_time - start_time, 4)

    return response

@app.get('/logs')
async def return_logs():
    return logs

with open('logs.txt', 'w') as obj:
    obj.write(str(logs))

