'''
3) Um engenheiro cartógrafo estava realizando o levantamento das divisas de uma propriedade urbana, somente com uma estação total a laser e uma trena, foi então que se deparou com um problema, ele
precisava determinar um ponto, mas sua visão estava obstruída.

Sendo assim ele se lembrou de uma técnica chamada interseção linear, onde ele poderia medir dois pontos notáveis (A e B) um em cada face do muro e medir as distâncias desses pontos para o ponto de
interesse P, para que em escritório ele determine as coordenadas do ponto P e suas respectivas precisões. Para tanto, o engenheiro mediu dois pontos que eram visíveis (A e B) e que possibilitavam
medida ao ponto P. Além disso, ele mediu com a trena, as distâncias de A e B para o ponto P.

Ponto A → X=100m, Y=100m, desviopadrao_x_A=0.05m, desviopadrao_y_A=0.03m
Ponto B → X=110m, Y=105m, desviopadrao_x_B=0.03m, desviopadrao_y_B=0.04m

Direção A-P → distancia_AP=12.50m, desviopadrao_distancia_AP=0.03m
Direção B-P → distancia_AP=8.50m, desviopadrao_distancia_AP=0.03m

Distância entre A-P → distancia_AP = 12.50m
Distância entre B-P → distancia_BP = 8.50m

Com os seus conhecimentos em geometria, e em propagação de erros, calcule as coordenadas do ponto P e suas respectivas precisões.

Formulário:
a² = b² + c² - 2b*c*cosÂ
b² = a² + c² - 2a*c*cosB̂
c² = a² + b² - 2a*b*cosĈ

MMF (Modelo Matemático Funcional):
Xp = X? + D? * sin Az?
Yp = Y? + D? * cos Az?

OBS PELO GRAFICO:
Xp teria que ser entre 104m a 106m (tem que ser mais proximo do 104m)
Yp deveria ser entre 110m e 112m (mais perto do 112m)
'''

import numpy as np
import math

# Dados dos pontos A e B
A = {'X': 100.0, 'Y': 100.0, 'std_X': 0.05, 'std_Y': 0.03}
B = {'X': 110.0, 'Y': 105.0, 'std_X': 0.03, 'std_Y': 0.04}

# Distâncias medidas e seus desvios padrão
d_AP = 12.50
d_BP = 8.50
std_d_AP = 0.03
std_d_BP = 0.03

def calcular_coordenadas_P():
    """
    Calcula as coordenadas do ponto P usando interseção linear.
    Retorna (Xp, Yp)
    """
    # Calcula a distância entre A e B
    delta_X = B['X'] - A['X']
    delta_Y = B['Y'] - A['Y']
    d_AB = math.sqrt(delta_X**2 + delta_Y**2)
    
    # Verifica se as distâncias são consistentes
    if d_AP + d_BP < d_AB or abs(d_AP - d_BP) > d_AB:
        raise ValueError("As distâncias fornecidas são inconsistentes com a geometria do problema")
    
    # Calcula o ângulo em A usando a lei dos cossenos
    cos_theta_A = (d_AP**2 + d_AB**2 - d_BP**2) / (2 * d_AP * d_AB)
    theta_A = math.acos(cos_theta_A)
    
    # Azimute de A para B (cuidado com a definição - aqui usamos atan2(delta_X, delta_Y))
    az_AB = math.atan2(delta_X, delta_Y)
    
    # Azimute de A para P
    az_AP = az_AB - theta_A
    
    # Calcula as coordenadas de P a partir de A
    Xp_A = A['X'] + d_AP * math.sin(az_AP)
    Yp_A = A['Y'] + d_AP * math.cos(az_AP)
    
    # Agora calculando a partir de B para verificação
    # Ângulo em B
    cos_theta_B = (d_BP**2 + d_AB**2 - d_AP**2) / (2 * d_BP * d_AB)
    theta_B = math.acos(cos_theta_B)
    
    # Azimute de B para A
    az_BA = math.atan2(-delta_X, -delta_Y)
    
    # Azimute de B para P
    az_BP = az_BA + theta_B
    
    # Calcula as coordenadas de P a partir de B
    Xp_B = B['X'] + d_BP * math.sin(az_BP)
    Yp_B = B['Y'] + d_BP * math.cos(az_BP)
    
    # Média das duas soluções (para maior precisão)
    Xp = (Xp_A + Xp_B) / 2
    Yp = (Yp_A + Yp_B) / 2
    
    return Xp, Yp

