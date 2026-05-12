# 💻 Developer — 검증된 지식

_Self-RAG가 출력에서 `[근거: ...]` 태그가 붙은 주장만 자동 승격해서 누적._
_여기 들어온 내용만 다음 사이클의 retrieval 우선순위에 들어갑니다._
_사용자가 직접 줄을 지우면 그 주장은 다시 미검증 상태로 돌아갑니다._


- [2026-05-06] # 기반으로 DB 스키마 매핑을 가정합니다. _(근거: sessions/2026-05-06T04-39/developer.md)_
- [2026-05-06] * `sessions/2026-05-06T07-07/business.md`에 따라, Business 에이전트가 정의한 대로 `Content Queue Manager`는 KPI 데이터 입력 요청을 성공적으로 수행했습니다. _(근거: sessions/2026-05-06T07-07/business.md)_
- [2026-05-06] * 로직 검증: `data_feedback_loop.py`는 입력받은 KPI를 Weighting(가중치)으로 변환하여, **Outcome-Based Bundle 전략**에 따라 Template A, B, C의 디자인 우선순위(Outcome > Weighting > Detail)를 결정하도록 설계되었습니다. _(근거: sessions/2026-05-06T07-47)_
- [2026-05-06] 1. **KPI $\rightarrow$ Weighting:** 데이터베이스에서 KPI가 읽혀지며 가중치(40%, 30%)로 변환됩니다. _(근거: sessions/2026-05-06T07-22/developer.md)_
- [2026-05-06] 2. **Weighting $\rightarrow$ Design Logic:** 이 가중치가 Designer에게 전달되어 시각적 계층 구조(Outcome 강조)를 결정합니다. _(근거: sessions/2026-05-06T07-22/designer.md)_
- [2026-05-06] 3. **Design Logic $\rightarrow$ Asset Output:** 최종적으로 Template A, B, C의 디자인이 시스템에 오류 없이 통합되어 출력되도록 보장합니다. _(근거: sessions/2026-05-06T06-52/developer.md)_