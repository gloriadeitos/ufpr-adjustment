# -*- coding: utf-8 -*-
"""
Created on Thu May 29 11:29:30 2025

@author: EllyonMagriMartins
"""

import sympy as sp
import numpy as np


Ni, Nj, Ei, Ej, Nn, Nm, En, Em, Hi, Hj, Hn, Hm, E, N, H = sp.symbols('Ni Nj Ei Ej Nn Nm En Em Hi Hj Hn Hm E N H')

t1= (E - Ei)/(Ej-Ei)
s1= (E - En)/(Em-En)

t2= (N - Ni)/(Nj-Ni)
s2= (N - Nn)/(Nm-Nn)

t3= (H - Hi)/(Hj-Hi)
s3= (H - Hn)/(Hm-Hn)

E1= Ei + t1*(Ej-Ei)- (En+s1*(Em-En))

N1= Ni + t2*(Nj-Ni)- (Nn+s2*(Nm-Nn))

H1= Hi + t3*(Hj-Hi)- (Hn+s3*(Hm-Hn))

dE1_dNi = sp.diff(E1, Ni)
dE1_dNj = sp.diff(E1, Nj)
dE1_dNn = sp.diff(E1, Nn)
dE1_dNm = sp.diff(E1, Nm)
dE1_dEi = sp.diff(E1, Ei)
dE1_dEj = sp.diff(E1, Ej)
dE1_dEn = sp.diff(E1, En)
dE1_dEm = sp.diff(E1, Em)
dE1_dHi = sp.diff(E1, Hi)
dE1_dHj = sp.diff(E1, Hj)
dE1_dHn = sp.diff(E1, Hn)
dE1_dHm = sp.diff(E1, Hm)
dE1_dEm = sp.diff(E1, Em)
dE1_dE = sp.diff(E1, E)
dE1_dN = sp.diff(E1, N)
dE1_dH = sp.diff(E1, H)

dN1_dNi = sp.diff(N1, Ni)
dN1_dNj = sp.diff(N1, Nj)
dN1_dNn = sp.diff(N1, Nn)
dN1_dNm = sp.diff(N1, Nm)
dN1_dEi = sp.diff(N1, Ei)
dN1_dEj = sp.diff(N1, Ej)
dN1_dEn = sp.diff(N1, En)
dN1_dEm = sp.diff(N1, Em)
dN1_dHi = sp.diff(N1, Hi)
dN1_dHj = sp.diff(N1, Hj)
dN1_dHn = sp.diff(N1, Hn)
dN1_dHm = sp.diff(N1, Hm)
dN1_dEm = sp.diff(N1, Em)
dN1_dE = sp.diff(N1, E)
dN1_dN = sp.diff(N1, N)
dN1_dH = sp.diff(N1, H)

dH1_dNi = sp.diff(H, Ni)
dH1_dNj = sp.diff(H, Nj)
dH1_dNn = sp.diff(H, Nn)
dH1_dNm = sp.diff(H, Nm)
dH1_dEi = sp.diff(H, Ei)
dH1_dEj = sp.diff(H, Ej)
dH1_dEn = sp.diff(H, En)
dH1_dEm = sp.diff(H, Em)
dH1_dHi = sp.diff(H1, Hi)
dH1_dHj = sp.diff(H1, Hj)
dH1_dHn = sp.diff(N1, Hn)
dH1_dHm = sp.diff(H1, Hm)
dH1_dEm = sp.diff(H1, Em)
dH1_dE = sp.diff(H1, E)
dH1_dN = sp.diff(H1, N)
dH1_dH = sp.diff(H1, H)


valores = {
   Ni: 1000,
   Nj: 2000,
   Nn: 1000,  
   Nm: 2000,
   Ei: 1000, 
   Ej: 2000, 
   En: 2000, 
   Em: 1000,
   Hi: 0,
   Hj:1000,
   Hn: 0,
   Hm:1000
   }


w= np.matrix([valores[Ni],valores[Nj],valores[Nn],valores[Nm],
              valores[Ei],valores[Ej],valores[En], valores[Em],
              valores[Hi],valores[Hj],valores[Hn], valores[Hm]])

A= np.matrix([[dE1_dE.evalf(subs=valores), dE1_dN.evalf(subs=valores), dE1_dH.evalf(subs=valores)],
              [dN1_dE.evalf(subs=valores), dN1_dN.evalf(subs=valores), dN1_dH.evalf(subs=valores)],
              [dH1_dE.evalf(subs=valores), dH1_dN.evalf(subs=valores), dH1_dH.evalf(subs=valores)]])

B= np.matrix([[dE1_dNi.evalf(subs=valores), dE1_dNj.evalf(subs=valores), dE1_dNn.evalf(subs=valores),dE1_dNm.evalf(subs=valores),
               dE1_dEi.evalf(subs=valores),dE1_dEj.evalf(subs=valores),dE1_dEn.evalf(subs=valores),dE1_dEm.evalf(subs=valores),
               dE1_dHi.evalf(subs=valores),dE1_dHj.evalf(subs=valores),dE1_dHn.evalf(subs=valores),dE1_dHm.evalf(subs=valores)]
              [dN1_dNi.evalf(subs=valores), dN1_dNj.evalf(subs=valores), dN1_dNn.evalf(subs=valores),dN1_dNm.evalf(subs=valores),
               dN1_dEi.evalf(subs=valores),dN1_dEj.evalf(subs=valores),dN1_dEn.evalf(subs=valores),dN1_dEm.evalf(subs=valores),
               dN1_dHi.evalf(subs=valores),dN1_dHj.evalf(subs=valores),dN1_dHn.evalf(subs=valores),dN1_dHm.evalf(subs=valores)]
              [dH1_dNi.evalf(subs=valores), dH1_dNj.evalf(subs=valores), dH1_dNn.evalf(subs=valores),dH1_dNm.evalf(subs=valores),
               dH1_dEi.evalf(subs=valores),dH1_dEj.evalf(subs=valores),dH1_dEn.evalf(subs=valores),dH1_dEm.evalf(subs=valores),
               dH1_dHi.evalf(subs=valores),dH1_dHj.evalf(subs=valores),dH1_dHn.evalf(subs=valores),dH1_dHm.evalf(subs=valores)]])


Sy=np.zeros([12,12])
np.fill_diagonal(Sy, (0.5**2))

W=np.matrix(Sy)
