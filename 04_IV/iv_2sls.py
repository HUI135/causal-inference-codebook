import pandas as pd
import numpy as np
from linearmodels.iv import IV2SLS

# Load data
df = pd.read_csv("../data/simulated_health_data.csv")
np.random.seed(42)

# Create instrument: random assignment (encouragement)
df["z"] = np.random.binomial(1, 0.5, len(df))  # instrument
df["treatment_iv"] = np.where(df["z"] == 1, df["treatment"], 0)  # imperfect compliance

# Estimate with 2SLS: outcome ~ treatment | instrument
model = IV2SLS.from_formula("outcome ~ 1 + [treatment_iv ~ z]", data=df).fit()
print(model.summary)
