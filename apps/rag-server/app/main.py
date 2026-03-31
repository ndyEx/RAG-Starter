from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.routes import chat, stock

app = FastAPI(
    title="RAG Server",
    description="RAG API server with ChromaDB and Google Gemini",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")
app.include_router(stock.router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
