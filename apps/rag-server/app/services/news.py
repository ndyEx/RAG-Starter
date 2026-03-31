"""
뉴스 API 인터페이스 모듈
실제 뉴스 API 연동 전까지 더미 데이터로 동작
"""

from datetime import datetime, timedelta
import random


DUMMY_KRX_NEWS = [
    {
        "title": "[속보] 삼성전자, 2분기 영업이익 시장 예상 상회",
        "content": "삼성전자가 2분기 영업이익 10조 4000억원을 기록하며 시장 컨센서스를 크게 상회했다. HBM(고대역폭메모리) 수요 급증이 실적 개선의 핵심 동력으로 작용했다. 증권가에서는 하반기에도 AI 반도체 수요 확대에 따른 실적 성장이 지속될 것으로 전망하고 있다.",
        "source": "한국경제",
        "published_at": "2026-03-30T09:00:00",
    },
    {
        "title": "외국인 투자자, 삼성전자 3거래일 연속 순매수",
        "content": "외국인 투자자들이 삼성전자를 3거래일 연속 순매수하며 수급 개선 신호를 보이고 있다. 이번 주 누적 순매수 규모는 약 5,000억원에 달한다. 글로벌 AI 투자 확대 기조 속에서 반도체 섹터 전반에 대한 긍정적 시각이 반영된 것으로 분석된다.",
        "source": "매일경제",
        "published_at": "2026-03-29T14:30:00",
    },
    {
        "title": "삼성전자, 차세대 HBM4 양산 일정 앞당긴다",
        "content": "삼성전자가 차세대 고대역폭메모리 HBM4의 양산 일정을 당초 계획보다 앞당기기로 했다. NVIDIA와의 협력을 통해 AI 가속기용 메모리 공급을 확대할 계획이다. 업계에서는 이를 통해 SK하이닉스와의 기술 격차를 좁힐 수 있을 것으로 기대하고 있다.",
        "source": "조선비즈",
        "published_at": "2026-03-28T11:15:00",
    },
    {
        "title": "반도체 업황 회복세, 삼성전자 목표가 상향 잇따라",
        "content": "주요 증권사들이 삼성전자의 목표주가를 일제히 상향 조정하고 있다. KB증권은 목표가를 9만 5000원으로, 미래에셋증권은 10만원으로 각각 상향했다. AI 서버용 메모리 수요 증가와 파운드리 사업부 수익성 개선이 주요 근거로 제시됐다.",
        "source": "서울경제",
        "published_at": "2026-03-27T16:45:00",
    },
    {
        "title": "삼성전자, 미국 텍사스 파운드리 공장 가동 본격화",
        "content": "삼성전자가 미국 텍사스주 테일러시에 건설 중인 파운드리 공장의 가동을 본격화한다고 밝혔다. 총 투자액 170억 달러 규모의 이 공장은 3나노 공정을 적용하며, 미국 내 반도체 자급률 확대에 기여할 전망이다.",
        "source": "전자신문",
        "published_at": "2026-03-26T10:00:00",
    },
]

DUMMY_US_NEWS = [
    {
        "title": "Apple Reports Record Q2 Revenue Driven by AI Features",
        "content": "Apple Inc. reported record second-quarter revenue of $98.5 billion, beating Wall Street estimates. The company's AI-powered features, including advanced Siri capabilities and on-device machine learning, drove strong iPhone 17 sales. CEO Tim Cook highlighted the growing services segment and the upcoming Vision Pro 2 launch.",
        "source": "Reuters",
        "published_at": "2026-03-30T15:00:00",
    },
    {
        "title": "Wall Street Analysts Upgrade Apple on AI Strategy",
        "content": "Multiple Wall Street firms have upgraded Apple stock following the company's expanded AI strategy announcement. Morgan Stanley raised its price target to $260, citing Apple's unique position in on-device AI processing. The integration of generative AI across Apple's ecosystem is seen as a major growth catalyst.",
        "source": "Bloomberg",
        "published_at": "2026-03-29T12:00:00",
    },
    {
        "title": "Apple's Supply Chain Shifts Signal New Product Launches",
        "content": "Supply chain reports indicate Apple is ramping up production for multiple new product categories. Sources suggest increased orders for advanced display components and custom silicon chips. Analysts interpret these moves as preparation for the fall product lineup, including a refreshed MacBook Pro and new wearable devices.",
        "source": "CNBC",
        "published_at": "2026-03-28T09:30:00",
    },
    {
        "title": "Apple Services Revenue Crosses $25 Billion Milestone",
        "content": "Apple's services division has crossed the $25 billion quarterly revenue mark for the first time. App Store, Apple Music, iCloud, and Apple TV+ all contributed to the milestone. The high-margin services business now represents over 25% of Apple's total revenue, supporting the company's premium valuation.",
        "source": "Financial Times",
        "published_at": "2026-03-27T14:00:00",
    },
    {
        "title": "Apple Expands Partnerships with TSMC for Next-Gen Chips",
        "content": "Apple has deepened its partnership with TSMC to secure capacity for its next-generation M5 chips built on the 2-nanometer process. The deal ensures Apple will be among the first to adopt the cutting-edge technology, maintaining its performance lead in personal computing and mobile devices.",
        "source": "Wall Street Journal",
        "published_at": "2026-03-26T11:00:00",
    },
]


async def fetch_news(ticker: str, market: str = "KRX") -> list[dict]:
    """
    종목 관련 뉴스 기사를 가져옴
    현재는 더미 데이터 반환, 추후 실제 뉴스 API로 교체 예정

    Args:
        ticker: 종목 코드 (예: "005930", "AAPL")
        market: 시장 구분 ("KRX" 또는 "US")

    Returns:
        뉴스 기사 리스트 [{title, content, source, published_at}, ...]
    """
    # TODO: 실제 뉴스 API 연동 시 이 부분을 교체
    # 예시: 네이버 뉴스 API, NewsAPI.org, Alpha Vantage News 등

    if market.upper() == "KRX":
        news = DUMMY_KRX_NEWS
    else:
        news = DUMMY_US_NEWS

    return [
        {
            "title": article["title"],
            "content": article["content"],
            "source": article["source"],
            "published_at": article["published_at"],
            "ticker": ticker,
            "market": market.upper(),
        }
        for article in news
    ]
