import pandas as pd
import numpy as np
from zepid import load_sample_data
from zepid.causal.tmle import TMLE
from sklearn.linear_model import LogisticRegression, LinearRegression

# Load data
df = pd.read_csv("../data/simulated_health_data.csv")

# TMLE 수행
tmle = TMLE(df, exposure='treatment', outcome='outcome')
tmle.exposure_model("age + sex + hypertension", model=LogisticRegression())
tmle.outcome_model("treatment + age + sex + hypertension", model=LinearRegression())
tmle.fit()
print("TMLE ATE:", tmle.ate)
print("95% CI:", tmle.ate_ci)
