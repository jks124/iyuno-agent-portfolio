# iyuno-agent-portfolio

채용공고의 요구사항을 실제로 구현한 AI Agent 포트폴리오 프로젝트입니다.

## 1. 프로젝트 목적
Iyuno AI Agent Engineer 공고의 핵심 요구사항을 '작동하는 증거'로 바꾸는 것을 목표로 합니다.

- LLM Agent / Router
- RAG: 문서 수집 → chunking → embedding/vector search → citation
- Tool calling / API orchestration
- Evaluation: 30개 이상 질문을 기준으로 정확도·지연시간·비용을 기록
- Feedback loop
- FastAPI 데모

> 현재 저장소는 수업 과제용 재현 가능한 기본 구현입니다. 실제 외부 LLM/API 키가 필요한 기능은 환경변수로 연결하도록 구성했습니다.

## 2. 채용공고 매핑
| 공고 요구사항 | 프로젝트 증거 |
|---|---|
| LLM 기반 AI Agent 설계·개발 | `app/agent.py` |
| RAG 검색·응답 + citation | `app/rag.py`, `data/documents/` |
| Tool calling / API 통합 | `app/tools.py` |
| 다단계 workflow | `app/agent.py` |
| 평가·피드백, latency/cost/reliability | `evaluation/` |

## 3. 실행
```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
pip install -r requirements.txt
python -m app.main
```

FastAPI 서버 실행 후 `/docs`에서 API를 확인할 수 있습니다.

## 4. AI 활용
ChatGPT를 사용해 요구사항 분석, 폴더 구조 설계, 코드 초안, 테스트 작성, 오류 분석, README 정리를 진행했습니다.
비밀키·개인정보·회사 내부자료는 입력하지 않았습니다.

## 5. 한계
- 실제 상용 LLM과 외부 API의 호출 비용/지연시간은 환경에 따라 달라집니다.
- 평가 결과는 과제용 데이터셋 기준이며 실제 서비스 성능을 의미하지 않습니다.
