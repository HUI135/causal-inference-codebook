# 3️⃣ Propensity Score (PS)

## 📌 목적
관측된 공변량을 기반으로 treatment을 받을 확률을 추정하여 매칭하거나 가중치를 적용

## 🧪 세 가지 방식
- `ps_matching.py`: PS 기반 최근접 매칭
- `ps_weighting.py`: IPTW (Inverse Probability of Treatment Weighting)
- `ps_diagnostics.py`: PS 분포 시각화 (balance 확인)

## ▶ 실행 방법
```bash
cd 3_Propensity_Score
python ps_matching.py
python ps_weighting.py
python ps_diagnostics.py
```
