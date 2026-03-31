# 🖥 App Router (Next.js 화면 및 라우팅)

이 폴더는 **사용자가 직접 보는 접속 페이지(View)** 와 URL 경로를 설정하는 곳입니다. Spring의 JSP나 Thymeleaf가 있는 뷰 템플릿 영역이라고 보시면 됩니다.

- `page.tsx`: 실제 화면에 렌더링되는 UI 코드입니다. (예: 시작 페이지)
- `stock/[ticker]/page.tsx`: 경로에 변수가 들어가는 동적 페이지입니다. (Spring의 `@PathVariable`과 유사)
- `api/`: 서버 프록시 API 라우트로, 여기서 파이썬 백엔드로 데이터를 넘겨줍니다.
