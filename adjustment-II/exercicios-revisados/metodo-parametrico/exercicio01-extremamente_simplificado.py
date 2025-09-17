"""
 Um fenômeno tem variação 𝐲 linear com respeito a 𝒙, representada pelo
 modelo matemático funcional 𝒚 = 𝒂𝒙+𝒃. O valor 𝒚_𝒊 foi observado para
 diferentes 𝒙_𝒊 , conforme dados abaixo. A abcissa 𝒙 é considerada isenta de
 erro. Calcular os valores ajustados dos parâmetros 𝒂 e 𝒃 da função linear
 
Para x | y medido
  -6   |   0.10
  -4   |   0.97
  -2   |   2.06
   0   |   3.11
   
Resolver o exercício e printar no terminal:
a) Modelo Matemático L_a=Lb+V
b) Vetor das observações
c) Matriz dos pesos
d) Responder se tem ou não tem solução. Se tiver, dizer quantas e qual o modelo.
e) Cálculo de L
f) Matriz A
g) Equações Normais
h) Vetor dos Resíduos
i) Variância a posteriori
j) MVC dos parâmetros ajustados

Imprimir também no terminal o significado de todas as siglas que existirem, sendo:
Sigla = Significado da Siga
"""

import numpy as np

# Dados básicos
x = [-6, -4, -2, 0]
y = [0.10, 0.97, 2.06, 3.11]

# 1. Modelo
print("y = ax + b")

# 2. Matrizes principais
Lb = np.array(y).reshape(-1, 1)
P = np.eye(4)
A = np.column_stack([x, [1,1,1,1]])

# 3. Cálculos
N = A.T @ P @ A
U = A.T @ P @ Lb
X = np.linalg.inv(N) @ U
V = A @ X - Lb

# 4. Resultados
sigma2 = (V.T @ P @ V) / 2
Sigma_x = sigma2 * np.linalg.inv(N)

print(f"a = {X[0,0]:.3f}")
print(f"b = {X[1,0]:.3f}")
print(f"Resíduos: {V.flatten()}")
