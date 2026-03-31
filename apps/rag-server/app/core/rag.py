from app.config import settings
from app.core.embeddings import get_query_embedding
from app.services.vectordb import search_documents, search_documents_with_filter
from app.services.llm import generate_response, generate_stock_analysis


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


def stock_query(ticker: str, market: str = "KRX") -> dict:
    """주식 종목 분석 파이프라인: 종목코드 기반 필터링 검색 → 분석 리포트 생성"""
    question = f"{ticker} 종목의 최근 뉴스를 분석해주세요"
    query_embedding = get_query_embedding(question)

    where_filter = {
        "$and": [
            {"ticker": {"$eq": ticker}},
            {"market": {"$eq": market}},
        ]
    }

    search_results = search_documents_with_filter(
        query_embedding=query_embedding,
        where_filter=where_filter,
        top_k=settings.TOP_K,
    )

    docs = search_results["documents"][0] if search_results["documents"] and search_results["documents"][0] else []
    context = "\n\n---\n\n".join(docs) if docs else ""

    if not context:
        return {
            "answer": f"{ticker} ({market}) 관련 저장된 뉴스 데이터가 없습니다. 먼저 /api/stock/ingest로 데이터를 수집해주세요.",
            "sources": [],
            "context_used": 0,
        }

    answer = generate_stock_analysis(ticker=ticker, market=market, context=context)

    sources = []
    if search_results["metadatas"] and search_results["metadatas"][0]:
        sources = [meta.get("source", "unknown") for meta in search_results["metadatas"][0]]

    return {
        "answer": answer,
        "sources": sources,
        "context_used": len(docs),
    }
