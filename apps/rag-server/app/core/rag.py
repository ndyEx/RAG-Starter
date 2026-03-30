from app.config import settings
from app.core.embeddings import get_query_embedding
from app.services.vectordb import search_documents
from app.services.llm import generate_response


def query(question: str) -> dict:
    """RAG 파이프라인 실행: 질문 → 임베딩 → 검색 → LLM 응답 생성"""
    query_embedding = get_query_embedding(question)

    search_results = search_documents(
        query_embedding=query_embedding,
        top_k=settings.TOP_K,
    )

    context = "\n\n---\n\n".join(search_results["documents"][0]) if search_results["documents"][0] else ""

    answer = generate_response(question=question, context=context)

    sources = []
    if search_results["metadatas"] and search_results["metadatas"][0]:
        sources = [meta.get("source", "unknown") for meta in search_results["metadatas"][0]]

    return {
        "answer": answer,
        "sources": sources,
        "context_used": len(search_results["documents"][0]) if search_results["documents"][0] else 0,
    }
