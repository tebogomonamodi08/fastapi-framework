from fastapi import FastAPI

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
]

app = FastAPI()
results = books
@app.get('/books')
async def paginate(author: str = None, genre : str = None, title : str = None, skip: int = 0, limit : int =10):
    results = books
    if author:
        results = [book for book in results if book['author'].lower()==author.lower()]
    if genre:
        results = [book for book in results if book['genre'].lower()==genre.lower()]

    if title:
        results = [book for book in results if book['title'].lower()==title.lower()]
    return results[skip:limit]
        
