import google.generativeai as genai

from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


def generate_response(question: str, context: str) -> str:
    """검색된 컨텍스트를 기반으로 Gemini LLM 응답 생성"""
    model = genai.GenerativeModel(settings.GENERATION_MODEL)

    prompt = f"""다음 컨텍스트를 기반으로 질문에 답변해 주세요.
컨텍스트에 답변할 수 있는 정보가 없다면, 정보가 부족하다고 솔직하게 말해 주세요.

## 컨텍스트
{context}

## 질문
{question}

## 답변"""

    response = model.generate_content(prompt)
    return response.text
