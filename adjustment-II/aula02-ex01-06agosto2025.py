"""
O MÉTODO DOS MÍNIMOS QUADRADOS: EXEMPLO

Dada a inconsistência das equações, podemos ter 4 soluções diferentes:

{ x + 2y - 2z = -1
{ 3x - 2y + z = 2
{ 2x - 3y+ 2z = 2
{ 3x - y + 2z = 6 
*é um sistema, então tudo é no mesmo {

a) Sistema composto pelas equações 1, 2 e 3.
b) Sistema composto pelas equações 1, 2 e 4.
c) Sistema composto pelas equações 1, 3 e 4.
d) Sistema composto pelas equações 2, 3 e 4.
"""

# ===================================================================================
# a) Sistema composto pelas equações 1, 2 e 3
"""
Escrevendo na forma matricial temos → [1 2 -2] [x]   [-1 ]
                                      [3 -2 1] [y] = [ 2 ]
                                      [2 -3 2] [z]   [ 2 ]

Onde:
    [1 2 -2]        [x]        [-1 ]
A = [3 -2 1]    X = [y]     L= [ 2 ]
    [2 -3 2]        [z]        [ 2 ]

Temos então, que:
X = ?
"""

import numpy as np

# Sistema de equações 1, 2 e 3
A = np.array([[1, 2, -2],
              [3, -2, 1],
              [2, -3, 2]])

# Matriz das observações L
L = np.array([[-1],
               [2], 
               [2]])

# Calculando a matriz inversa de A
A_inv = np.linalg.inv(A)

# Matriz das incógnitas de X
X = np.dot(A_inv, L)
X = A_inv @ L  # Alternativa mais comum para multiplicação de matrizes

# ===================================================================================
# b) Sistema composto pelas equações 1, 2 e 4
"""
Escrevendo na forma matricial temos → [1 2 -2] [x]   [-1 ]
                                      [3 -2 1] [y] = [ 2 ]
                                      [3 -1 2] [z]   [ 6 ]

Onde:
    [1 2 -2]        [x]        [-1 ]
A = [3 -2 1]    X = [y]     L= [ 2 ]
    [3 -1 2]        [z]        [ 6 ]

Temos então, que:
X = ?
"""
# Sistema de equações 1, 2 e 4
A_letraB = np.array([[1, 2, -2],
                     [3, -2, 1],
                     [3, -1, 2]])

# Matriz das observações L
L_letraB = np.array([[-1],
                     [2], 
                     [6]])

# Calculando a matriz inversa de A
A_inv_letraB = np.linalg.inv(A_letraB)

# Matriz das incógnitas de X
X_letraB = np.dot(A_inv_letraB, L_letraB)
X_letraB = A_inv_letraB @ L_letraB # Multiplicação de matrizes

# ===================================================================================
# c) Sistema composto pelas equações 1, 3 e 4
"""
Escrevendo na forma matricial temos → [1 2 -2] [x]   [-1 ]
                                      [2 -3 2] [y] = [ 2 ]
                                      [3 -1 2] [z]   [ 6 ]

Onde:
    [1 2 -2]        [x]        [-1 ]
A = [2 -3 2]    X = [y]     L= [ 2 ]
    [3 -1 2]        [z]        [ 6 ]

Temos então, que:
X = ?
"""
# Sistema de equações 1, 3 e 4
A_letraC = np.array([[1, 2, -2],
              [2, -3, 2],
              [3, -1, 2]])

# Matriz das observações L
L_letraC = np.array([[-1],
               [2], 
               [6]])

# Calculando a matriz inversa de A
A_inv_letraC = np.linalg.inv(A_letraC)

# Matriz das incógnitas de X
X_letraC = np.dot(A_inv_letraC, L_letraC)
X_letraC = A_inv_letraC @ L_letraC  # Multiplicação de matrizes

# ===================================================================================
# d) Sistema composto pelas equações 2, 3 e 4
"""
Escrevendo na forma matricial temos → [3 -2 1] [x]   [ 2 ]
                                      [2 -3 2] [y] = [ 2 ]
                                      [3 -1 2] [z]   [ 6 ]

Onde:
    [3 -2 1]        [x]        [ 2 ]
A = [2 -3 2]    X = [y]     L= [ 2 ]
    [3 -1 2]        [z]        [ 6 ]

Temos então, que:
X = ?
"""
# Sistema de equações 2, 3 e 4
A_letraD = np.array([[3, -2, 1],
              [2, -3, 2],
              [3, -1, 2]])

# Matriz das observações L
L_letraD = np.array([[2],
               [2], 
               [6]])

# Calculando a matriz inversa de A
A_inv_letraD = np.linalg.inv(A_letraD)

# Matriz das incógnitas de X
X_letraD = np.dot(A_inv_letraD, L_letraD)
X_letraD = A_inv_letraD @ L_letraD  # Multiplicação de matrizes

# ===================================================================================
# Exibindo os resultados

# Define a precisão e o formato de exibição dos números do numpy para facilitar a leitura dos resultados
np.set_printoptions(precision=4, suppress=True)

# Função para formatar a matriz de forma mais legível, com 4 casas decimais alinhadas
def format_matrix(mat):
    return np.array2string(mat, formatter={'float_kind':lambda x: f"{x:8.4f}"})

print("Solução do sistema composto pelas equações 1, 2 e 3:\n X = \n", format_matrix(X), 
    "\n\nSolução do sistema composto pelas equações 1, 2 e 4:\n X' = \n", format_matrix(X_letraB), 
    "\n\nSolução do sistema composto pelas equações 1, 3 e 4:\n X'' = \n", format_matrix(X_letraC), 
    "\n\nSolução do sistema composto pelas equações 2, 3 e 4:\n X''' = \n", format_matrix(X_letraD))
