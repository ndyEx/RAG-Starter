"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Search, Loader2 } from "lucide-react";

export default function StockSearchBar() {
  const [ticker, setTicker] = useState("");
  const [market, setMarket] = useState("KRX");
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (!ticker.trim()) return;

    setIsLoading(true);
    // ex) /stock/005930?market=KRX
    router.push(`/stock/${ticker.toUpperCase()}?market=${market}`);
  };

  return (
    <form onSubmit={handleSearch} className="w-full max-w-2xl mx-auto">
      <div className="relative flex items-center glass-card p-2 group hover:border-blue-500/50 transition-colors">
        {/* 시장 선택 Select */}
        <select
          value={market}
          onChange={(e) => setMarket(e.target.value)}
          className="bg-transparent text-slate-300 font-medium text-sm py-3 pl-4 pr-8 border-r border-slate-700/50 outline-none appearance-none cursor-pointer focus:text-white transition-colors"
          disabled={isLoading}
        >
          <option value="KRX" className="bg-slate-800">한국 (KRX)</option>
          <option value="US" className="bg-slate-800">미국 (US)</option>
        </select>
        
        {/* 화살표 아이콘 (Select용 커스텀) */}
        <div className="absolute left-[88px] top-1/2 -translate-y-1/2 pointer-events-none opacity-50">
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
        </div>

        {/* 검색어 입력란 */}
        <input
          type="text"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
          placeholder={market === "KRX" ? "종목코드 입력 (예: 005930)" : "티커 입력 (예: AAPL)"}
          className="flex-1 bg-transparent border-none text-white px-4 py-3 outline-none placeholder:text-slate-500 font-mono"
          disabled={isLoading}
        />

        {/* 검색 버튼 */}
        <button
          type="submit"
          disabled={!ticker.trim() || isLoading}
          className="flex items-center justify-center bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white rounded-xl px-6 py-3 font-medium transition-all shadow-lg shadow-blue-900/20 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isLoading ? (
            <Loader2 className="w-5 h-5 animate-spin" />
          ) : (
            <Search className="w-5 h-5" />
          )}
        </button>
      </div>
    </form>
  );
}
