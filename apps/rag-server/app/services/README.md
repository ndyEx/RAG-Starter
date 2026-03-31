# 💾 Services (데이터 접근 및 외부 시스템 연동 계층)

이 폴더는 **데이터베이스나 외부 API 등 "바깥" 세상과 통신하는 전담 부서**입니다.

주로 **Spring의 `@Repository`** 나 의존성을 주입받아 쓰는 **외부 통신 클라이언트(OpenFeign, RestTemplate)** 의 역할을 합니다.

- `vectordb.py`: ChromaDB 저장소에 접근해 데이터를 쓰고 읽는 기능
- `llm.py`: Google Gemini API 서버로 통신을 보내 텍스트를 받아오는 기능
- `news.py`: 외부 뉴스 API 서버에서 뉴스 기사를 가져오는 기능
