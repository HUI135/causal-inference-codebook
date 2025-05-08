# 🧠 Python Causal Inference Codebook

**인과추론을 처음 접하는 사람부터 실무자까지**, 단계적으로 학습할 수 있도록 설계된 Python 기반 인과추론 코드북입니다.  
각 방법론은 이론 개요 → 사용 조건 → 수식 및 가정 → Python 코드 예제 순으로 구성되어 있습니다.

---

## 📦 포함된 인과추론 기법

| 번호 | 방법론                         | 한줄 설명 |
|------|--------------------------------|------------|
| 1️⃣   | 무작위 대조군 실험 (RCT)        | 무작위 배정을 통해 교란 없이 인과 추정 |
| 2️⃣   | Matching / Stratification      | 유사한 특성을 가진 사람끼리 비교 |
| 3️⃣   | Propensity Score               | 처치 확률을 추정하여 교란 조정 |
| 4️⃣   | Instrumental Variable (IV)     | 처치에 영향을 주되 결과에 직접 영향이 없는 외생변수 활용 |
| 5️⃣   | Difference-in-Differences (DiD)| 시간에 따른 차이를 활용한 준실험적 추정 |
| 6️⃣   | Regression Discontinuity (RDD) | 임계값 기반 처치 적용 시 효과 추정 |
| 7️⃣   | G-computation (G-formula)      | 결과 모형 기반의 인과 추정 방식 |
| 8️⃣   | Marginal Structural Models     | 시간의존적 교란 조정 (IPTW 기반) |
| 9️⃣   | TMLE                           | Outcome + Propensity 모델을 결합한 이중강건 추정 |
| 🔟   | Meta Learners (S/T/X)           | 머신러닝으로 개별 효과(CATE) 추정 |
| 🔟   | Causal Forest                   | 비선형성과 이질성을 반영한 랜덤포레스트 기반 CATE 추정 |
| 🔟   | Structure Learning              | 데이터 기반 DAG(인과구조) 자동 학습 |

---

## 🎓 학습 단계별 추천

### 🌱 초심자
- **권장 순서**: RCT → Matching → PS → DiD
- **학습 포인트**: 교란 개념, 평균 처치 효과(ATE), 무작위 배정의 가치

### 🌿 중급 학습자
- **권장 순서**: G-computation → IPTW(MSM) → TMLE → RDD → IV
- **학습 포인트**: 모델 기반 추정법, 시간 의존성, 조건부 독립성

### 🌳 실무자
- **권장 순서**: Meta Learners → Causal Forest → NOTEARS/PC
- **학습 포인트**: 개별효과(CATE), 비선형 모델링, DAG 추론

---

## 🧠 핵심 개념 해설

### ✅ 평균 처치 효과 (ATE)
> E[Y(1) - Y(0)] — 모든 사람에 대한 평균적인 효과

### ✅ 개별 조건부 처치 효과 (CATE)
> E[Y(1) - Y(0) | X=x] — 특정 특성을 가진 집단에서의 효과

### ✅ 교란 변수 (Confounder)
> 처치와 결과에 모두 영향을 주는 제3 변수

### ✅ 조건부 독립성 (Conditional Exchangeability)
> X가 주어졌을 때, 처치와 결과가 독립이라는 가정

---

## 📁 폴더 구성 예시

```
causal-inference-codebook/
├── 1_RCT/
│   ├── rct_simulation.py
│   ├── rct_simulation.ipynb
│   └── README.md
├── 2_Matching/
├── ...
├── 12_Structure_Learning/
├── utils/  ← 데이터 시뮬레이션 스크립트
├── data/   ← 공통 시뮬레이션 데이터 (CSV)
└── requirements.txt
```

---

## 📊 예시 결과 (Matching)

```python
# PS 매칭 후 ATT 추정 결과
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                outcome   R-squared:                       0.321
==============================================================================
coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const      1.6245      0.134     12.097      0.000       1.361       1.888
treatment  1.8743      0.172     10.927      0.000       1.537       2.212
```

---

## 🛠️ 설치 방법

```bash
git clone https://github.com/your-repo/causal-inference-codebook.git
cd causal-inference-codebook
pip install -r requirements.txt
```

---

## 📚 추천 자료

| 구분 | 제목 | 비고 |
|------|------|------|
| 입문 | Hernán & Robins - *Causal Inference: What If* | 무료 PDF |
| 실전 | Judea Pearl - *Causality* | 그래프 기반 접근 |
| 적용 | 강필성 외 - *데이터과학을 위한 인과추론 입문* | R/Python 예제 포함 |

---

© 2025 HUI135 / Causal Inference Codebook Project
