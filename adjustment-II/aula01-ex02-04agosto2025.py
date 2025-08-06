"""
O conjunto de dados, mostrados abaixo, representa a porção em segundos de arco de 50 medidas de uma direção.

Calcular a amplitude, média média, e mediana, a moda, desvio padrão da amostra, desvio padrão da média, a variância e construir um histrograma de classes.
"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats

# Dados fornecidos
data = np.array([
    [34.2, 33.6, 35.2, 30.1, 38.4, 34.0, 30.2, 34.1, 37.7, 36.4],
    [37.9, 33.0, 33.5, 35.9, 35.9, 32.4, 39.3, 32.2, 32.8, 36.3],
    [35.3, 32.6, 34.1, 35.6, 33.7, 39.2, 35.1, 33.4, 34.9, 32.6],
    [36.7, 34.8, 36.4, 33.7, 36.1, 34.8, 36.7, 30.0, 35.3, 34.4],
    [33.7, 34.1, 37.8, 38.7, 33.6, 32.6, 34.7, 34.7, 36.8, 31.8],
])

# Amplitude (a amplitude é a diferença entre o valor máximo e mínimo)
amplitude = np.max(data) - np.min(data)

# Média (a média é a soma dos valores dividida pelo número de elementos)
media = np.mean(data)

# Mediana (a mediana é o valor central quando os dados estão ordenados)
mediana = np.median(data)

# Moda (a moda é o valor que aparece com mais frequência)
moda = stats.mode(data, axis=None).mode

# Desvio padrão da amostra (o desvio padrão da amostra mede a dispersão dos dados em relação à média)
desvio_padrao_amostra = np.std(data) #ddof=1

# Desvio padrão da média (o desvio padrão da média é o desvio padrão da amostra dividido pela raiz quadrada do número de elementos)
desvio_padrao_media = desvio_padrao_amostra / np.sqrt(data.size)

# Variância (a variância é o quadrado do desvio padrão)
variancia = np.var(data) #ddof=1

# Histograma
plt.hist(data.flatten(), bins=10, edgecolor='#d991ba', color='lightpink', alpha=0.7)
plt.title('Histograma da imagem - 8bits')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.75, color="#c0d8fc")
plt.grid(axis='x', alpha=0.75, color='#c9e7c5')
plt.axvline(media, color="#dd1b1b", linestyle=':', linewidth=3, label='Média')
plt.axvline(mediana, color="#93d340", linestyle=':', linewidth=3, label='Mediana')
plt.axvline(moda, color="#6195E4", linestyle=':', linewidth=3, label='Moda')
plt.legend()
plt.show()

# Exibindo os resultados
print(f'Amplitude: {amplitude:.2f}') # Esse ":.2f" formata o número para duas casas decimais
print(f'Média: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Moda: {moda:.2f}')
print(f'Desvio Padrão da Amostra: {desvio_padrao_amostra:.2f}')
print(f'Desvio Padrão da Média: {desvio_padrao_media:.2f}')
print(f'Variância: {variancia:.2f}')
