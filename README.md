# iyuno-agent-portfolio

[![CI](https://github.com/jks124/iyuno-agent-portfolio/actions/workflows/test.yml/badge.svg)](https://github.com/jks124/iyuno-agent-portfolio/actions/workflows/test.yml)

채용공고의 요구사항을 실제로 구현한 AI Agent 포트폴리오 프로젝트입니다.

## 1. 프로젝트 목적
Iyuno AI Agent Engineer 공고의 핵심 요구사항을 작동하는 포트폴리오 증거로 연결하는 것을 목표로 합니다.

- LLM Agent / Router 구조
- RAG: 문서 검색 → 근거 문서 반환 → citation
- Tool calling / API 도구 구조
- Evaluation: 35개 질문 데이터셋과 지표 측정
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
| 평가·피드백, latency/cost/reliability | `evaluation/`, `RETROSPECTIVE.md` |
| 테스트/재현성 | `tests/`, `.github/workflows/test.yml` |

## 3. 폴더 구조
```text
app/
  agent.py       # 질문 라우팅 및 응답
  rag.py         # TF-IDF 기반 문서 검색
  tools.py       # calculator / policy 도구
  main.py        # FastAPI API

data/documents/ # RAG 샘플 문서
evaluation/     # 평가 질문, metrics, 결과 그래프
tests/          # pytest
.github/        # GitHub Actions CI
docs/           # AI 활용 기록
DATA_SOURCES.md # 데이터 출처·라이선스·생성일
RETROSPECTIVE.md# 최종 1페이지 회고
LICENSE         # MIT License
```

## 4. 설치 및 실행
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

## 5. 평가 결과
`evaluation/questions.json`에는 35개 질문이 있습니다.

2026-09-10 로컬 환경 측정 결과:
- Recall@1: **74.29%**
- Recall@3: **100%**
- 평균 retrieval latency: **0.861 ms**
- P95 retrieval latency: **0.928 ms**

결과 그래프: `evaluation/metrics_graph.svg`

현재 외부 LLM을 연결하지 않았기 때문에 faithfulness와 token cost는 실측하지 않았습니다. 실제 LLM 연결 시 동일 평가셋으로 추가 측정합니다.

## 6. 테스트 및 CI
- `tests/test_rag.py`: RAG 검색 기본 동작 테스트
- GitHub Actions에서 `pytest` 자동 실행
- README 상단 CI 배지로 최신 테스트 상태 확인 가능

## 7. 데이터 출처·라이선스·생성일
상세 기록은 `DATA_SOURCES.md`에 있습니다.

현재 데이터는 프로젝트 작성자가 직접 만든 교육용 샘플 문서와 35개 평가 질문입니다. 외부 공개 기술문서 20개 이상을 실제 수집한 버전은 향후 확장 예정입니다.

- 생성일: 2026-09-10
- 소스코드 라이선스: MIT
- 샘플 데이터: 프로젝트 작성자 직접 작성

## 8. AI 활용
ChatGPT를 사용해 요구사항 분석, 폴더 구조 설계, 코드 초안, 테스트 작성, 오류 분석, README 정리를 진행했습니다.
비밀키·개인정보·회사 내부자료는 입력하지 않았습니다. 상세 기록은 `docs/AI_USAGE.md`에서 확인할 수 있습니다.

## 9. 최종 회고
`RETROSPECTIVE.md`에 1페이지 회고를 작성했습니다. 구현한 기능, 측정 결과, 남은 과제와 개선 방향을 정리했습니다.

## 10. 한계 및 개선 계획
- 현재 RAG는 가벼운 TF-IDF 검색 기반이며, 실제 임베딩 모델/vector DB로 확장할 수 있습니다.
- 현재 Tool은 로컬 함수 구조이며 실제 외부 API 연결은 추가 구현이 필요합니다.
- 실제 상용 LLM을 연결하면 faithfulness와 token cost를 추가 측정할 수 있습니다.
- 공개 기술문서 20개 이상을 수집하고 각 문서의 원문 URL·라이선스·수집일을 기록하면 데이터 요구사항을 더 직접적으로 충족할 수 있습니다.
- Streamlit/FastAPI 화면과 실행 영상을 추가하면 데모 완성도를 높일 수 있습니다.
