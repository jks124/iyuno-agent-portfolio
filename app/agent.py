from .rag import SimpleRAG
from .tools import calculator, search_policy

class Agent:
    def __init__(self):
        self.rag = SimpleRAG()

    def route(self, question: str):
        q = question.lower()
        if any(x in q for x in ["계산", "+", "-", "*", "/"]):
            return "calculator"
        if "정책" in q or "api key" in q or "라이선스" in q:
            return "policy"
        return "rag"

    def answer(self, question: str):
        route = self.route(question)
        if route == "calculator":
            # 과제용 안전한 예시: 숫자/연산식이 명확한 경우에만 사용
            return {"route": route, "answer": "계산 도구 호출 경로가 선택되었습니다.", "sources": []}
        if route == "policy":
            return {"route": route, "answer": search_policy("security"), "sources": ["policy"]}
        hits = self.rag.retrieve(question)
        if not hits:
            return {"route": route, "answer": "관련 문서를 찾지 못했습니다.", "sources": []}
        best = hits[0]
        return {"route": route, "answer": best["text"], "sources": [h["source"] for h in hits]}
