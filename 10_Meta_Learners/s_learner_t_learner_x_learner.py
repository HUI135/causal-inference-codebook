import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from causalml.inference.meta import BaseSClassifier, BaseTClassifier, BaseXClassifier
from causalml.dataset import synthetic_data

# Load sample data (or replace with actual)
df = pd.read_csv("../data/simulated_health_data.csv")
y = df["outcome"].values
treatment = df["treatment"].values
X = df[["age", "sex", "hypertension"]].values

# S-learner
s_learner = BaseSClassifier(learner=RandomForestRegressor())
s_te, s_lb, s_ub = s_learner.estimate_ate(X=X, treatment=treatment, y=y)
print("S-learner ATE:", s_te)

# T-learner
t_learner = BaseTClassifier(learner=RandomForestRegressor())
t_te, t_lb, t_ub = t_learner.estimate_ate(X=X, treatment=treatment, y=y)
print("T-learner ATE:", t_te)

# X-learner
x_learner = BaseXClassifier(learner=RandomForestRegressor())
x_te, x_lb, x_ub = x_learner.estimate_ate(X=X, treatment=treatment, y=y)
print("X-learner ATE:", x_te)
