import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv("../data/simulated_health_data.csv")

# Estimate propensity scores
X = df[["age", "sex", "hypertension"]]
y = df["treatment"]
ps_model = LogisticRegression()
ps_model.fit(X, y)
df["pscore"] = ps_model.predict_proba(X)[:, 1]

# Plot distribution
sns.kdeplot(df[df["treatment"] == 1]["pscore"], label="Treated", fill=True)
sns.kdeplot(df[df["treatment"] == 0]["pscore"], label="Control", fill=True)
plt.title("Propensity Score Distribution")
plt.xlabel("Propensity Score")
plt.legend()
plt.tight_layout()
plt.show()
