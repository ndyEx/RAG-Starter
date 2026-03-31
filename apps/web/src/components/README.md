# 🧱 UI Components (공통 화면 부품)

이 폴더는 여러 화면에서 재사용하기 위해 **잘게 쪼개놓은 화면의 부품(컴포넌트)** 들이 모여있는 곳입니다. 

- `StockSearchBar.tsx`: 검색창 컴포넌트
- `AnalysisResult.tsx`: 마크다운 분석 결과를 예쁘게 보여주는 카드
- 등등...

Spring의 `include` 또는 `fragment` 조각 템플릿 같은 역할입니다. 페이지 파일(`app/page.tsx`)에서 이 부품들을 조립해서 하나의 큰 화면을 만듭니다.
