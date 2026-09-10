# iyuno-agent-portfolio

채용공고의 요구사항을 실제로 구현한 AI Agent 포트폴리오 프로젝트입니다.

## 1. 프로젝트 목적
Iyuno AI Agent Engineer 공고의 핵심 요구사항을 작동하는 포트폴리오 증거로 연결하는 것을 목표로 합니다.

- LLM Agent / Router 구조
- RAG: 문서 검색 → 근거 문서 반환 → citation
- Tool calling / API 도구 구조
- Evaluation: 30개 이상 질문 데이터셋과 지표 저장 구조
- FastAPI 데모
- pytest + GitHub Actions 기반 자동 테스트

채용공고: https://iyuno.wd3.myworkdayjobs.com/careers/job/seoul/ai-agent-engineer_jr101122

> 현재 저장소는 수업 과제용 재현 가능한 기본 구현입니다. 외부 상용 LLM/API를 실제 연결한 운영 서비스가 아니라, 요구사항을 구현 구조와 실행 가능한 코드로 보여주는 포트폴리오 베이스입니다.

## 2. 채용공고 매핑
| 공고 요구사항 | 프로젝트 증거 |
|---|---|
| LLM 기반 AI Agent 설계·개발 | `app/agent.py` |
| RAG 검색·응답 + citation | `app/rag.py`, `data/documents/` |
| Tool calling / API 통합 | `app/tools.py` |
| 다단계 workflow | `app/agent.py`의 Router → Tool/RAG 분기 |
| 평가·피드백, latency/cost/reliability | `evaluation/` |
| 테스트/재현성 | `tests/`, `.github/workflows/test.yml` |

## 3. 폴더 구조
```text
app/
  agent.py       # 질문 라우팅 및 응답
  rag.py         # TF-IDF 기반 문서 검색
  tools.py       # calculator / policy 도구
  main.py        # FastAPI API

data/documents/ # RAG 샘플 문서
evaluation/     # 평가 질문 및 metrics
tests/          # pytest
.github/        # GitHub Actions CI
docs/           # AI 활용 기록
```

## 4. 실행
```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
pip install -r requirements.txt
python -m app.main
```

FastAPI 서버 실행 후 `/docs`에서 API를 확인할 수 있습니다.

테스트:
```bash
PYTHONPATH=. pytest
```

## 5. 평가
`evaluation/questions.json`에 35개 질문이 있으며, `evaluation/metrics.json`에 Recall@k, faithfulness, latency, token cost를 기록할 수 있도록 구성했습니다.

현재 metrics 값은 실제 외부 LLM/서비스 환경 측정 전 상태이며, 실행 후 실측값으로 업데이트해야 합니다.

## 6. AI 활용
ChatGPT를 사용해 요구사항 분석, 폴더 구조 설계, 코드 초안, 테스트 작성, 오류 분석, README 정리를 진행했습니다.
비밀키·개인정보·회사 내부자료는 입력하지 않았습니다.

## 7. 한계 및 개선 계획
- 현재 RAG는 가벼운 TF-IDF 검색 기반이며, 실제 임베딩 모델/vector DB로 확장할 수 있습니다.
- 현재 Tool은 로컬 함수 구조이며 실제 외부 API 연결은 추가 구현이 필요합니다.
- 실제 상용 LLM을 연결하면 latency/token cost를 실측하여 metrics에 반영할 수 있습니다.
- 실제 공개 기술문서 20개 이상을 수집하고 출처·라이선스를 정리하면 과제의 데이터 요구사항을 더 직접적으로 충족할 수 있습니다.
