from app.rag import SimpleRAG

def test_retrieve_returns_results():
    rag = SimpleRAG()
    results = rag.retrieve("API 키 보안", k=2)
    assert len(results) > 0
    assert "source" in results[0]
