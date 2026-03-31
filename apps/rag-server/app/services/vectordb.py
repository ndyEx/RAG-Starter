import chromadb
from chromadb.api import ClientAPI

from app.config import settings

_client: ClientAPI | None = None


def get_client() -> ClientAPI:
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(path=settings.CHROMA_PERSIST_DIR)
    return _client


def get_collection() -> chromadb.Collection:
    client = get_client()
    return client.get_or_create_collection(
        name=settings.CHROMA_COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def add_documents(
    documents: list[str],
    embeddings: list[list[float]],
    metadatas: list[dict] | None = None,
    ids: list[str] | None = None,
) -> None:
    """문서를 VectorDB에 저장"""
    collection = get_collection()
    if ids is None:
        ids = [f"doc_{i}" for i in range(len(documents))]
    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )


def search_documents(
    query_embedding: list[float],
    top_k: int = 5,
) -> dict:
    """임베딩 벡터로 유사 문서 검색"""
    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    return results


def search_documents_with_filter(
    query_embedding: list[float],
    where_filter: dict,
    top_k: int = 5,
) -> dict:
    """메타데이터 필터링이 적용된 유사 문서 검색"""
    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        where=where_filter,
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    return results
