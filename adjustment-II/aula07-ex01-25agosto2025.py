"""
EXERCÍCIOS: MÉTODO PARAMÉTRICO

As duas escalas representadas na figura são uniformes. Com isso, foram realizadas leituras na
escala B em correspondência a valores cheios da escala A.

  A | B
  7 | 63,10
  8 | 89,15
 10 | 141,40
 12 | 193,45
 13 | 219,50
 14 | 245,60

 X₀ = [x⁰₁] = [63,10]
      [x⁰₂]   [26,05]

As observações não são consistentes entre si. Ajustar os valores observados exprimindo uma 
unidade da escala A em unidades da escala B.
"""

# Mostrar imagem do exercício no terminal
import matplotlib.pyplot as plt
from PIL import Image

# Mostrar imagem do exercício no terminal
img_path = './img/aula07-01.jpg'
img = Image.open(img_path)
plt.imshow(img)
plt.axis('off')
plt.show()

# RESOLVENDO O EXERCÍCIO:

import numpy as np

# Dados
escala_A = np.array([[7],
                     [8],
                     [10],
                     [12],
                     [13],
                     [14]
                    ])

escala_B = np.array([[63.10],
                     [89.15],
                     [141.40],
                     [193.45],
                     [219.50],
                     [245.60]
                    ])

# 1º PASSO: Montar a matriz do sistema de equações

# 2º PASSO: Matriz das incógnitas - (Matriz X)
# X = (Aᵀ * P * A)⁻¹ * (Aᵀ * P * L)

# 2º PASSO: Matriz dos coeficientes - (Matriz A)

# 3º PASSO: Matriz dos pesos (matriz identidade) - (Matriz P)

# 4º PASSO: Cálculo de L
# (L é a matriz de observações, e Lb também é a matriz das observações, a diferença é que Lb contém as incógnitas,
# enquanto L contém apenas as observações)


# 1º PASSO: Montar a matriz do sistema de equações
# Modelo: B = a*A + b
# A matriz de coeficientes terá uma coluna de A e uma de 1 (para o termo independente)
A = np.hstack([escala_A, np.ones_like(escala_A)])

# 2º PASSO: Matriz dos coeficientes - (Matriz A)
# Já montada acima como 'A'

# 3º PASSO: Matriz dos pesos (matriz identidade) - (Matriz P)
P = np.eye(len(escala_A))

# 4º PASSO: Cálculo de L (matriz das observações)
L = escala_B

# 5º PASSO: Ajuste dos parâmetros (a, b) usando mínimos quadrados
# X = (Aᵀ * P * A)⁻¹ * (Aᵀ * P * L)
AtPA = A.T @ P @ A
AtPL = A.T @ P @ L
X = np.linalg.inv(AtPA) @ AtPL

a, b = X.flatten()
print(f"Coeficiente a (escala): {a:.5f}")
print(f"Coeficiente b (intercepto): {b:.5f}")

# 6º PASSO: Mostrar ajuste
print("\nAjuste: B = {:.5f} * A + {:.5f}".format(a, b))
