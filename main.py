import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Massage
from chat_bots import SDG_chatbot
from contextlib import asynccontextmanager
from models_manager import Models_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    
    yield
    # Clean up the ML models and release the resources
    Models_manager.save_state()
app = FastAPI(lifespan=lifespan)
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
    new_msg = await SDG_chatbot(msg)
    return new_msg