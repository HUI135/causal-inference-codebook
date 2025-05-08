import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 데이터 로드
df = pd.read_csv("../data/simulated_health_data.csv")

# 매칭할 공변량
covariates = ["age", "sex", "hypertension"]

# 처리군/비처리군 분리
treated = df[df["treatment"] == 1].copy()
control = df[df["treatment"] == 0].copy()

# Nearest Neighbor Matching
nn = NearestNeighbors(n_neighbors=1)
nn.fit(control[covariates])
distances, indices = nn.kneighbors(treated[covariates])
matched_control = control.iloc[indices.flatten()].copy()
matched_df = pd.concat([treated.reset_index(drop=True), matched_control.reset_index(drop=True)])

# ATE 추정
X = sm.add_constant(matched_df["treatment"])
y = matched_df["outcome"]
model = sm.OLS(y, X).fit()
print(model.summary())
