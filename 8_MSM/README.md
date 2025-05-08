# 8️⃣ Marginal Structural Models (MSM using IPTW)

## 📌 목적
시간에 따라 변하는 처치와 교란 변수의 영향을 제거하고, 인과효과를 추정

## ⚙️ 분석 개요
- `pscore`: treatment 확률 (propensity score)
- `iptw`: 1/pscore 또는 1/(1-pscore)
- `WLS`: weighted least squares로 outcome ~ treatment 분석

## ▶ 실행 방법
```bash
cd 8_MSM
python iptw_msm.py
```
