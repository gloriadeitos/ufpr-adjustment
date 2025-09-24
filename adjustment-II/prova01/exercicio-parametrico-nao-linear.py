import numpy as np

# MODELO NÃO-LINEAR
def modelo(X, x):
    a, b = X
    return a * np.exp(b * x)

# DADOS
x_dados = np.array([1, 2, 3])
L_b = np.array([3.5, 5.0, 8.0])
X_a = np.array([2.0, 0.5])  # Chute inicial

# AJUSTE ITERATIVO
for i in range(10):
    L0 = modelo(X_a, x_dados)  # Valores aproximados
    L = L0 - L_b  # Termos independentes
    
    # Jacobiano (derivadas)
    a, b = X_a
    A = np.column_stack([
        np.exp(b * x_dados),           # df/da
        a * x_dados * np.exp(b * x_dados)  # df/db
    ])
    
    # Correção
    dX = -np.linalg.inv(A.T @ A) @ A.T @ L
    X_a += dX
    
    if np.linalg.norm(dX) < 1e-6:
        break

print("Parâmetros finais:", X_a)



