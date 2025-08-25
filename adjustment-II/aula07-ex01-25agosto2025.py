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

import numpy as np
import pandas as pd

# =============================================================================
# 1º PASSO: DEFINIÇÃO DO PROBLEMA E DADOS INICIAIS
# =============================================================================
print("=" * 70)
print("EXERCÍCIO: MÉTODO PARAMÉTRICO - AJUSTAMENTO DE ESCALAS")
print("=" * 70)

print("\n1º PASSO: DADOS DO PROBLEMA")
print("-" * 40)

# Dados das observações
A_values = [7, 8, 10, 12, 13, 14]  # Valores da escala A
B_values = [63.10, 89.15, 141.40, 193.45, 219.50, 245.60]  # Valores da escala B

# Solução inicial aproximada
X0 = np.array([63.10, 26.05])  # [x1⁰, x2⁰]

print(f"Valores da escala A: {A_values}")
print(f"Valores da escala B: {B_values}")
print(f"Solução inicial X₀: {X0}")

# =============================================================================
# 2º PASSO: MODELO MATEMÁTICO (a)
# =============================================================================
print("\n" + "=" * 70)
print("2º PASSO: MODELO MATEMÁTICO")
print("-" * 40)

print("Modelo: L_a = L_b + V = F(X)")
print("Onde:")
print("L_a = vetor das observações ajustadas")
print("L_b = vetor das observações brutas")
print("V = vetor dos resíduos")
print("X = vetor dos parâmetros [x1, x2]")
print("\nEquações específicas:")
print("l₁ᵃ = 63,10 + v₁ = x₁")
print("l₂ᵃ = 89,15 + v₂ = x₁ + x₂")
print("l₃ᵃ = 141,40 + v₃ = x₁ + 3x₂")
print("l₄ᵃ = 193,45 + v₄ = x₁ + 5x₂")
print("l₅ᵃ = 219,50 + v₅ = x₁ + 6x₂")
print("l₆ᵃ = 245,60 + v₆ = x₁ + 7x₂")

# =============================================================================
# 3º PASSO: VETOR DAS OBSERVAÇÕES (b)
# =============================================================================
print("\n" + "=" * 70)
print("3º PASSO: VETOR DAS OBSERVAÇÕES")
print("-" * 40)

Lb = np.array(B_values).reshape(-1, 1)
print("L_b =")
print(Lb)

# =============================================================================
# 4º PASSO: MATRIZ DOS PESOS (c)
# =============================================================================
print("\n" + "=" * 70)
print("4º PASSO: MATRIZ DOS PESOS")
print("-" * 40)

n = len(Lb)
P = np.eye(n)  # Matriz identidade (pesos unitários)
print("P = (matriz identidade - pesos unitários)")
print(P)

# =============================================================================
# 5º PASSO: SOLUÇÃO INICIAL APROXIMADA (d)
# =============================================================================
print("\n" + "=" * 70)
print("5º PASSO: SOLUÇÃO INICIAL APROXIMADA")
print("-" * 40)

print(f"X₀ = [{X0[0]:.2f}, {X0[1]:.2f}]ᵀ")
print("Onde:")
print("x₁⁰ = 63,10 (valor inicial para o parâmetro x₁)")
print("x₂⁰ = 26,05 (valor inicial para o parâmetro x₂)")

# =============================================================================
# 6º PASSO: CÁLCULO DE L (e)
# =============================================================================
print("\n" + "=" * 70)
print("6º PASSO: CÁLCULO DO VETOR L")
print("-" * 40)

# Coeficientes para cada observação (multiplicadores de x2)
coeffs = [0, 1, 3, 5, 6, 7]  # Coeficientes baseados nas diferenças da escala A
# Calculando as diferenças em relação ao primeiro valor (7):
# A=7:  7-7 = 0
# A=8:  8-7 = 1  
# A=10: 10-7 = 3
# A=12: 12-7 = 5
# A=13: 13-7 = 6
# A=14: 14-7 = 7

# Cálculo de L0 (valores calculados com a solução inicial)
L0 = np.array([X0[0] + coeff * X0[1] for coeff in coeffs]).reshape(-1, 1)

# Vetor L = L0 - Lb
L = L0 - Lb

print("L₀ (valores calculados com X₀) =")
print(np.array2string(L0.flatten(), precision=2, separator=', '))

print("\nL = L₀ - L_b =")
print(np.array2string(L.flatten(), precision=2, separator=', '))

# =============================================================================
# 7º PASSO: MATRIZ A (f)
# =============================================================================
print("\n" + "=" * 70)
print("7º PASSO: MATRIZ A (MATRIZ DOS COEFICIENTES)")
print("-" * 40)

# Construção da matriz A
A = np.ones((n, 2))
A[:, 1] = coeffs

print("A =")
print(A)
print("\nOnde:")
print("Coluna 1: coeficientes de x₁ (sempre 1)")
print("Coluna 2: coeficientes de x₂ (baseados na escala A)")

# =============================================================================
# 8º PASSO: EQUAÇÕES NORMAIS (g)
# =============================================================================
print("\n" + "=" * 70)
print("8º PASSO: EQUAÇÕES NORMAIS")
print("-" * 40)

