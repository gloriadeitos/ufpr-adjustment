"""
Os ângulos apresentados na tabela abaixo, com observações e pesos, foram medidos
com uma estação total. Use MMQ para ajustá-los.

Ângulos | Observações | Peso
  A1    | 44° 50' 44" |  1
  A2    | 46° 10' 25" |  3
  A3    | 45° 55' 12" |  3
  A4    | 43° 04' 03" |  3
  A5    | 48° 32' 45" |  3
  A6    | 42° 27' 42" |  1


  B----------C
  |          |
  |          |
  |          |
  A          D

  a2 a3         a4 a5


  a1               a6


TRIANGULO 1 = a1 a2
TRIANGULO 2 = a3 a4
TRIANGULO 3 = a5 a6

Determinar os ângulos A, B, C e D

"""

import numpy as np
from astropy.coordinates import Angle

# Ângulos dos triângulos, com os pesos
"""
Medições mais precisas → maior peso
Medições menos precisas → menor peso
"""
angulos = {
    "a1": Angle('44d50m44s'), "p1": 1,
    "a2": Angle('46d10m25s'), "p2": 3,
    "a3": Angle('45d55m12s'), "p3": 3,
    "a4": Angle('43d04m03s'), "p4": 3,
    "a5": Angle('48d32m45s'), "p5": 3,
    "a6": Angle('42d27m42s'), "p6": 1
}

# Erro fechamento angular (w)
"""
TRIANGULO 1 (ABC)
a1 + a2 + a3 + a4 = 180° → Se NÃO houvesse erro de fechamento
(a1 + a2 + a3 + a40) -180° → Assim teremos o valor SEM o erro

TRIANGULO 2 (BCD)
(a3 + a4 + a5 + a6) -180° → Valor SEM o erro
"""
w1 = ( angulos["a1"] + angulos["a2"] + angulos["a3"] + angulos["a4"] ) - Angle('180d')
print ('Erro de fechamento angular do triângulo 1 (ABC) = ', w1, '\n')

w2 = ( angulos["a3"] + angulos["a4"] + angulos["a5"] + angulos["a6"] ) - Angle('180d')
print ('Erro de fechamento angular do triângulo 1 (BCD) = ', w2, '\n')

# Matriz das derivadas parciais
