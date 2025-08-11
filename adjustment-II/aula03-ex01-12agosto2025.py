"""
MÉTODO DOS MÍNIMOS QUADRADOS

Aplicando o princípio de MMQ resolver o sistemas de equações

{ x + y + z = 9
{ 2x + y + z = 11
{ x + 2y + z = 12
{ 4x + 3y + 4z = 33
*é um sistema, então tudo é no mesmo {

{ x + y + z = 9
{ 2x + y + z = 11
{ 3x + 2y + 2z = 20
{ -y -z = -7
*é um sistema, então tudo é no mesmo {

Temos que:
A * X = L
A → matriz do sistema de equações
X → matriz das incógnitas
L → matriz das observações

X = (A_transposta * A)^-1 * (A_transposta * L)
"""

import numpy as np

# Define a matriz A e vetor L
A = np.array([[1, 1, 1],
              [2, 1, 1],
              [1, 2, 1],
              [4, 3, 4]])

L = np.array([[9],
              [11],
              [12],
              [33]])

# Calculando:
# X = (A_transposta * A)^-1 * (A_transposta * L)
X = np.linalg.inv(A.T @ A) @ A.T @ L

"""
Mesma resolução de X, porém passo-a-passo

# Transposta de A
A_transposta = A.T

# A_transposta * A
AtA = np.dot(A_transposta, A)

# Inversa de AtA
AtA_inv = np.linalg.inv(AtA)

# A_transposta * L
AtL = np.dot(A_transposta, L)

# Resposta
X = np.dot(AtA_inv, AtL)

print("X =")
print(X)
"""

# Resposta com 3 casas decimais
print("X =")
for valor in X:
    print(f"[{valor[0]:.3f}]")