# Cálculo da matriz N = AᵀPA
N = A.T @ P @ A

# Cálculo do vetor U = AᵀPL
U = A.T @ P @ L

print("N = AᵀPA =")
print(N)

print("\nU = AᵀPL =")
print(U)

# Solução do sistema NX = -U
X_correcao = -np.linalg.inv(N) @ U

print(f"\nX (correção) = -N⁻¹U = [{X_correcao[0,0]:.6f}, {X_correcao[1,0]:.6f}]ᵀ")

# =============================================================================
# 9º PASSO: PARÂMETROS AJUSTADOS (i)
# =============================================================================
print("\n" + "=" * 70)
print("9º PASSO: PARÂMETROS AJUSTADOS")
print("-" * 40)

X_ajustado = X0.reshape(-1, 1) + X_correcao

print("Xₐ = X₀ + X =")
print(f"[{X_ajustado[0,0]:.6f}]")
print(f"[{X_ajustado[1,0]:.6f}]")

print("\nInterpretação:")
print(f"x₁ₐ = {X_ajustado[0,0]:.6f} (valor de B correspondente a A=7)")
print(f"x₂ₐ = {X_ajustado[1,0]:.6f} (valor de uma unidade de A em unidades de B)")

# =============================================================================
# 10º PASSO: VETOR DOS RESÍDUOS (j)
# =============================================================================
print("\n" + "=" * 70)
print("10º PASSO: VETOR DOS RESÍDUOS")
print("-" * 40)

V = A @ X_correcao + L

print("V = AX + L =")
for i, residuo in enumerate(V.flatten(), 1):
    print(f"v{i} = {residuo:.6f}")

# =============================================================================
# 11º PASSO: OBSERVAÇÕES AJUSTADAS (k)
# =============================================================================
print("\n" + "=" * 70)
print("11º PASSO: OBSERVAÇÕES AJUSTADAS")
print("-" * 40)

L_ajustado = Lb + V

print("Lₐ = L_b + V =")
for i, (orig, ajust) in enumerate(zip(Lb.flatten(), L_ajustado.flatten()), 1):
    print(f"l{i}ᵃ = {orig:.2f} + {V[i-1,0]:.6f} = {ajust:.6f}")

# =============================================================================
# 12º PASSO: VARIÂNCIA A POSTERIORI (h)
# =============================================================================
print("\n" + "=" * 70)
print("12º PASSO: VARIÂNCIA A POSTERIORI")
print("-" * 40)

# Graus de liberdade
gl = n - 2  # 6 observações - 2 parâmetros

# Cálculo da variância a posteriori
sigma0_quadrado = (V.T @ P @ V) / gl

print(f"Graus de liberdade: {gl}")
print(f"Variância a posteriori (σ₀²) = {sigma0_quadrado[0,0]:.8f}")

# =============================================================================
# 13º PASSO: MATRIZ VARIÂNCIA-COVARIÂNCIA DOS PARÂMETROS
# =============================================================================
print("\n" + "=" * 70)
print("13º PASSO: MATRIZ VARIÂNCIA-COVARIÂNCIA DOS PARÂMETROS")
print("-" * 40)

Sigma_X = sigma0_quadrado * np.linalg.inv(N)

print("Σ_X = σ₀² * N⁻¹ =")
print(Sigma_X)

print(f"\nDesvio padrão de x₁: {np.sqrt(Sigma_X[0,0]):.6f}")
print(f"Desvio padrão de x₂: {np.sqrt(Sigma_X[1,1]):.6f}")

# =============================================================================
# 14º PASSO: RESULTADO FINAL
# =============================================================================
print("\n" + "=" * 70)
print("RESULTADO FINAL")
print("=" * 70)

print(f"UMA UNIDADE DA ESCALA A CORRESPONDE A {X_ajustado[1,0]:.6f} UNIDADES DA ESCALA B")
print(f"COM PRECISÃO DE ±{np.sqrt(Sigma_X[1,1]):.6f} UNIDADES")

print("\n" + "=" * 70)
print("RESUMO DOS PARÂMETROS AJUSTADOS")
print("-" * 40)
print(f"x₁ (valor de B para A=7): {X_ajustado[0,0]:.6f} ± {np.sqrt(Sigma_X[0,0]):.6f}")
print(f"x₂ (fator de conversão):  {X_ajustado[1,0]:.6f} ± {np.sqrt(Sigma_X[1,1]):.6f}")

# =============================================================================
# TABELA COMPARATIVA
# =============================================================================
print("\n" + "=" * 70)
print("TABELA COMPARATIVA: OBSERVAÇÕES vs AJUSTADAS")
print("=" * 70)

df = pd.DataFrame({
    'Escala A': A_values,
    'Escala B (observado)': B_values,
    'Resíduo (V)': V.flatten(),
    'Escala B (ajustado)': L_ajustado.flatten(),
    'Diferença': (L_ajustado - Lb).flatten()
})

print(df.to_string(index=False, float_format='%.6f'))
