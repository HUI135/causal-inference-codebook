import pandas as pd
import numpy as np
from pgmpy.estimators import PC
from pgmpy.models import BayesianModel

# 샘플 데이터 생성
np.random.seed(42)
df = pd.DataFrame()
df["X0"] = np.random.normal(size=500)
df["X1"] = np.random.normal(size=500)
df["X2"] = df["X0"] + np.random.normal(scale=0.1, size=500)
df["X3"] = df["X1"] + df["X2"] + np.random.normal(scale=0.1, size=500)

# PC 알고리즘 실행
pc = PC(data=df)
model = pc.estimate(return_type="dag")
print("Learned structure edges:")
print(model.edges())
