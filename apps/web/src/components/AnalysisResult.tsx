"use client";

import { motion } from "framer-motion";
import ReactMarkdown from "react-markdown";
import SourceList from "./SourceList";

interface AnalysisResultProps {
  analysis: str;
  sources: string[];
}

export default function AnalysisResult({ analysis, sources }: AnalysisResultProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: "easeOut" }}
      className="glass-card p-6 md:p-8"
    >
      <div className="prose prose-invert prose-blue max-w-none">
        <ReactMarkdown
          components={{
            h1: ({ node, ...props }) => <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-400 mb-6" {...props} />,
            h2: ({ node, ...props }) => <h2 className="text-xl font-semibold text-blue-300 mt-8 mb-4 flex items-center gap-2 before:content-[''] before:w-1.5 before:h-5 before:bg-blue-500 before:rounded-full" {...props} />,
            h3: ({ node, ...props }) => <h3 className="text-lg font-medium text-slate-200 mt-6 mb-3" {...props} />,
            p: ({ node, ...props }) => <p className="text-slate-300 leading-relaxed mb-4 text-sm md:text-base" {...props} />,
            ul: ({ node, ...props }) => <ul className="list-disc pl-5 mb-4 text-slate-300 space-y-2 marker:text-blue-500" {...props} />,
            ol: ({ node, ...props }) => <ol className="list-decimal pl-5 mb-4 text-slate-300 space-y-2 marker:text-blue-500 font-medium" {...props} />,
            li: ({ node, ...props }) => <li className="pl-1" {...props} />,
            strong: ({ node, ...props }) => <strong className="font-semibold text-white bg-blue-900/30 px-1 rounded" {...props} />,
          }}
        >
          {analysis}
        </ReactMarkdown>
      </div>

      <SourceList sources={sources} />
    </motion.div>
  );
}
