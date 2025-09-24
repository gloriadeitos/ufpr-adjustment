import numpy as np

# DADOS
L_b = np.array([10.2, 20.5, 30.8])  # Observações
A = np.column_stack([np.ones(3), [1, 2, 3]])  # Matriz A

# CÁLCULOS
P = np.eye(3)  # Pesos (identidade)
N = A.T @ P @ A
U = A.T @ P @ L_b
X = np.linalg.inv(N) @ U  # Parâmetros

V = A @ X - L_b  # Resíduos
n, u = len(L_b), A.shape[1]
sigma2_0 = (V.T @ P @ V) / (n - u)

print("Parâmetros:", X)






