import numpy as np

# 1. DADOS DE EXEMPLO
# Vamos ajustar uma reta aos pontos: (1, 1), (2, 2), (3, 2)
x_dados = np.array([1, 2, 3])
y_dados = np.array([1, 2, 2])

# 2. CONSTRUIR a MATRIZ A e o VETOR L
# Queremos o modelo: y = a + b*x
# Logo, a matriz A tem uma coluna de 1s e uma coluna com os valores de x.
# Número de observações (m)
m = len(x_dados)

# Construir A como uma matriz de duas colunas: [1, x]
A = np.column_stack((np.ones(m), x_dados))
# A agora é:
# [[1. 1.]
#  [1. 2.]
#  [1. 3.]]

# L é simplesmente o vetor y dos resultados observados
L = y_dados

# 3. CALCULAR A SOLUÇÃO MMQ (X) usando a fórmula
# X = (A^T * A)^-1 * A^T * L

# Passo a passo para clareza:
A_transposta = A.T                    # Calcula A^T
ATA = np.dot(A_transposta, A)         # Calcula A^T * A
ATA_inversa = np.linalg.inv(ATA)      # Calcula (A^T * A)^-1
ATL = np.dot(A_transposta, L)         # Calcula A^T * L
X = np.dot(ATA_inversa, ATL)          # Calcula (A^T * A)^-1 * A^T * L

# 4. MOSTRAR O RESULTADO
print("Matriz A:")
print(A)
print("\nVetor L:")
print(L)
print("\nSolução MMQ - Vetor X [a, b]:")
print(X)

# Os coeficientes da reta são:
a = X[0]
b = X[1]
print(f"\nA equação da reta é: y = {a:.2f} + {b:.2f}*x")

# 5. (OPCIONAL) FORMA MAIS DIRETA E ROBUSTA
# NumPy tem uma função específica para resolver sistemas no sentido de MMQ: np.linalg.lstsq
# É a forma recomendada por ser numericamente mais estável, especialmente para problemas grandes.
X_lstsq, residuos, rank, s = np.linalg.lstsq(A, L, rcond=None)
print(f"\nSolução usando np.linalg.lstsq: {X_lstsq}")