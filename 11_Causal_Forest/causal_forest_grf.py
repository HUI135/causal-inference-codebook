import pandas as pd
from econml.dml import CausalForestDML
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 데이터 불러오기
df = pd.read_csv("../data/simulated_health_data.csv")
X = df[["age", "sex", "hypertension"]]
T = df["treatment"]
Y = df["outcome"]

# 모델 구성
est = CausalForestDML(
    model_t=LogisticRegression(),
    model_y=RandomForestRegressor(),
    n_estimators=100,
    min_samples_leaf=5,
    max_depth=10,
    verbose=0,
    random_state=42,
)

# 학습
est.fit(Y, T, X=X)

# ATE 및 CATE 추정
ate = est.ate(X)
cate = est.effect(X)

print(f"Causal Forest ATE: {ate}")
print(f"First 5 CATEs: {cate[:5]}")
