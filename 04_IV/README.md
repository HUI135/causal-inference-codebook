# 4️⃣ Instrumental Variable (IV)

## 📌 목적
무작위 배정이 존재하지만 비순응(non-compliance)이 존재할 때, instrument를 사용하여 인과추정

## ⚙️ 방법
- `z`: 무작위 배정 (instrument)
- `treatment_iv`: 실제 행동한 treatment
- 2단계 최소제곱법(2SLS)을 통해 간접 인과 추정

## ▶ 실행 방법
```bash
cd 4_IV
python iv_2sls.py
```
