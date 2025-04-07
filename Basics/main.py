from fastapi import FastAPI #import the FastAPI class to create the main object

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
]

app = FastAPI() #An instance of the FastAPI class(main object)

@app.get('/books') #A decorator to extend the get method from the FastAPI class and a an endpoint
async def get_books(author : str = None, genre : str = None):
    results = books
    if author!=None or genre!=None:
        if author:
            results = [item  for item in results if item['author'].lower()==author.lower()]
        if genre:
            results = [item for item in results if item['genre'].lower()==genre.lower()]
        return results
    else :
        return results