def propagacao_erros(Xp, Yp):
    """
    Calcula as precisões das coordenadas de P usando propagação de erros.
    Retorna (std_Xp, std_Yp)
    """
    # Derivadas parciais aproximadas usando diferenças finitas
    delta = 0.0001
    
    # Variação em XA
    A_plus = {'X': A['X'] + delta, 'Y': A['Y'], 'std_X': A['std_X'], 'std_Y': A['std_Y']}
    Xp_plus, Yp_plus = calcular_coordenadas_P_aux(A_plus, B, d_AP, d_BP)
    dXp_dXA = (Xp_plus - Xp) / delta
    dYp_dXA = (Yp_plus - Yp) / delta
    
    # Variação em YA
    A_plus = {'X': A['X'], 'Y': A['Y'] + delta, 'std_X': A['std_X'], 'std_Y': A['std_Y']}
    Xp_plus, Yp_plus = calcular_coordenadas_P_aux(A_plus, B, d_AP, d_BP)
    dXp_dYA = (Xp_plus - Xp) / delta
    dYp_dYA = (Yp_plus - Yp) / delta
    
    # Variação em XB
    B_plus = {'X': B['X'] + delta, 'Y': B['Y'], 'std_X': B['std_X'], 'std_Y': B['std_Y']}
    Xp_plus, Yp_plus = calcular_coordenadas_P_aux(A, B_plus, d_AP, d_BP)
    dXp_dXB = (Xp_plus - Xp) / delta
    dYp_dXB = (Yp_plus - Yp) / delta
    
    # Variação em YB
    B_plus = {'X': B['X'], 'Y': B['Y'] + delta, 'std_X': B['std_X'], 'std_Y': B['std_Y']}
    Xp_plus, Yp_plus = calcular_coordenadas_P_aux(A, B_plus, d_AP, d_BP)
    dXp_dYB = (Xp_plus - Xp) / delta
    dYp_dYB = (Yp_plus - Yp) / delta
    
    # Variação em dAP
    Xp_plus, Yp_plus = calcular_coordenadas_P_aux(A, B, d_AP + delta, d_BP)
    dXp_dAP = (Xp_plus - Xp) / delta
    dYp_dAP = (Yp_plus - Yp) / delta
    
    # Variação em dBP
    Xp_plus, Yp_plus = calcular_coordenadas_P_aux(A, B, d_AP, d_BP + delta)
    dXp_dBP = (Xp_plus - Xp) / delta
    dYp_dBP = (Yp_plus - Yp) / delta
    
    # Propagação de erros
    var_Xp = (dXp_dXA * A['std_X'])**2 + (dXp_dYA * A['std_Y'])**2 + \
             (dXp_dXB * B['std_X'])**2 + (dXp_dYB * B['std_Y'])**2 + \
             (dXp_dAP * std_d_AP)**2 + (dXp_dBP * std_d_BP)**2
    
    var_Yp = (dYp_dXA * A['std_X'])**2 + (dYp_dYA * A['std_Y'])**2 + \
             (dYp_dXB * B['std_X'])**2 + (dYp_dYB * B['std_Y'])**2 + \
             (dYp_dAP * std_d_AP)**2 + (dYp_dBP * std_d_BP)**2
    
    std_Xp = math.sqrt(var_Xp)
    std_Yp = math.sqrt(var_Yp)
    
    return std_Xp, std_Yp

def calcular_coordenadas_P_aux(A, B, d_AP, d_BP):
    """Função auxiliar para cálculo das coordenadas com parâmetros modificados"""
    delta_X = B['X'] - A['X']
    delta_Y = B['Y'] - A['Y']
    d_AB = math.sqrt(delta_X**2 + delta_Y**2)
    
    # Ângulo em A
    cos_theta_A = (d_AP**2 + d_AB**2 - d_BP**2) / (2 * d_AP * d_AB)
    theta_A = math.acos(cos_theta_A)
    az_AB = math.atan2(delta_X, delta_Y)
    az_AP = az_AB - theta_A
    Xp_A = A['X'] + d_AP * math.sin(az_AP)
    Yp_A = A['Y'] + d_AP * math.cos(az_AP)
    
    # Ângulo em B
    cos_theta_B = (d_BP**2 + d_AB**2 - d_AP**2) / (2 * d_BP * d_AB)
    theta_B = math.acos(cos_theta_B)
    az_BA = math.atan2(-delta_X, -delta_Y)
    az_BP = az_BA + theta_B
    Xp_B = B['X'] + d_BP * math.sin(az_BP)
    Yp_B = B['Y'] + d_BP * math.cos(az_BP)
    
    return (Xp_A + Xp_B)/2, (Yp_A + Yp_B)/2

# Cálculo das coordenadas de P
Xp, Yp = calcular_coordenadas_P()

# Cálculo das precisões
std_Xp, std_Yp = propagacao_erros(Xp, Yp)

# Resultados
print("Solução para o problema de interseção linear:")
print(f"Coordenadas do ponto P: X = {Xp:.3f} m, Y = {Yp:.3f} m")
print(f"Precisões: σ_X = {std_Xp:.3f} m, σ_Y = {std_Yp:.3f} m")
