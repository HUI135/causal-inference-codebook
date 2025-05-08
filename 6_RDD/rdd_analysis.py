import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# 시뮬레이션: RDD 구조 생성
np.random.seed(42)
n = 1000
df = pd.DataFrame({
    "score": np.random.uniform(0, 100, n)
})
df["treatment"] = (df["score"] >= 50).astype(int)
df["outcome"] = 2 * df["treatment"] + 0.1 * df["score"] + np.random.normal(0, 1, n)

# 회귀불연속 분석
df["score_centered"] = df["score"] - 50
model = smf.ols("outcome ~ treatment + score_centered", data=df).fit()
print(model.summary())

# 시각화
plt.scatter(df["score"], df["outcome"], alpha=0.3, label="Data")
plt.axvline(50, color="red", linestyle="--", label="Threshold")
plt.xlabel("Score")
plt.ylabel("Outcome")
plt.title("Regression Discontinuity Design")
plt.legend()
plt.tight_layout()
plt.show()
