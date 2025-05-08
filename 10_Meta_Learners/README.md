# 🔟 Meta Learners (S/T/X)

## 📌 목적
머신러닝 예측기를 활용하여 개별적 인과효과 (CATE)를 추정

## ⚙️ 분석 개요
- `S-learner`: 하나의 모델에 treatment를 feature로 포함
- `T-learner`: treatment/control 각각 모델을 따로 학습
- `X-learner`: T-learner 기반의 개선된 방식

## ▶ 실행 방법
```bash
cd 10_Meta_Learners
python s_learner_t_learner_x_learner.py
```

## 🔧 의존성
```bash
pip install causalml
```
