import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv("../data/simulated_health_data.csv")

# Estimate propensity scores
X = df[["age", "sex", "hypertension"]]
y = df["treatment"]
ps_model = LogisticRegression()
ps_model.fit(X, y)
df["pscore"] = ps_model.predict_proba(X)[:, 1]

# IPTW 계산
df["iptw"] = df["treatment"] / df["pscore"] + (1 - df["treatment"]) / (1 - df["pscore"])

# MSM: IPTW를 적용한 weighted regression
X_reg = sm.add_constant(df["treatment"])
y_reg = df["outcome"]
msm_model = sm.WLS(y_reg, X_reg, weights=df["iptw"]).fit()
print(msm_model.summary())
