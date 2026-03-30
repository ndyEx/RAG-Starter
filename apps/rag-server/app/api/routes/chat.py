from fastapi import APIRouter
from pydantic import BaseModel

from app.core.rag import query

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    context_used: int


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """RAG 기반 채팅 엔드포인트"""
    result = query(question=request.message)
    return ChatResponse(**result)
