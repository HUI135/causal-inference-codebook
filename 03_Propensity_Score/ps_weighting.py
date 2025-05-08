import pandas as pd
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

# Compute IPTW weights
df["weight"] = df["treatment"] / df["pscore"] + (1 - df["treatment"]) / (1 - df["pscore"])

# Weighted regression
X_reg = sm.add_constant(df["treatment"])
y_reg = df["outcome"]
wls_model = sm.WLS(y_reg, X_reg, weights=df["weight"]).fit()
print(wls_model.summary())
