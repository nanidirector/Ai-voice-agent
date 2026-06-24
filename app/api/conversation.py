from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Conversation, User
from app.core.deps import get_current_user

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)

@router.post("/")
def create_conversation(
    title: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    conversation = Conversation(
        title=title,
        user_id=current_user.id
    )
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return {
        "id": conversation.id,
        "title": conversation.title
    }