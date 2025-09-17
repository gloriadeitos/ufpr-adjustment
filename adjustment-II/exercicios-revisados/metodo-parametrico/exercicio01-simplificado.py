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

# Dados
x = [-6, -4, -2, 0]
y = [0.10, 0.97, 2.06, 3.11]

# a) Modelo Matemático
print("a) Modelo: y = ax + b")
print("   -6a + b = 0,10 + v1")
print("   -4a + b = 0,97 + v2")
print("   -2a + b = 2,06 + v3")
print("    0a + b = 3,11 + v4")

# b) Vetor observações
Lb = np.array(y).reshape(-1, 1)
print("\nb) Lb =")
print(Lb)

# c) Matriz pesos
P = np.eye(4)
print("\nc) P =")
print(P)

# d) Tipo de solução
print("\nd) Modelo LINEAR - Solução única")
print("   X0 = 0 (não precisa aproximação inicial)")

# e) Vetor L
L = Lb.copy()
print("\ne) L = Lb =")
print(L)

# f) Matriz A
A = np.column_stack([x, [1,1,1,1]])
print("\nf) A =")
print(A)

# g) Equações normais
N = A.T @ P @ A
U = A.T @ P @ L
X = np.linalg.inv(N) @ U
print("\ng) N = AᵀPA =")
print(N)
print("U = AᵀPL =")
print(U)
print("X = N⁻¹U =")
print(X)

# h) Resíduos
V = A @ X - Lb
print("\nh) V = AX - Lb =")
print(V)

# i) Variância
n, u = 4, 2
sigma2 = (V.T @ P @ V) / (n - u)
print("\ni) σ₀² = (VᵀPV)/(n-u) =")
print(f"{sigma2[0,0]:.6f}")

# j) MVC
Sigma_x = sigma2 * np.linalg.inv(N)
print("\nj) Σ_x = σ₀²N⁻¹ =")
print(Sigma_x)

# Resultados finais
print(f"\nRESULTADO: a = {X[0,0]:.3f}, b = {X[1,0]:.3f}")
