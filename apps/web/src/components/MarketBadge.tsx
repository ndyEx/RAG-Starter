import { Globe, LineChart } from "lucide-react";

interface MarketBadgeProps {
  market: "KRX" | "US";
}

export default function MarketBadge({ market }: MarketBadgeProps) {
  const isKrx = market === "KRX";

  return (
    <div
      className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold shadow-sm transition-all ${
        isKrx
          ? "bg-blue-500/10 text-blue-400 border border-blue-500/20"
          : "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
      }`}
    >
      {isKrx ? <LineChart className="w-3.5 h-3.5" /> : <Globe className="w-3.5 h-3.5" />}
      {isKrx ? "한국 주식 (KRX)" : "미국 주식 (US)"}
    </div>
  );
}
