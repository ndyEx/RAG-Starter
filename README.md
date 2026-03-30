# RAG-Starter

Next.js + Python RAG 서버 기반의 Retrieval-Augmented Generation 스타터 프로젝트

## 아키텍처

```
Browser → Next.js (Frontend + API Routes) → Python RAG Server → ChromaDB
                                                    ↓
                                              Google Gemini
```

## 기술 스택

| 영역 | 기술 |
|------|------|
| Frontend / BFF | Next.js (App Router, TypeScript) |
| RAG Server | Python, FastAPI |
| Vector DB | ChromaDB |
| LLM / Embedding | Google Gemini |
| 패키지 관리 | pnpm (web), uv (rag-server) |

## 프로젝트 구조

```
├── apps/
│   ├── web/            # Next.js 풀스택 앱
│   └── rag-server/     # Python RAG 서버
├── .gitignore
└── README.md
```

## 시작하기

### 1. Next.js 앱

```bash
cd apps/web
pnpm install
pnpm dev
```

### 2. RAG 서버

```bash
cd apps/rag-server
cp .env.example .env
# .env 파일에 GEMINI_API_KEY 입력

uv sync
uv run uvicorn app.main:app --reload --port 8000
```

## 환경변수

### RAG Server (`apps/rag-server/.env`)

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `GEMINI_API_KEY` | Google Gemini API 키 | - |
| `EMBEDDING_MODEL` | 임베딩 모델 | `models/embedding-001` |
| `GENERATION_MODEL` | 생성 모델 | `gemini-2.0-flash` |
| `CHROMA_PERSIST_DIR` | ChromaDB 저장 경로 | `./chroma_db` |
| `TOP_K` | 검색 결과 수 | `5` |