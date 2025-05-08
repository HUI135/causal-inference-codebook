# 5️⃣ Difference-in-Differences (DiD)

## 📌 목적
처리군과 통제군의 사전-사후 변화 차이를 비교하여 인과효과 추정

## ⚙️ 분석 개요
- `group`: 처리군(1) vs 통제군(0)
- `time`: 사전(0) vs 사후(1)
- `treatment`: group * time (상호작용항)

## ▶ 실행 방법
```bash
cd 5_DiD
python did_basic.py
```

## 📈 결과 해석
- 회귀식: `outcome ~ group + time + treatment`
- `treatment`의 계수가 DiD 추정값 (인과효과)
