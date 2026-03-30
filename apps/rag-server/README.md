# RAG Server

FastAPI + ChromaDB + Google Gemini 기반 RAG 서버

## 실행 방법

```bash
# 의존성 설치
uv sync

# 환경변수 설정
cp .env.example .env
# .env 파일에 GEMINI_API_KEY 입력

# 서버 실행
uv run uvicorn app.main:app --reload --port 8000
```

## API 엔드포인트

| Method | Path | 설명 |
|--------|------|------|
| GET | `/health` | 헬스체크 |
| POST | `/api/chat` | RAG 기반 채팅 |

## API 문서

서버 실행 후 http://localhost:8000/docs 에서 Swagger UI 확인 가능
