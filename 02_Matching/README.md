# 2️⃣ Matching (Nearest Neighbor)

## 📌 목적
처리군과 비처리군을 공변량 기준으로 유사한 개체끼리 짝지어 비교함으로써 인과효과(ATE)를 추정

## 🧪 방법
- 관측된 공변량(`age`, `sex`, `hypertension`) 기준으로 최근접 이웃을 찾음
- 1:1 Matching을 수행 (복원 없이)
- 매칭된 데이터로 선형회귀를 통해 효과 추정

## 📁 파일 설명
- `matching.py`: 실행형 매칭 스크립트
- `matching.ipynb`: 설명 포함 매칭 노트북

## ▶ 실행 방법
```bash
cd 2_Matching
python matching.py
```
