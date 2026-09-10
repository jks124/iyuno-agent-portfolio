# 최종 1페이지 회고

## 무엇을 구현했는가
이번 프로젝트는 Iyuno AI Agent Engineer 채용공고를 분석한 뒤, 요구사항을 실제 코드와 GitHub 저장소의 증거로 연결하는 것을 목표로 진행했다.

구현한 핵심 기능은 다음과 같다.
- 질문을 RAG와 Tool 경로로 분기하는 Agent Router
- TF-IDF 기반 문서 검색과 검색 결과의 source 반환
- calculator / policy 형태의 Tool 호출 구조
- FastAPI `/ask` API를 통한 데모 인터페이스
- 35개 평가 질문 데이터셋
- Recall@1, Recall@3, retrieval latency 측정
- pytest 테스트와 GitHub Actions CI 자동 실행
- README, 데이터 출처·라이선스, AI 활용 기록 문서화

## 평가 결과
2026-09-10 로컬 환경에서 35개 질문을 대상으로 측정했다.
- Recall@1: 74.29%
- Recall@3: 100%
- 평균 retrieval latency: 0.861 ms
- P95 retrieval latency: 0.928 ms

현재는 외부 LLM을 연결하지 않았기 때문에 faithfulness와 token cost는 실측하지 않았다.

## 무엇이 남았는가
현재 구현은 채용공고의 요구사항을 보여주는 재현 가능한 기본 포트폴리오다. 실제 서비스 수준으로 발전시키려면 다음 작업이 필요하다.
1. 공개 기술문서 20개 이상을 실제 수집하고 원문 URL, 라이선스, 수집일을 기록한다.
2. TF-IDF를 실제 임베딩 모델과 vector DB 기반 RAG로 확장한다.
3. 외부 LLM과 실제 API를 연결해 자연어 응답과 Tool calling을 완성한다.
4. 동일 평가셋으로 faithfulness, latency, token cost를 추가 측정한다.
5. Streamlit/FastAPI 데모 화면과 실행 영상을 추가한다.

## 느낀 점
채용공고를 단순히 읽는 것보다 요구사항을 기능 단위로 나누고 각각을 코드, 테스트, 평가 결과로 연결하는 방식이 포트폴리오를 만드는 데 더 효과적이었다. 특히 RAG와 Agent 구조를 직접 구현하면서 기술 이름을 아는 것과 실제로 동작하는 구조를 만드는 것의 차이를 확인했다.
