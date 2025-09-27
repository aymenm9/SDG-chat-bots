import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Massage
from chat_bots import SDG_chatbot, Podcast_chatbot, EVENT_chatbot
from contextlib import asynccontextmanager
from models_manager import Models_manager
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    
    yield
    # Clean up the ML models and release the resources
    Models_manager.save_state()
app = FastAPI(lifespan=lifespan)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Secure CORS - replace the ["*"] with your domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://skills-lab.setif-developers-club.com", 
        "https://sdg-chat-bots-server.onrender.com",
        "http://localhost:3000",  # for development
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
@limiter.limit("100/hour")
def read_root():
    return {"Hello": "World"}


@app.post("/api/chatbot/sdg")
@limiter.limit("100/hour")
@limiter.limit("10/minute")
async def sdg_chatbot(msg: Massage)-> Massage:
    return await SDG_chatbot(msg)

@app.post("/api/chatbot/event")
@limiter.limit("100/hour")
@limiter.limit("10/minute")
async def event_chatbot(msg: Massage)-> Massage:
    return await EVENT_chatbot(msg)

@app.post("/api/chatbot/podcast")
@limiter.limit("100/hour")
@limiter.limit("10/minute")
async def podcast_chatbot(msg: Massage)-> Massage:
    return await Podcast_chatbot(msg)