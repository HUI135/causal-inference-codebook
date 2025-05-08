# 🔟 Causal Forest (EconML)

## 📌 목적
비선형성과 이질적 처치 효과를 반영하여 인과효과를 추정하는 머신러닝 기반 모델

## ⚙️ 분석 개요
- `CausalForestDML`: Double ML 기반 Causal Forest
- ATE 추정 + 개별 CATE 추정
- model_y: outcome 모델
- model_t: treatment 모델

## ▶ 실행 방법
```bash
cd 11_Causal_Forest
python causal_forest_grf.py
```

## 🔧 의존성
```bash
pip install econml
```
