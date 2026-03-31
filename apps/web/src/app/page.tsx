import StockSearchBar from "@/components/StockSearchBar";

export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-6 relative overflow-hidden">
      {/* 배경 장식용 흐릿한 원형 그라데이션 */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-blue-500/10 blur-[100px] rounded-full pointer-events-none" />

      <div className="relative z-10 w-full max-w-3xl flex flex-col items-center">
        {/* 타이틀 영역 */}
        <div className="text-center mb-10 space-y-4">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 text-blue-400 text-sm font-medium border border-blue-500/20 mb-4 shadow-xl">
            ✨ AI 기반 초고속 뉴스 분석
          </div>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-white mb-6">
            RAG 기반 <span className="text-gradient">주식 분석</span> 시스템
          </h1>
          <p className="text-slate-400 text-lg md:text-xl max-w-xl mx-auto leading-relaxed">
            관심 있는 종목을 입력하면 수백 개의 최신 뉴스를 AI가 순식간에 요약하고 핵심을 짚어드립니다.
          </p>
        </div>

        {/* 검색창 영역 */}
        <div className="w-full relative z-20">
          <StockSearchBar />
        </div>

        {/* 하단 툴팁 */}
        <p className="text-slate-500 text-sm mt-8 mt-12 mb-4">
          한국 주식은 <strong className="font-semibold text-slate-300">005930</strong> 등 종목코드를,
          미국 주식은 <strong className="font-semibold text-slate-300">AAPL</strong> 등 티커를 입력하세요.
        </p>

      </div>
    </main>
  );
}
