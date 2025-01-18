from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from orchestrated_agent import OrchestratedAgent

router = APIRouter()
agent = OrchestratedAgent()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
async def chat(request: ChatRequest):
    """Handle chat requests using the orchestrated agent."""
    try:
        response = agent.get_response(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
