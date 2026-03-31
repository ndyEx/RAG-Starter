import { ExternalLink, Newspaper } from "lucide-react";

interface SourceListProps {
  sources: string[];
}

export default function SourceList({ sources }: SourceListProps) {
  if (!sources || sources.length === 0) return null;

  // 더미 중복 제거
  const uniqueSources = Array.from(new Set(sources));

  return (
    <div className="mt-8 pt-6 border-t border-slate-700/50">
      <h3 className="text-sm font-semibold text-slate-300 mb-3 flex items-center gap-2">
        <Newspaper className="w-4 h-4 text-slate-400" />
        참고한 뉴스 소스 제공처
      </h3>
      <div className="flex flex-wrap gap-2">
        {uniqueSources.map((source, idx) => (
          <div
            key={idx}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-slate-800/60 border border-slate-700 text-xs text-slate-300 hover:bg-slate-700 transition-colors"
          >
            {source}
            <ExternalLink className="w-3 h-3 text-slate-500" />
          </div>
        ))}
      </div>
    </div>
  );
}
