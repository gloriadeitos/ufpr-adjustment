# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:14:53 2025

@author: EllyonMagriMartins
"""

import sympy as sp
import numpy as np


Ni, Nj, Ei, Ej, Nn, Nm, En, Em = sp.symbols('Ni Nj Ei Ej Nn Nm En Em')   # Coordenadas dos pontos das retas

a1=(Nj-Ni)/(Ej-Ei)

a2= (Nn-Nm)/(En-Em)

b1= Ni - ((Nj-Ni)/(Ej-Ei)) * Ei

b2= Nn - ((Nn-Nm)/(En-Em)) * En

E = (b2-b1)/(a1-a2)

N = a1*((b2-b1)/(a1-a2))+b1


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
   Ni: 1000,
   Nj: 2000,
   Nn: 1000,  
   Nm: 2000,
   Ei: 1000, 
   Ej: 2000, 
   En: 2000, 
   Em: 1000 
   }


Ef= E.evalf(subs=valores)

Nf= N.evalf(subs=valores)


De= np.matrix([dE_dNi.evalf(subs=valores), dE_dNj.evalf(subs=valores), dE_dNn.evalf(subs=valores),
              dE_dNm.evalf(subs=valores),dE_dEi.evalf(subs=valores),dE_dEi.evalf(subs=valores),
              dE_dEi.evalf(subs=valores),dE_dEi.evalf(subs=valores)])

Dn= np.matrix([dN_dNi.evalf(subs=valores), dN_dNj.evalf(subs=valores), dN_dNn.evalf(subs=valores),
              dN_dNm.evalf(subs=valores),dN_dEi.evalf(subs=valores),dN_dEi.evalf(subs=valores),
              dN_dEi.evalf(subs=valores),dN_dEi.evalf(subs=valores)])

Sy=np.zeros([8,8])
np.fill_diagonal(Sy, (0.5**2))
Sy=np.matrix(Sy)

Se= De*Sy*De.T
Sn= Dn*Sy*Dn.T

print(f'Desvio padrão de E:{Ef} +- {np.sqrt(float(Se[0,0]))}')
print(f'Desvio padrão de N:{Nf} +- {np.sqrt(float(Sn[0,0]))}')

