# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:14:53 2025

@author: EllyonMagriMartins
"""

import sympy as sp
import numpy as np


Ni, Nj, Ei, Ej, Nn, Nm, En, Em = sp.symbols('Ni Nj Ei Ej Nn Nm En Em')   # Coordenadas dos pontos das retas

a1=(Nj-Ni)/(Ej-Ei)

a2= (Nm-Nn)/(Em-En)

b1= -1* (((Nj-Ni)/(Ej-Ei)) * Ei) + Ni

b2= -1* (((Nm-Nn)/(Em-En)) * En) + Nn

E = (b2-b1)/(a1-a2)

N = (a1*((b2-b1)/(a1-a2)))+b1


dE_dNi = sp.diff(E, Ni)
dE_dNj = sp.diff(E, Nj)
dE_dNn = sp.diff(E, Nn)
dE_dNm = sp.diff(E, Nm)
dE_dEi = sp.diff(E, Ei)
dE_dEj = sp.diff(E, Ej)
dE_dEn = sp.diff(E, En)
dE_dEm = sp.diff(E, Em)

dN_dNi = sp.diff(N, Ni)
dN_dNj = sp.diff(N, Nj)
dN_dNn = sp.diff(N, Nn)
dN_dNm = sp.diff(N, Nm)
dN_dEi = sp.diff(N, Ei)
dN_dEj = sp.diff(N, Ej)
dN_dEn = sp.diff(N, En)
dN_dEm = sp.diff(N, Em)


valores = {
   Ni: 7210100.734,
   Nj: 7210107.126,
   Nn: 7210019.871,
   Nm: 7210176.939,
   Ei: 423052.506,
   Ej: 422569.01,
   En: 423061.341,
   Em: 423053.391
   }


Ef= E.evalf(subs=valores)

Nf= N.evalf(subs=valores)


De= np.matrix([dE_dNi.evalf(subs=valores), dE_dNj.evalf(subs=valores), dE_dNn.evalf(subs=valores),
              dE_dNm.evalf(subs=valores),dE_dEi.evalf(subs=valores),dE_dEj.evalf(subs=valores),
              dE_dEn.evalf(subs=valores),dE_dEm.evalf(subs=valores)])

Dn= np.matrix([dN_dNi.evalf(subs=valores), dN_dNj.evalf(subs=valores), dN_dNn.evalf(subs=valores),
              dN_dNm.evalf(subs=valores),dN_dEi.evalf(subs=valores),dN_dEj.evalf(subs=valores),
              dN_dEn.evalf(subs=valores),dN_dEm.evalf(subs=valores)])

Sy=np.zeros([8,8])

ls=[0.004**2, 0.004**2, 0.004**2, 0.004**2, 0.004**2, 0.004**2, 0.006**2, 0.004**2]

np.fill_diagonal(Sy, ls)

Sy=np.matrix(Sy)

Se= De*Sy*De.T
Sn= Dn*Sy*Dn.T

print(f'Desvio padrão de E:{Ef} +- {np.sqrt(float(Se[0,0]))}')
print(f'Desvio padrão de N:{Nf} +- {np.sqrt(float(Sn[0,0]))}')


import matplotlib.pyplot as plt

# Coordenadas dos pontos
AFPR_M_131 = (423052.506, 7210100.734)
BKR_M_436  = (422569.01, 7210107.126)
E1065      = (423061.341, 7210019.871)
E25        = (423053.391, 7210176.939)

# Interseção calculada no seu script
V_intersec = (float(Ef), float(Nf))

# Criando a figura
plt.figure(figsize=(10, 8))

# Plotando os pontos e rotulando
plt.plot(*AFPR_M_131, 'o', label='AFPR-M-131')
plt.plot(*BKR_M_436, 'o', label='BKR-M-436')
plt.plot(*E1065, 'o', label='E1065')
plt.plot(*E25, 'o', label='E25')
plt.plot(*V_intersec, 'x', markersize=10, color='red', label='Vértice V (interseção)')

# Retas entre os pares de pontos
x1, y1 = zip(AFPR_M_131, BKR_M_436)
x2, y2 = zip(E1065, E25)

plt.plot(x1, y1, 'b--', label='Reta 1 (AFPR ↔ BKR)')
plt.plot(x2, y2, 'g--', label='Reta 2 (E1065 ↔ E25)')

# Estética do gráfico
plt.xlabel('Coordenada E (m)')
plt.ylabel('Coordenada N (m)')
plt.title('Interseção entre duas retas')
plt.grid(True)
plt.legend()
plt.axis('equal')

# Mostrar
plt.show()


