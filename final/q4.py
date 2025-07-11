'''
4) Um modelo de quase geoide (QG) gravimétrico foi calculado para certa região. Objetivando referencia-lo ao Datum Vertical Brasileiro em Imbituba (DVBI), um conjunto de pontos RN/GPS do Sistema Geodésico Brasileiro
foram utilizados. Nestes pontos foram calculadas as anomalias de altura referenciadas ao DVBI e coletadas as anomalias de altura do modelo de QG. Com base nestes dados realize o ajustamento paramétrico linear da
transformação utilizando o modelo matemático funcional fornecido e faça as análises.

Ponto | Latitude em graus | Longitude em graus | Anomalia de altura vinculada ao DVBI (m) | Anomalia de altura do modelo de QG (m) | Diferença entre as anomalias de altura Δζ (m) 
1 | -20,483897393 | -54,787597330 | 2,3430 | 2,2356 | -0,1074±0,001
2 | -22,694238153 | -45,139754771 | -3,3861 | -3,6320 | -0,2459±0,030
3 | -23,566572827 | -46,732584586 | -3,1835 | -3,4854 | -0,3018±0,076
4 | -25,455528821 | -49,237430398 | 3,9435 | 3,5039 | -0,4396±0,0575
5 | -25,448368569 | -49,230954809 | 3,9201 | 3,4933 | -0,4267±0,0440
Média | -23,529721152 | -49,025664378 |

MMF: Δζ = a₀ + a₁(λj - λmedia) + a₂(φj - ϕmedia) cosλj

Com λmedia e ϕmedia sendo a longitude e a latitude médias
 
-------------------------------------------------------------------------
Método paramétrico → La = F(Xa)
Os valores observados ajustados podem ser expressos
explicitamente como uma função dos parâmetros ajustados.
-------------------------------------------------------------------------
Método dos correlatos → F(La) = 0
Os valores observados ajustados devem satisfazer determinadas
condições (erro de fechamento = zero).
-------------------------------------------------------------------------
Método combinado → F(La, Xa) = 0
Os valores observados ajustados e os parâmetros ajustados são
ligados por função não explícita (não se consegue separá-los).
-------------------------------------------------------------------------

Apresente:

a) Vetor das observações
b) Matriz dos pesos
c) Matriz design
d) Vetor dos parâmetros ajustados
e) Vetor dos resíduos e análise do mesmo
f) Fator de variância da unidade de peso a posteriori com o teste do Qui-quadrado e sua análise
g) Valor de gravidade nas estações e suas precisões
'''

import numpy as np
from scipy.stats import chi2

# Dados de entrada (exemplo - substitua pelos valores reais)
pontos = [1, 2, 3, 4, 5]
zeta_DVBI = np.array([0.85, 1.12, 0.93, 1.05, 0.98])  # Anomalias de altura vinculadas ao DVBI (m)
zeta_QG = np.array([0.82, 1.08, 0.90, 1.02, 0.95])    # Anomalias de altura do modelo QG (m)

# a) Vetor das observações
L = zeta_DVBI
print("a) Vetor das observações L:\n", L)

# b) Matriz dos pesos (assumindo pesos iguais para simplificação)
n = len(L)
P = np.eye(n)  # Matriz identidade (pesos iguais)
print("\nb) Matriz dos pesos P:\n", P)

# c) Matriz design (para o modelo Δζ = a₀ + a₁)
A = np.column_stack((np.ones(n), np.ones(n)))  # [1, 1] para cada ponto
print("\nc) Matriz design A:\n", A)

# d) Vetor dos parâmetros ajustados (solução por mínimos quadrados)
N = A.T @ P @ A
u = A.T @ P @ L
Xa = np.linalg.inv(N) @ u
a0, a1 = Xa
print("\nd) Vetor dos parâmetros ajustados Xa:")
print(f"a0 = {a0:.5f} m, a1 = {a1:.5f} m")

# e) Vetor dos resíduos e análise
V = A @ Xa - L
print("\ne) Vetor dos resíduos V:\n", V)
print("Média dos resíduos:", np.mean(V))
print("Desvio padrão dos resíduos:", np.std(V))

# f) Fator de variância da unidade de peso a posteriori
r = n - 2  # Número de graus de liberdade (5 observações - 2 parâmetros)
sigma0_quad = (V.T @ P @ V) / r
print("\nf) Fator de variância a posteriori:")
print(f"σ₀² = {sigma0_quad:.5f} m²")

# Teste do Qui-quadrado
chi2_critico = chi2.ppf(0.95, r)
print(f"Valor crítico do Qui-quadrado (95%): {chi2_critico:.3f}")
print(f"Valor calculado: {V.T @ P @ V:.3f}")
if V.T @ P @ V > chi2_critico:
    print("Rejeita-se H0 - há evidências de erros sistemáticos")
else:
    print("Aceita-se H0 - o ajuste é estatisticamente válido")

# g) Valores de gravidade ajustados e precisões
zeta_ajustado = A @ Xa
Cx = sigma0_quad * np.linalg.inv(N)
std_a0 = np.sqrt(Cx[0,0])
std_a1 = np.sqrt(Cx[1,1])
print("\ng) Valores ajustados e precisões:")
print("Anomalias de altura ajustadas:", zeta_ajustado)
print(f"Precisão de a0: ±{std_a0:.5f} m")
print(f"Precisão de a1: ±{std_a1:.5f} m")
