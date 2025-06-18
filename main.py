# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from generate_meme import get_meme_caption 

app = FastAPI()

class EmotionRequest(BaseModel):
    emotion: str

@app.get("/")
def read_root():
    return {"message": "Mood Meme Generator API is running!"}

@app.post("/generate-meme/")
def generate_meme(data: EmotionRequest):
    emotion = data.emotion
    caption = get_meme_caption(emotion)
    return {"caption": caption}
