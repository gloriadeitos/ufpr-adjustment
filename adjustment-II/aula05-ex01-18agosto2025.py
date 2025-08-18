"""
Um fenômeno tem variação "y" linear com respeito a "x", representada pelo modelo matemático funcional "y=ax+b".
O valor "yᵢ" foi observado para diferentes "xᵢ", conforme dados abaixo. A abcissa "x" é considerada isenta de
erro. Calcular os valores ajustados dos parâmetros "a" e "b" da função linear.

Depois:
- Calcular vetor dos resíduos
- Calcular variância a posteriori
- Calcular a matriz variência-covariancia (MVC)

Para x | y medido
  -6   |   0.10
  -4   |   0.97
  -2   |   2.06
   0   |   3.11
"""

# ============================================================================================================
# RESOLUÇAO:
"""
==== 1)
Modelo matemático: Lₐ = Lb + V
* Essa equação é chamada de modelo de regressão linear, e é usada para descrever a relação entre as variáveis
observadas, as incógnitas e os resíduos.

Lₐ → vetor de observações
Lb → vetor de incógnitas
V → vetor de resíduos

y=ax+b

==== 2)
X = (Aᵀ * P * A)⁻¹ * (Aᵀ * P * L)
* Essa equação é chamada de estimativa dos parâmetros do modelo de regressão linear, e é usada para calcular
os valores ajustados dos parâmetros "a" e "b".

"""

import numpy as np 

# ===================================================================================
# Matriz dos coeficientes
A = np.array([
              [-6, 1],
              [-4, 1],
              [-2, 1],
              [0, 1]
            ])

# ===================================================================================
# Vetor das observações
Lb = np.array([
                [0.10],
                [0.97], 
                [2.06],
                [3.11]
            ])
print(f"Vetor das observações: \n Lb = \n {Lb} \n")

# ===================================================================================
# Matriz dos pesos (matriz identidade)
P = np.array([
              [1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]
            ])
print(f"Matriz dos pesos: \n P = \n {P} \n")
"""
A matriz identidade é usada pois não há pesos específicos para cada observação (as observações são as variáveis
independentes: x), então cada observação tem o mesmo peso, ou seja, são igualmente importante.

Ademais, é usada uma matriz 4x4 pois cada observação (são 4 valores de x) é representada por uma linha na matriz,
sendo que é na diagonal ao invés de tudo na mesma linha ou na mesma coluna pois os números na diagonal significam
que cada observação é independente e não há correlação entre elas, uma vez que, se estivessem na mesma linha ou na
mesma coluna, significaria que haveria correlação entre as observações.
"""

# ===================================================================================
# Verificando se a matriz A.T @ P @ A é invertível e mostrando seu valor
matriz_ATA = A.T @ P @ A
print("Matriz (Aᵀ * P * A):\n", matriz_ATA)
if np.linalg.det(matriz_ATA) == 0:
  print("A matriz NÃO É invertível. NÃO é possível ajustar o Modelo Linear.\n")
else:
  print("A matriz É invertível. Prosseguindo com o ajuste do Modelo Linear.\n")

# ===================================================================================
# Cálculo de L
"""
L = Lb

L → vetor de observações
Lb → vetor de incógnitas
"""
L = Lb
print(f"Vetor de observações: \n L = Lb = \n {L} \n")

# ===================================================================================
# *Parte opcional, porém bom pro professor corrigir:

# Equações Normais
print("\n ===================== \n*Parte opcional, porém bom pro professor corrigir:\n \nEquações Normais:")

# Matriz Normal
"""
N = AᵀPA

N → matriz normal
A → matriz dos coeficientes
P → matriz de pesos
L → vetor de observações
"""
N = A.T @ P @ A
print(f"Matriz Normal (N = Aᵀ * P * A): \n N = \n {N} \n")

# Vetor das incógnitas
"""
U = AᵀPL

U → vetor de incógnitas
Aᵀ → matriz transposta dos coeficientes
P → matriz de pesos
L → vetor de observações
"""
U = A.T @ P @ L
print(f"Vetor de incógnitas (U = Aᵀ * P * L): \n U = \n {U} \n")

#
"""
X = N⁻¹U

X → vetor de incógnitas [a, b]
N⁻¹ → matriz inversa da matriz normal
U → vetor de incógnitas
"""
print("===================== \n")

# ===================================================================================
# Vetor de incógnitas [a, b]
"""
X = (Aᵀ * P * A)⁻¹ * (Aᵀ * P * L)
"""
X = np.linalg.inv(A.T @ P @ A) @ (A.T @ P @ L) # o @ serve para multiplicação de matrizes
# O np.linalg.inv calcula a inversa da matriz

a, b = X

# Imprimindo o resultado
print(f"Valor ajustado de a: {a} \n")
print(f"Valor ajustado de b: {b} \n")

# ===== Parte2

# Calcular vetor dos resíduos
"""
V = AX + L

V → vetor dos resíduos
A → matriz dos coeficientes
X → vetor de incógnitas
L → vetor de observações
"""
V = Lb - (A @ X)
print(f"Vetor dos resíduos: \n V=AX+L = \n {V} \n")

# Calcular variância a posteriori
n = len(Lb) # número de observações
r = len(X) # número de incógnitas
variancia_posteriori = (V.T @ P @ V) / (n - r)
print(f"Variância a posteriori: \n σ̂ = \n {variancia_posteriori} \n")

# Calcular matriz variância-covariância (MVC)
MVC = variancia_posteriori * np.linalg.inv(A.T @ P @ A)
print("Matriz variância-covariância (MVC):")
print(MVC)

# ==========================================================================================================
# OQ O PROFESSOR ESCREVEU NO QUADRO:
"""
y=ax+b
incógnitas → "a" e "b"

-6a + b = 0.10
-4a + b = 0.97
-2a + b = 2.06
 0a + b = 3.11

X = (Aᵀ * P * A)⁻¹ * (Aᵀ * P * L)

X → vetor de incógnitas [a, b]
A → matriz dos coeficientes
P → matriz de pesos
L → vetor de observações
"""
