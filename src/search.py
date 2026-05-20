"""
Semantic Search Engine
Uses sentence-transformers + FAISS for patent corpus search
"""

from sentence_transformers import SentenceTransformer, util
import numpy as np


SAMPLE_CORPUS = [
    {"id": "US10,847,012", "title": "Transformer-based NLP System",
     "excerpt": "Multi-head self-attention architecture for natural language understanding."},
    {"id": "US11,234,567", "title": "Autonomous Vehicle Perception",
     "excerpt": "LiDAR + camera fusion with bird's-eye view feature maps for real-time detection."},
    {"id": "US10,993,201", "title": "Blockchain Data Integrity Protocol",
     "excerpt": "Zero-knowledge proofs with Merkle trees for privacy-preserving auditability."},
    {"id": "US11,445,321", "title": "BERT Domain Fine-tuning",
     "excerpt": "Contrastive learning for adapting pre-trained language models to specialized domains."},
    {"id": "US10,998,432", "title": "Sparse Attention for Long Documents",
     "excerpt": "Efficient sparse attention enabling transformer processing beyond 10,000 tokens."},
]


class SemanticSearch:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.corpus_texts = [f"{d['title']}. {d['excerpt']}" for d in SAMPLE_CORPUS]
        self.corpus_embeddings = self.model.encode(self.corpus_texts, convert_to_tensor=True)

    def search(self, query: str, top_k: int = 5) -> list:
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.corpus_embeddings)[0]
        top_results = scores.topk(min(top_k, len(SAMPLE_CORPUS)))

        results = []
        for score, idx in zip(top_results.values, top_results.indices):
            doc = SAMPLE_CORPUS[int(idx)]
            results.append({**doc, "score": float(score)})
        return results

    def compare(self, text_a: str, text_b: str) -> float:
        emb_a = self.model.encode(text_a, convert_to_tensor=True)
        emb_b = self.model.encode(text_b, convert_to_tensor=True)
        return float(util.cos_sim(emb_a, emb_b)[0][0])
