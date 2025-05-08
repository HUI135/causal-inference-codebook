import pandas as pd
import numpy as np
from notears.linear import notears_linear
from sklearn.preprocessing import StandardScaler

# 시뮬레이션 데이터 생성
np.random.seed(42)
n = 500
X = np.random.randn(n, 4)
X[:, 2] = 0.8 * X[:, 0] + np.random.normal(0, 0.1, n)  # Causal: X0 → X2
X[:, 3] = 0.5 * X[:, 1] + 0.3 * X[:, 2] + np.random.normal(0, 0.1, n)  # X1 → X3, X2 → X3

# NOTEARS 실행
W_est = notears_linear(X, lambda1=0.01)
print("Estimated adjacency matrix:")
print(np.round(W_est, 2))
