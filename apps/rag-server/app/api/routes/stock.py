from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.rag import stock_query
from app.core.embeddings import get_embeddings
from app.services.vectordb import get_collection, add_documents
from app.services.news import fetch_news

router = APIRouter()


class StockAnalyzeRequest(BaseModel):
    ticker: str
    market: str = "KRX"  # "KRX" 또는 "US"


class StockAnalyzeResponse(BaseModel):
    ticker: str
    market: str
    analysis: str
    sources: list[str]
    news_count: int


class StockIngestResponse(BaseModel):
    ticker: str
    market: str
    ingested_count: int
    message: str


@router.post("/stock/analyze", response_model=StockAnalyzeResponse)
async def analyze_stock(request: StockAnalyzeRequest):
    """종목 분석 요청 — VectorDB에서 관련 뉴스 검색 후 Gemini가 분석"""
    ticker = request.ticker.upper()
    market = request.market.upper()

    if market not in ("KRX", "US"):
        raise HTTPException(status_code=400, detail="market은 'KRX' 또는 'US'만 가능합니다")

    result = stock_query(ticker=ticker, market=market)

    return StockAnalyzeResponse(
        ticker=ticker,
        market=market,
        analysis=result["answer"],
        sources=result["sources"],
        news_count=result["context_used"],
    )


@router.post("/stock/ingest", response_model=StockIngestResponse)
async def ingest_stock_news(request: StockAnalyzeRequest):
    """뉴스 데이터를 VectorDB에 저장"""
    ticker = request.ticker.upper()
    market = request.market.upper()

    news_list = await fetch_news(ticker=ticker, market=market)

    if not news_list:
        raise HTTPException(status_code=404, detail="수집된 뉴스가 없습니다")

    documents = [f"[{n['source']}] {n['title']}\n{n['content']}" for n in news_list]
    metadatas = [
        {
            "ticker": ticker,
            "market": market,
            "source": n["source"],
            "title": n["title"],
            "published_at": n["published_at"],
        }
        for n in news_list
    ]
    ids = [f"{ticker}_{market}_{i}" for i in range(len(documents))]

    embeddings = get_embeddings(documents)
    add_documents(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )

    return StockIngestResponse(
        ticker=ticker,
        market=market,
        ingested_count=len(documents),
        message=f"{ticker} 관련 뉴스 {len(documents)}건이 VectorDB에 저장되었습니다",
    )


@router.get("/stock/status")
async def stock_status():
    """VectorDB에 저장된 데이터 현황 조회"""
    collection = get_collection()
    count = collection.count()

    return {
        "total_documents": count,
        "collection_name": collection.name,
    }
