import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.read_csv("../data/simulated_health_data.csv")

df["treatment_rct"] = np.random.binomial(1, 0.5, len(df))

# ITT 분석
X = sm.add_constant(df["treatment_rct"])
y = df["outcome"]
model = sm.OLS(y, X).fit()

print(model.summary())

# 시각화
plt.hist(df[df["treatment_rct"] == 1]["outcome"], alpha=0.6, label="Treated")
plt.hist(df[df["treatment_rct"] == 0]["outcome"], alpha=0.6, label="Control")
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.title("RCT Outcome Distribution")
plt.legend()
plt.tight_layout()
plt.show()
