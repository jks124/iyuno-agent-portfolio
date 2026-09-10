from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleRAG:
    def __init__(self, doc_dir="data/documents"):
        self.doc_dir = Path(doc_dir)
        self.docs = []
        for path in sorted(self.doc_dir.glob("*.txt")):
            self.docs.append({"source": path.name, "text": path.read_text(encoding="utf-8")})
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform([d["text"] for d in self.docs]) if self.docs else None

    def retrieve(self, query, k=3):
        if not self.docs:
            return []
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix)[0]
        idx = scores.argsort()[::-1][:k]
        return [{"source": self.docs[i]["source"], "score": float(scores[i]), "text": self.docs[i]["text"]} for i in idx]
