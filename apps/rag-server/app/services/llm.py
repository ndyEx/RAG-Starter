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


def generate_stock_analysis(ticker: str, market: str, context: str) -> str:
    """주식 종목 뉴스 기반 분석 리포트 생성"""
    model = genai.GenerativeModel(settings.GENERATION_MODEL)

    market_label = "한국(KRX)" if market == "KRX" else "미국(US)"

    prompt = f"""당신은 전문 주식 애널리스트입니다.
아래 {ticker} ({market_label}) 종목 관련 최신 뉴스 기사들을 분석하여 투자자에게 유용한 리포트를 작성해주세요.

## 분석 뉴스 데이터
{context}

## 작성 형식
1. **종목 요약**: 현재 이 종목의 핵심 이슈를 2-3줄로 요약
2. **긍정적 요인**: 뉴스에서 파악되는 호재 요인들
3. **부정적 요인**: 뉴스에서 파악되는 리스크 요인들 (없으면 "특이사항 없음")
4. **뉴스 감성 분석**: 전체적인 뉴스 톤이 긍정/중립/부정 중 어디에 해당하는지
5. **종합 의견**: 뉴스 데이터 기반 종합적인 시각

## 주의사항
- 뉴스 데이터에 기반해서만 분석하세요
- 투자 권유가 아닌 정보 제공 목적임을 명시하세요
- 한국어로 작성하세요

## 분석 리포트"""

    response = model.generate_content(prompt)
    return response.text
