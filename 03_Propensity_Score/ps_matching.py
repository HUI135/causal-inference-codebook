import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
import statsmodels.api as sm

# Load data
df = pd.read_csv("../data/simulated_health_data.csv")

# Estimate propensity scores
X = df[["age", "sex", "hypertension"]]
y = df["treatment"]
ps_model = LogisticRegression()
ps_model.fit(X, y)
df["pscore"] = ps_model.predict_proba(X)[:, 1]

# Nearest neighbor matching based on propensity score
treated = df[df["treatment"] == 1]
control = df[df["treatment"] == 0]

nn = NearestNeighbors(n_neighbors=1)
nn.fit(control[["pscore"]])
_, indices = nn.kneighbors(treated[["pscore"]])
matched_control = control.iloc[indices.flatten()]

matched_df = pd.concat([treated.reset_index(drop=True), matched_control.reset_index(drop=True)])

# Estimate ATE
X_matched = sm.add_constant(matched_df["treatment"])
y_matched = matched_df["outcome"]
model = sm.OLS(y_matched, X_matched).fit()
print(model.summary())
