from fastapi import FastAPI, Header


app = FastAPI()

@app.get('/')
async def user_agent(user_agent : str = Header(...)):
    return f'well well well {user_agent}'
