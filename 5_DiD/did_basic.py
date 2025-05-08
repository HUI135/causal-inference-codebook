import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# 시뮬레이션: 두 시점, 두 그룹
np.random.seed(42)
n = 1000
df = pd.DataFrame({
    "id": np.arange(n),
    "group": np.random.binomial(1, 0.5, n),
    "time": np.random.binomial(1, 0.5, n)
})
df["treatment"] = df["group"] * df["time"]
df["outcome"] = 3 * df["treatment"] + 0.5 * df["group"] + 0.2 * df["time"] + np.random.normal(0, 1, n)

# DiD 회귀 분석
model = smf.ols("outcome ~ group + time + treatment", data=df).fit()
print(model.summary())
