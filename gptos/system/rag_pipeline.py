# gptos/system/rag_pipeline.py

from typing import List, Optional
import numpy as np
import os

def load_default_rag_docs(pipeline):
    doc_path = "doc/why_gpt_os_exists.md"
    if os.path.exists(doc_path):
        with open(doc_path, "r", encoding="utf-8") as f:
            content = f.read()
        chunks = [p.strip() for p in content.split("\n\n") if p.strip()]
        pipeline.add_documents(chunks)

class SimpleRAGPipeline:
    def __init__(self):
        self.documents: List[str] = []
        self.embeddings: List[np.ndarray] = []
        self.cache: dict[str, List[str]] = {}

    def embed(self, text: str) -> np.ndarray:
        # 임시: 단어 단위 길이로 벡터화 (후에 OpenAI Embedding으로 교체)
        return np.array([len(w) for w in text.split()])

    def add_documents(self, docs: List[str]):
        """문서 추가 최적화"""
        for doc in docs:
            # 중복 문서 추가 방지
            if doc not in self.documents:
                self.documents.append(doc)
                self.embeddings.append(self.embed(doc))

    def retrieve(self, query: str, top_k: int = 3) -> List[str]:
        # 캐시 확인
        if query in self.cache:
            return self.cache[query]
        
        q_emb = self.embed(query)
        scores = [self.similarity(q_emb, emb) for emb in self.embeddings]
        top_indices = np.argsort(scores)[-top_k:][::-1]
        results = [self.documents[i] for i in top_indices]

        # 쿼리 결과 캐싱
        self.cache[query] = results
        
        return results

    def run(self, query: str) -> str:
        results = self.retrieve(query)
        return "\n---\n".join(results) if results else "(No results)"

    def similarity(self, v1: np.ndarray, v2: np.ndarray) -> float:
        if len(v1) != len(v2):
            min_len = min(len(v1), len(v2))
            v1 = v1[:min_len]
            v2 = v2[:min_len]
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-6))
    


