"""
Este script realiza a análise estatística de um conjunto de dados representando números digitais (ND) em uma imagem de 7x10 pixels de 8 bits.

Calcular a amplitude, média, a mediana, a moda, desvio padrão da amostra, desvio padrão da média, a variância e construir um histograma de classes.
"""

import numpy as np
import matplotlib.pyplot as plt # precisa usar essa biblioteca para construir o histograma
from scipy import stats # precisa usar essa biblioteca para calcular a moda

# Dados fornecidos
data = np.array([
    [12, 123, 252, 13, 123, 70, 70, 75, 17, 77],
    [1, 17, 123, 13, 0, 5, 23, 17, 17, 75],
    [17, 245, 75, 13, 255, 73, 33, 3, 17, 73],
    [123, 245, 5, 123, 137, 255, 255, 123, 255, 77],
    [243, 3, 27, 27, 5, 123, 255, 77, 123, 252],
    [243, 123, 83, 77, 250, 250, 73, 123, 77, 17],
    [93, 37, 37, 37, 145, 250, 3, 3, 17, 0],
])

# Amplitude (a amplitude é a diferença entre o valor máximo e mínimo)
amplitude = np.max(data) - np.min(data)

# Média (a média é a soma dos valores dividida pelo número de elementos)
media = np.mean(data)

# Mediana (a mediana é o valor central quando os dados estão ordenados)
mediana = np.median(data)

# Moda (a moda é o valor que aparece com mais frequência)
moda = stats.mode(data, axis=None).mode
"""
Obs.: O parâmetro axis=None é utilizado para considerar todos os elementos do array como uma única sequência, ignorando a estrutura bidimensional,
garantindo que a moda seja calculada sobre todos os valores.
"""

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
print(f'Amplitude: {amplitude}')
print(f'Média: {media}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
print(f'Desvio Padrão da Amostra: {desvio_padrao_amostra}')
print(f'Desvio Padrão da Média: {desvio_padrao_media}')
print(f'Variância: {variancia}')
