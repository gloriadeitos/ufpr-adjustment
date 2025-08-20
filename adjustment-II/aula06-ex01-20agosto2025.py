"""
Esse exercício ta muito ruim, precisa arrumar depois, não da pra entender absolutamente nada.

MÉTODO PARAMÉTRICO

O quadro e o esquema que se seguem resumem um nivelamento geométrico que partiu da referência
de nível A, de altitude nula. As setas indicam o sentido em que o terreno se eleva.

Linha | Desnível (m) | Comprimento (km)
  1   |    6,16      |        4
  2   |    12,57     |        2
  3   |    6,41      |        2
  4   |    1,09      |        4
  5   |    11,58     |        2
  6   |    5,07      |        4

Estimar as altitudes das estações B, C e D pelo método dos parâmetros.

Obs: Tomar pesos inversamente proporcionais ao comprimento das linhas.
"""

# =======================================================================================
# Não precisa fazer isso, é apenas o código pra mostrar a imagem que o professor passou
# para esse exercício, mostrada/plotada no terminal:
import matplotlib.pyplot as plt

# Coordenadas dos vértices
points = {
    'A': np.array([0, 0]),
    'B': np.array([4, 0]),
    'C': np.array([2, 2]),
    'D': np.array([2, 4])
}

# Arestas (início, fim, número, direção)
edges = [
    ('A', 'B', '1', (1, 0)),
    ('A', 'C', '2', (0.7, 1)),
    ('B', 'C', '3', (-0.7, 1)),
    ('A', 'D', '4', (1, 2)),
    ('C', 'D', '5', (0, 1)),
    ('B', 'D', '6', (-1, 2)),
]

fig, ax = plt.subplots(figsize=(6,6))

# Desenhar arestas
for start, end, num, arrow_dir in edges:
    x0, y0 = points[start]
    x1, y1 = points[end]
    ax.plot([x0, x1], [y0, y1], 'k')
    # Posição do número (do ladinho)
    xm, ym = (x0 + x1)/2, (y0 + y1)/2
    dx, dy = arrow_dir
    # desloca o número perpendicular à linha
    # vetor perpendicular (dy, -dx), normalizado
    perp = np.array([dy, -dx])
    perp = perp / np.linalg.norm(perp) if np.linalg.norm(perp) != 0 else perp
    offset = 0.25  # ajuste de distância do ladinho
    x_num = xm + perp[0]*offset
    y_num = ym + perp[1]*offset
    ax.text(x_num, y_num, num, color='black', fontsize=14, fontweight='bold', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='none', pad=0.5))
    # Desenhar seta
    ax.arrow(xm, ym, dx*0.15, dy*0.15, head_width=0.18, head_length=0.18, fc='black', ec='black', length_includes_head=True)

# Desenhar vértices
for label, (x, y) in points.items():
    ax.plot(x, y, 'ko')
    # Para o ponto C, colocar o texto abaixo do ponto
    if label == 'C':
        ax.text(x, y-0.2, label, fontsize=14, fontweight='bold', ha='center', va='top')
    else:
        ax.text(x, y+0.2, label, fontsize=14, fontweight='bold', ha='center')

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.show()

# =======================================================================================

# RESOLVENDO O EXERCÍCIO:

import numpy as np

# Dados (Lb) - Matriz das observações
# Nesse exercício, as observações são os desníveis, ou seja:
desnivel = np.array([
                     [6.16],
                     [12.57], 
                     [6.41],
                     [1.09],
                     [11.58],
                     [5.07]
                    ])

# Vai ser usada na matriz dos pesos:
comprimento = np.array([
                        [4],
                        [2],
                        [2],
                        [4],
                        [2],
                        [4]
                    ])

# O exercício pede para encontrar as altitudes dos pontos B, C e D pelo método dos parâmetros
# Para isso, basta resolver a FÓRMULA do Vetor de incógnitas, que é:

# X = (Aᵀ * P * A)⁻¹ * (Aᵀ * P * L)
# (O X é a matriz das incógnitas)

# Para resolve-la, precisa achar primeiro os valores de A, P e L, logo:

# Matriz dos coeficientes - (A)
"""
A fórmula da matriz dos coeficientes é:

A =                altitude_B                          |                    altitude_C                      |                   altitude_D
    [ (derivada da função 1 / derivada da altitude_B)     (derivada da função 1 / derivada da altitude_C)]      (derivada da função 1 / derivada da altitude_D) ]
    [ (derivada da função 2 / derivada da altitude_B)     (derivada da função 2 / derivada da altitude_C)]      (derivada da função 2 / derivada da altitude_D) ]
    [ (derivada da função 3 / derivada da altitude_B)     (derivada da função 3 / derivada da altitude_C)]      (derivada da função 3 / derivada da altitude_D) ]
    [ (derivada da função 4 / derivada da altitude_B)     (derivada da função 4 / derivada da altitude_C)]      (derivada da função 4 / derivada da altitude_D) ]
    [ (derivada da função 5 / derivada da altitude_B)     (derivada da função 5 / derivada da altitude_C)]      (derivada da função 5 / derivada da altitude_D) ]
    [ (derivada da função 6 / derivada da altitude_B)     (derivada da função 6 / derivada da altitude_C)]      (derivada da função 6 / derivada da altitude_D) ]

* OBS: A tabela desse exercício tem o valor de 6 desníveis (que são as nossas observações), como são 6 desníveis, temos então, 6 obervações, e 3 incógnitas (que são o valor da altitude de B, C e D)
       Por conta disso, a matriz dos coeficientes terá 6 linhas, sendo 1 função em cada linha, sendo 1 função para cada observação que temos no exercício.
"""
A = np.array([

])

# Matriz dos pesos (matriz identidade) - (P)
P = np.array([])

# Cálculo de L
# (L é a matriz de observações, e Lb também é a matriz das observações, a diferença é que Lb contém as incógnitas,
# enquanto L contém apenas as observações)
"""
L = Lb

L → vetor de observações
Lb → vetor de incógnitas
"""
L = desnivel
