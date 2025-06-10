from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()

@app.post('/register')
async def add_profile(name : str = Form(), password : str = Form(), profile_picture : UploadFile = File(...), resume = File(None)):
    return {
        'name': name,
        'password':password,
        'filename': profile_picture.filename,
        'resume' : resume.filename if resume else 'No document' 
    }

