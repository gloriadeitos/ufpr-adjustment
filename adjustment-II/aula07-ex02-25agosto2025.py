"""
EXERCÍCIOS: MÉTODO PARAMÉTRICO

Determinar as coordenadas planas (x,y) do ponto P, a partir da medida de três distâncias
de pontos conhecidos A, B e C até o P.

PONTO |  X (m)  |  Y(m)
  A   | 200,00  | 400,00
  B   | 600,00  | 700,00
  C   | 1100,00 | 300,00

Coordenadas aproximadas de 
P = (585,00; 112,00)m

Distâncias medidas com σ = 0,05m
AP = 499,92 m
BP = 600,02 m
CP = 538,48 m
"""

import numpy as np

# Matriz das observações (Lb)
Lb = np.array([
              [200, 400],
              [600, 700],
              [1100, 300]
])

# Matriz dos pesos (P)
Lb = np.array([
              []
])


# Matriz dos parâmetros ajustados (Xo)
Xo = np.array([
              [449.92],
              [600.02],
              [538.48]
])
