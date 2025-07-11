'''
1) Foram realizados voos fotogrametricos com diferentes alturas de voo, e mediu-se o tamanho do pixel (GSD) resultante nas imagens geradas.
O objetivo é avaliar se existe correlação entre altura de voo e o GSD. Os dados coletados são:

Ponto 1 → Altura=80, GSD(cm/pixel)=2,0
Ponto 2 → Altura=100, GSD(cm/pixel)=2,5
Ponto 3 → Altura=120, GSD(cm/pixel)=3,0
Ponto 4 → Altura=140, GSD(cm/pixel)=3,5
Ponto 5 → Altura=160, GSD(cm/pixel)=4,0

a) Calcule o coeficiente de correlação entre altura de voo e o GSD.

b) Analise o resultado baseado no gráfico: há correlação positiva, negativa ou nenhuma correlação? O resultado é coerente com o comportamento
esperado?
'''

import numpy as np
import matplotlib.pyplot as plt

# Dados fornecidos
alturas = np.array([80, 100, 120, 140, 160])  # Altura de voo em metros
gsd = np.array([2.0, 2.5, 3.0, 3.5, 4.0])     # GSD em cm/pixel

# a) Cálculo do coeficiente de correlação
correlacao = np.corrcoef(alturas, gsd)[0, 1]

print("a) Coeficiente de correlação:", round(correlacao, 4))

# b) Análise do resultado e plotagem do gráfico
plt.figure(figsize=(8, 5))
plt.scatter(alturas, gsd, color='blue', s=100)
plt.plot(alturas, gsd, 'r--')  # Linha conectando os pontos

# Configurações do gráfico
plt.title('Relação entre Altura de Voo e GSD', fontsize=14)
plt.xlabel('Altura de voo (m)', fontsize=12)
plt.ylabel('GSD (cm/pixel)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(80, 161, 20))
plt.yticks(np.arange(2.0, 4.1, 0.5))

# Análise textual
print("\nb) Análise:")
print("O gráfico mostra uma correlação positiva perfeita (r = 1.0) entre altura de voo e GSD.")
print("Isso significa que quanto maior a altura de voo, maior o tamanho do pixel no solo (GSD).")
print("Este resultado é totalmente coerente com o comportamento esperado em fotogrametria,")
print("pois a relação entre altura de voo e GSD é diretamente proporcional.")

plt.show()
