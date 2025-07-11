'''
2) Um engenheiro cartógrafo, durante uma campanha de levantamento geodésico, mediu cinco vezes o ângulo entre dois marcos utilizando uma estação total de alta precisão, em condições normais de operação.
Os valores obtidos nas medições foram registrados na tabela a seguir:

Observação 1 → 75° 14' 32,4"
Observação 2 → 75° 14' 33,1"
Observação 3 → 75° 14' 32,9"
Observação 4 → 75° 14' 33,5"
Observação 5 → 75° 14' 31,8"

Estime o intervalo de confiança de 99% para média e variância.
'''
import numpy as np
import scipy.stats as stats

# Dados fornecidos
observacoes_sexagesimais = [
    "75° 14' 32,4\"",
    "75° 14' 33,1\"",
    "75° 14' 32,9\"",
    "75° 14' 33,5\"",
    "75° 14' 31,8\""
]

def converter_para_segundos(angulo):
    # Remove as aspas e separa os componentes
    partes = angulo.replace('"', '').split()
    graus = float(partes[0].replace('°', ''))
    minutos = float(partes[1].replace("'", ''))
    segundos = float(partes[2].replace(",", "."))
    return graus * 3600 + minutos * 60 + segundos

# Convertendo todas as observações para segundos
observacoes_segundos = np.array([converter_para_segundos(obs) for obs in observacoes_sexagesimais])

# Cálculos estatísticos
n = len(observacoes_segundos)
media = np.mean(observacoes_segundos)
desvio_padrao = np.std(observacoes_segundos, ddof=1)  # ddof=1 para amostra
variancia = desvio_padrao**2

# Intervalo de confiança para a média (99%)
t_valor = stats.t.ppf(0.995, df=n-1)  # 99% bilateral
erro_padrao_media = desvio_padrao / np.sqrt(n)
ic_media_inf = media - t_valor * erro_padrao_media
ic_media_sup = media + t_valor * erro_padrao_media

# Intervalo de confiança para a variância (99%)
qui_quadrado_inf = stats.chi2.ppf(0.995, df=n-1)
qui_quadrado_sup = stats.chi2.ppf(0.005, df=n-1)
ic_var_inf = (n-1) * variancia / qui_quadrado_inf
ic_var_sup = (n-1) * variancia / qui_quadrado_sup

# Função para converter segundos de volta para formato sexagesimal
def segundos_para_sexagesimal(segundos):
    graus = int(segundos // 3600)
    resto = segundos % 3600
    minutos = int(resto // 60)
    segundos = resto % 60
    return f"{graus}° {minutos}' {segundos:.1f}\""

# Resultados
print("Dados originais convertidos para segundos:", observacoes_segundos)
print(f"\nMédia: {media:.4f} segundos ({segundos_para_sexagesimal(media)})")
print(f"Desvio padrão: {desvio_padrao:.4f} segundos")
print(f"Variância: {variancia:.4f} segundos²")

print("\nIntervalo de Confiança 99% para a Média:")
print(f"({ic_media_inf:.4f}, {ic_media_sup:.4f}) segundos")
print(f"({segundos_para_sexagesimal(ic_media_inf)}, {segundos_para_sexagesimal(ic_media_sup)})")

print("\nIntervalo de Confiança 99% para a Variância:")
print(f"({ic_var_inf:.4f}, {ic_var_sup:.4f}) segundos²")
