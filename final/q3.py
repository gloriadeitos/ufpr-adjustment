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

Com os seus conhecimentos em geometria, e em propagação de erros, calcule as coordenadas do ponto P e suas respectivas precisões.

Formulário:
a² = b² + c² - 2b*c*cosÂ
b² = a² + c² - 2a*c*cosB̂
c² = a² + b² - 2a*b*cosĈ

MMF (Modelo Matemático Funcional):
Xp = X? + D? * sin Az?
Yp = Y? + D? * cos Az?

'''
