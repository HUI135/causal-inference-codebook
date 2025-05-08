# 7️⃣ G-computation (G-formula)

## 📌 목적
모델을 기반으로 잠재적 결과(Potential Outcome)를 추정하여 ATE 계산

## ⚙️ 분석 개요
- `LinearRegression`: outcome ~ treatment + covariates
- treatment을 0/1로 바꾼 예측 결과 차이의 평균이 ATE

## ▶ 실행 방법
```bash
cd 7_GComputation
python g_formula.py
```

## 📈 해석
- ATE = E[Y(1) - Y(0)] = 평균 예측 차이
