from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.db.models import Base
from app.api.auth import router as auth_router
from app.api.conversation import router as conversation_router
from app.api.chat import router as chat_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Voice Agent API")

# Allow React frontend to talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(conversation_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "AI Voice Agent Backend Running"
    }