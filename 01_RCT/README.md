# 1️⃣ 무작위 대조군 실험 (RCT)

## 📌 목적
무작위로 할당된 treatment를 통해 outcome의 인과적 효과를 추정

## 🧪 분석 방식
- treatment는 `binomial(1, 0.5)`로 무작위 할당
- ITT 방식으로 ATE 추정
- 시각화로 결과 비교

## ⚙️ 방법론 설명
- **ITT (Intention-to-Treat)**: 실제 복용 여부와 상관없이 무작위 배정 기준으로 분석
- **Per-protocol**: 실제로 복용한 집단만 분석 → 선택 편향 위험
- **Complier 분석**: 무작위 배정에 따라 행동한 집단만 추출 (IV에서 연결됨)

## ▶ 실행 방법
```bash
cd 1_RCT
python rct_simulation.py
```
