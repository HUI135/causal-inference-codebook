# 🔟 Structure Learning (NOTEARS / PC Algorithm)

## 📌 목적
변수 간의 구조적 인과 그래프(DAG)를 자동으로 추정

## ⚙️ 방법
- `NOTEARS`: 연속형 데이터에서 미분가능한 방식으로 DAG 학습
- `PC Algorithm`: 조건부 독립성 검정을 기반으로 DAG 추론

## ▶ 실행 방법
```bash
cd 12_Structure_Learning
python notears_example.py
python pc_algorithm.py
```

## 🔧 의존성
```bash
pip install notears pgmpy
```
