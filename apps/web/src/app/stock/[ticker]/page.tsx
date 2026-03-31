"use client";

import { use, useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { ArrowLeft, RefreshCw, AlertCircle } from "lucide-react";
import MarketBadge from "@/components/MarketBadge";
import AnalysisResult from "@/components/AnalysisResult";

interface StockPageProps {
  params: Promise<{ ticker: string }>;
}

export default function StockAnalysisPage({ params }: StockPageProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const rawTicker = use(params).ticker;
  const ticker = decodeURIComponent(rawTicker);
  const market = searchParams.get("market") || "KRX";

  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<any>(null);

  const fetchAnalysis = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const res = await fetch("/api/stock/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticker, market }),
      });

      const json = await res.json();
      if (!res.ok) throw new Error(json.error || "분석에 실패했습니다.");

      setData(json);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchAnalysis();
  }, [ticker, market]);

  return (
    <div className="min-h-screen p-6 md:p-12 relative max-w-5xl mx-auto">
      {/* 상단 네비게이션 */}
      <div className="flex items-center justify-between mb-10">
        <button
          onClick={() => router.push("/")}
          className="flex items-center gap-2 text-slate-400 hover:text-white transition-colors"
        >
          <ArrowLeft className="w-5 h-5" />
          <span>새로운 검색</span>
        </button>

        <MarketBadge market={market as "KRX" | "US"} />
      </div>

      {/* 헤더 정보 */}
      <div className="mb-12">
        <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
          <span className="text-gradient font-mono mr-3">{ticker}</span>
          AI 심층 분석
        </h1>
        <p className="text-slate-400 text-lg">
          가장 최신 뉴스들을 기반으로 생성된 {market === "KRX" ? "한국" : "미국"} 주식 시장 종목 리포트입니다.
        </p>
      </div>

      {/* 로딩 상태 뷰 */}
      {isLoading && (
        <div className="flex flex-col items-center justify-center py-20 glass-card">
          <RefreshCw className="w-12 h-12 text-blue-500 animate-spin mb-6" />
          <h2 className="text-xl font-semibold text-white mb-2">데이터 수집 및 분석 중...</h2>
          <p className="text-slate-400">수백 개의 뉴스를 읽고 요약하는 중입니다. (약 10~20초 소요)</p>
        </div>
      )}

      {/* 에러 상태 뷰 */}
      {!isLoading && error && (
        <div className="p-8 rounded-2xl bg-red-900/20 border border-red-500/50 flex flex-col items-center text-center">
          <AlertCircle className="w-12 h-12 text-red-400 mb-4" />
          <h2 className="text-xl font-semibold text-red-200 mb-2">분석 오류 발생</h2>
          <p className="text-red-300/80 mb-6">{error}</p>
          <button
            onClick={fetchAnalysis}
            className="px-6 py-2 bg-red-500/20 text-red-300 rounded-lg hover:bg-red-500/30 transition-colors"
          >
            다시 시도
          </button>
        </div>
      )}

      {/* 분석 결과 뷰 */}
      {!isLoading && !error && data && (
        <AnalysisResult analysis={data.analysis} sources={data.sources} />
      )}
    </div>
  );
}
