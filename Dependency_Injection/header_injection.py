'''
Injecting the Header method from fastapi into a get endpoint to retrieve the User-Agent of the request
'''

from fastapi import FastAPI, Header #This function takes the variable and turns it to another case, and retrieves data from the request object

app = FastAPI()

@app.get('/')
async def get_user_agent(user_agent : str = Header(...)):
    return {
        'User-Agent':user_agent
    }