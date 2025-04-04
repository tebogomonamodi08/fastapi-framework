from fastapi import FastAPI
from enum import Enum

class Movies(str, Enum):
   action= "action"
   comedy = "comedy"
   drama = "drama"
   horror= "horror"

rating = {
   "action": "PG-13",
    "comedy": "PG",
    "drama": "R",
    "horror": "NC-17",
}

app = FastAPI()

@app.get('/rating/{movies}')
async def get_rating(movies : Movies):
   return {
      'movies': movies.name,
      'rating': rating[movies.name]
   }