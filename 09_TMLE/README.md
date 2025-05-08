# 9️⃣ Targeted Maximum Likelihood Estimation (TMLE)

## 📌 목적
Outcome model과 Propensity model을 결합해 doubly robust 방식으로 ATE를 추정

## ⚙️ 분석 개요
- Exposure model: treatment ~ covariates
- Outcome model: outcome ~ treatment + covariates
- TMLE = Bias correction + model combination

## ▶ 실행 방법
```bash
cd 9_TMLE
python tmle_demo.py
```

## 🔧 의존성
```bash
pip install zepid
```
