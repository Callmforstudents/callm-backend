from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()
@app.get("/")
def health():
    return {"status": "ok"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://callmforstudents.github.io"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

class ChatRequest(BaseModel):
    message: str
@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Je bent Call'm, een sparringpartner voor MBO studenten."},
            {"role": "user", "content": req.message}
        ],
    )
    return {"reply": response.choices[0].message.content}


