import google.generativeai as genai

from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


def get_embeddings(texts: list[str]) -> list[list[float]]:
    """텍스트 리스트를 벡터 임베딩으로 변환"""
    result = genai.embed_content(
        model=settings.EMBEDDING_MODEL,
        content=texts,
        task_type="retrieval_document",
    )
    return result["embedding"]


def get_query_embedding(query: str) -> list[float]:
    """검색 쿼리를 벡터 임베딩으로 변환"""
    result = genai.embed_content(
        model=settings.EMBEDDING_MODEL,
        content=query,
        task_type="retrieval_query",
    )
    return result["embedding"]
