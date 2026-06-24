from fastapi import FastAPI

from app.db.database import engine
from app.db.models import Base

from app.api.auth import router as auth_router

from app.api.conversation import router as conversation_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(conversation_router)

app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "AI Voice Agent Backend Running"
    }