from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from util.orchestrated_agent import generate_chat_response


router = APIRouter()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
async def chat(request: ChatRequest):
    """Handle chat requests."""
    try:
        response = generate_chat_response(request.prompt)
        return {"response": response}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))