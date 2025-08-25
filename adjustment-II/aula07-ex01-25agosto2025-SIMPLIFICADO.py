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

OBSERVAÇOES SOBRE A RESOLUÇAO DO EXERCÍCIO:
a) Modelo Matemático
b) Vetor das observações
c) Matriz dos Pesos
d) Solução inicial aproximada: Modelo Linear
e) Cálculo de L
f) Matriz A
g) Equações Normais
h) Variância a posteriori
i) Parâmetros ajustados
j) Vetor dos Resíduos
k) Observações ajustadas

*Tudo deve aparecer como resposta, juntamente de um texto explicativo de cada um, sendo que
quando houver fórmulas, colocar qual é a fórmula e o que significa cada letra/matriz, ademais,
as respostas no terminam devem ser faceis de ler, com divisórias e etc. Escrever quais são
os passos pra resolução do exercício (1º PASSO, 2º PASS0...) e como resolver cada etapa.
"""

# OBS: Esse código é o jeito simples, curto e direto pra resolver o exercício, porém ainda tendo as respostas
# por etapa

import numpy as np

# Dados do problema
A = np.array([7, 8, 10, 12, 13, 14])  # Valores da escala A
B = np.array([63.10, 89.15, 141.40, 193.45, 219.50, 245.60])  # Valores da escala B

print("=" * 50)
print("MÉTODO PARAMÉTRICO - AJUSTAMENTO DE ESCALAS")
print("=" * 50)

# 1. Vetor das observações (Lb)
print("\n1. VETOR DAS OBSERVAÇÕES (Lb):")
Lb = B.reshape(-1, 1)
print(Lb)

# 2. Matriz dos pesos (P) - identidade (pesos unitários)
print("\n2. MATRIZ DOS PESOS (P):")
P = np.eye(len(B))
print(P)

# 3. Solução inicial aproximada (X0)
print("\n3. SOLUÇÃO INICIAL (X0):")
X0 = np.array([[63.10], [26.05]])
print(X0)

# 4. Cálculo do vetor L = L0 - Lb
print("\n4. VETOR L = L0 - Lb:")
coeffs = [0, 1, 3, 5, 6, 7]  # Coeficientes de x2 para cada observação
L0 = np.array([X0[0] + c * X0[1] for c in coeffs])
L = L0 - Lb
print(L)

# 5. Matriz A (coeficientes)
print("\n5. MATRIZ A (COEFICIENTES):")
A_mat = np.column_stack((np.ones(len(B)), coeffs))
print(A_mat)

# 6. Equações normais
print("\n6. EQUAÇÕES NORMAIS:")
N = A_mat.T @ P @ A_mat  # N = AᵀPA
U = A_mat.T @ P @ L      # U = AᵀPL
print("N = AᵀPA =")
print(N)
print("\nU = AᵀPL =")
print(U)

# 7. Solução do sistema: X = -N⁻¹U
print("\n7. SOLUÇÃO DO SISTEMA:")
X_correcao = -np.linalg.inv(N) @ U
print("X = -N⁻¹U =")
print(X_correcao)

# 8. Parâmetros ajustados
print("\n8. PARÂMETROS AJUSTADOS:")
X_ajustado = X0 + X_correcao
print("Xₐ = X₀ + X =")
print(X_ajustado)
print(f"\nUma unidade da escala A corresponde a {X_ajustado[1,0]:.6f} unidades da escala B")

# 9. Vetor dos resíduos
print("\n9. VETOR DOS RESÍDUOS:")
V = A_mat @ X_correcao + L
print("V = AX + L =")
print(V)

# 10. Observações ajustadas
print("\n10. OBSERVAÇÕES AJUSTADAS:")
L_ajustado = Lb + V
print("Lₐ = L_b + V =")
print(L_ajustado)

# 11. Variância a posteriori
print("\n11. VARIÂNCIA A POSTERIORI:")
gl = len(B) - 2  # graus de liberdade
sigma0_quadrado = (V.T @ P @ V) / gl
print(f"σ₀² = {sigma0_quadrado[0,0]:.8f}")

print("\n" + "=" * 50)
print("RESULTADO FINAL:")
print(f"UMA UNIDADE DA ESCALA A = {X_ajustado[1,0]:.6f} UNIDADES DA ESCALA B")
print("=" * 50)
