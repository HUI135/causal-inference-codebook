import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("../data/simulated_health_data.csv")

# Fit model for outcome based on treatment and covariates
X = df[["treatment", "age", "sex", "hypertension"]]
y = df["outcome"]
model = LinearRegression().fit(X, y)

# Predict potential outcomes
df_0 = df.copy()
df_0["treatment"] = 0
y0 = model.predict(df_0[["treatment", "age", "sex", "hypertension"]])

df_1 = df.copy()
df_1["treatment"] = 1
y1 = model.predict(df_1[["treatment", "age", "sex", "hypertension"]])

# Estimate ATE
ate = np.mean(y1 - y0)
print(f"G-computation ATE: {ate:.3f}")
