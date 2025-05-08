import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("../data/simulated_health_data.csv")
ps_model = LogisticRegression()
X = df[["age", "sex", "hypertension"]]
ps_model.fit(X, df["treatment"])
df["pscore"] = ps_model.predict_proba(X)[:, 1]
treated = df[df["treatment"] == 1]
control = df[df["treatment"] == 0]
nn = NearestNeighbors(n_neighbors=1)
nn.fit(control[["pscore"]])
distances, indices = nn.kneighbors(treated[["pscore"]])
matched_controls = control.iloc[indices.flatten()]
matched_df = pd.concat([treated.reset_index(drop=True), matched_controls.reset_index(drop=True)])
model = sm.OLS(matched_df["outcome"], sm.add_constant(matched_df["treatment"])).fit()
print(model.summary())