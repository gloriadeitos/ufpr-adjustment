"""
MÉTODO DOS MÍNIMOS QUADRADOS

Sistema de equações:
- Consistente: quando existe PELO MENOS UMA solução que satisfaz todas as equações do modelo
- Incosistente: quando NÃO POSSUI NENHUMA solução
- Determinado: quando existe APENAS UMA solução que satisfaz todas as equações do modelo
- Indeterminado: quando existem INFINITAS soluções que satisfazem todas as equações do modelo

Dado o sistema de equações de observação:

{ x + y = 3.1
{ x - y = 0.9
{ 2z + w = 4.9
{ z - w = 4.1
{ x + z - w = 3.9
{ x - y + z - w = 3.1
*é um sistema, então tudo é no mesmo {

{ x + y = 3.1
{ x + z = 3.9
{ 2z = 4.9
{ x - y + z = 3.1
{ x - y = 0.9
{ z = 4.1
*é um sistema, então tudo é no mesmo {

{ a + b + c + d = 15.25
{ -a -b -c = 7.35
{ 3a - 4b + 8c - d = 8.75
{ b - c - d = 3.17
*é um sistema, então tudo é no mesmo {

a) Identificar se os sistemas de equações são consistentes e determinados.

b) Se os sistemas são identificados por consistentes e determinados, encontrar a solução que
melhor representa o sistema utilizando o princípio de mínimos quadrados.
"""

import numpy as np

# Matriz do sistema de equações
A = np.array([[1, 1, 0, 0],
      [1, -1, 0, 0],
      [0, 0, 2, 1],
      [0, 0, 1, -1],
      [1, 0, 1, -1],
      [1, -1, 1, -1]
    ])

# Matriz das observações
L = np.array([[3.1],
      [0.9],
      [4.9],
      [4.1],
      [3.9],
      [3.1]
    ])

# RESPOSTA, Matriz das incógnitas
"""
X = (A_transposta * A)^-1 * (A_transposta * L)
"""
X = np.linalg.inv(A.T @ A) @ A.T @ L

# Resposta com 4 casas decimais
print("X =")
for valor in X:
    print(f"[{valor[0]:.4f}]")
print("\n Ou seja: \n X = \n [x] \n [y] \n [z] \n [w]")
