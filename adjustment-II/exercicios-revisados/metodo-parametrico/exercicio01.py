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

# Dados do problema
x = np.array([-6, -4, -2, 0])
y_medido = np.array([0.10, 0.97, 2.06, 3.11])

# a) Modelo Matemático
print("a) Modelo Matemático L_a = L_b + V")
print("   y = ax + b")
print("   -6a + b = 0,10 + v₁")
print("   -4a + b = 0,97 + v₂") 
print("   -2a + b = 2,06 + v₃")
print("    0a + b = 3,11 + v₄")
print()

# b) Vetor das observações
L_b = y_medido.reshape(-1, 1)
print("b) Vetor das observações L_b:")
print(L_b)
print()

# c) Matriz dos pesos
P = np.eye(4)
print("c) Matriz dos pesos P:")
print(P)
print()

# d) Tipo de solução
print("d) O modelo é LINEAR e tem SOLUÇÃO ÚNICA")
print("   Não é necessário aproximação inicial (X₀ = 0)")
print("   Número de observações (n) = 4")
print("   Número de parâmetros (u) = 2")
print()

# e) Cálculo de L
L = L_b.copy()
print("e) Vetor L = L_b:")
print(L)
print()

# f) Matriz A
A = np.column_stack([x, np.ones(4)])
print("f) Matriz A:")
print(A)
print()

# g) Equações Normais
N = A.T @ P @ A
U = A.T @ P @ L
X = np.linalg.inv(N) @ U

print("g) Equações Normais:")
print("   N = AᵀPA =")
print(N)
print()
print("   U = AᵀPL =")
print(U)
print()
print("   X = N⁻¹U =")
print(X)
print()

# h) Vetor dos Resíduos
V = A @ X - L_b
print("h) Vetor dos resíduos V:")
print(V)
print()

# i) Variância a posteriori
n = 4  # número de observações
u = 2  # número de parâmetros
sigma0_2 = (V.T @ P @ V) / (n - u)
print("i) Variância a posteriori σ₀²:")
print(f"   σ₀² = (VᵀPV)/(n-u) = {sigma0_2[0,0]:.6f}")
print()

# j) MVC dos parâmetros ajustados
Sigma_x = sigma0_2 * np.linalg.inv(N)
print("j) MVC dos parâmetros ajustados Σ_x:")
print(Sigma_x)
print()

# Resultados finais
print("RESULTADOS FINAIS:")
print(f"Parâmetro a = {X[0,0]:.3f} ± {np.sqrt(Sigma_x[0,0]):.6f}")
print(f"Parâmetro b = {X[1,0]:.3f} ± {np.sqrt(Sigma_x[1,1]):.6f}")
print()

# Significado das siglas
print("SIGNIFICADO DAS SIGLAS:")
print("L_a = Vetor dos valores observados ajustados")
print("L_b = Vetor dos valores observados")
print("V = Vetor dos resíduos")
print("P = Matriz dos pesos")
print("A = Matriz das derivadas parciais (Jacobiana)")
print("N = Matriz das equações normais (AᵀPA)")
print("U = Vetor AᵀPL")
print("X = Vetor correção dos parâmetros")
print("σ₀² = Variância a posteriori")
print("Σ_x = Matriz variância-covariância dos parâmetros ajustados")
print("MVC = Matriz Variância-Covariância")
print("n = Número de observações")
print("u = Número de parâmetros")
