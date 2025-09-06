from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Massage
from chat_bot import generate_response
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/chatbot/sdg")
async def chatbot(msg: Massage)-> Massage:
    await generate_response(msg)
    return msg