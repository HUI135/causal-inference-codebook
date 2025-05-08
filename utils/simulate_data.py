import numpy as np
import pandas as pd

def simulate_health_data(seed=42, n=1000):
    np.random.seed(seed)
    age = np.random.normal(60, 10, n)
    sex = np.random.binomial(1, 0.5, n)
    hypertension = np.random.binomial(1, 0.3 + 0.01 * (age - 60), n)
    treatment = np.random.binomial(1, 0.4 + 0.1 * hypertension - 0.05 * sex, n)
    outcome = 2 * treatment + 0.5 * hypertension - 0.3 * sex + 0.01 * age + np.random.normal(0, 1, n)
    df = pd.DataFrame({"age": age, "sex": sex, "hypertension": hypertension, "treatment": treatment, "outcome": outcome})
    return df

if __name__ == "__main__":
    df = simulate_health_data()
    df.to_csv("data/simulated_health_data.csv", index=False)