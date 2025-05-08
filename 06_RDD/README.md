# 6️⃣ Regression Discontinuity Design (RDD)

## 📌 목적
임계값을 기준으로 처치 여부가 결정되는 상황에서 인과효과 추정

## ⚙️ 분석 개요
- `score`: 연속적 변수
- `treatment`: score >= 50 이면 1
- `score_centered`: 경계값(50) 중심으로 정규화
- 회귀식: outcome ~ treatment + score_centered

## ▶ 실행 방법
```bash
cd 6_RDD
python rdd_analysis.py
```
