"""
AJUSTAMENTO II - MÉTODO DOS MÍNIMOS QUADRADOS

 ___________________
:' ,__________,  ':  `.
| '            `  |    `.
| |            |  |      `.
| |Ajustamento |  |        \
| |    II      |  |         ]
| |            |  |~~~~~~.  )
| `,__________,'  |\__O\_| ,'
|    _______      |     \.`
|<> [___=___](@)<>|    .'\
':________________/__.'   )
   (____________)        /
                        /
              _________/
  ___________/______
 /''''=========='(@)\___
 |[][][][][][][][][]|   \ _______
 |[][][][][][][][][]|    \__     \
 |[][][][][][][][][]|    |  \..  |
 \------------------/    | ( # ) |
                         |  '''  |
                         \_______/
"""

"""
   ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
    |         MÉTODO DOS         |.
    |      MÍNIMOS QUADRADOS     |.
    |                            |.
    |         A * X = L          |.
    |                            |.
    | A = Matriz do sistema de   |.
    |     equações               |.
    |                            |.
    | L = Matriz das observações |.
    |                            |.
    | X = Matriz das incógnitas  |.
    |                            |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.

"""

# ===================================================================================

# Método Paramétrico 
"""
Os valores observados ajustados podem ser expressos explicitamente como uma função
dos parâmetros ajustados.
"""

"""
La = F(Xa)

La = Vetor dos valores observados ajustados
F = Função de ajuste
Xa = Vetor dos parâmetros ajustados (um dos objetivos)
"""


"""
    __________________   __________________
.-/|                  \ /                  |\-.
||||                   |                   ||||
||||                   |       ~~*~~       ||||
||||                   |                   ||||
||||                   |                   ||||
||||    La = F(Xa)     |                   ||||
||||                   |     --==*==--     ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||__________________ | __________________||||
||/===================\|/===================\||
`--------------------~___~-------------------''

"""

# Método Paramétrico LINEAR
"""
Modelo matemático que relaciona as observações com os parâmetros e uma função linear
considerando variáveis com exponentes = 1

RESOLUÇAO DIRETA (uma única etapa para encontrar a solução)

NÃO é necessário uma aproximação inicial

Exemplo: Nivelamento, Poligonais
"""


# Método Paramétrico NÃO LINEAR

# ===================================================================================

# Método dos correlatos
"""
Os valores observados ajustados devem satisfazer determinadas condições
(erro de fechamento = zero)

F(La) = 0

F = Função de ajuste
La = Vetor dos valores observados ajustados
"""

# ===================================================================================

# Método combinado
"""
Os valores observados ajustados e os parâmetros ajustados são ligados por função não
explícita (não se consegue separa-los)

F(La, Xa) = 0

F = Função de ajuste
La = Vetor dos valores observados ajustados
Xa = Vetor dos parâmetros ajustados (um dos objetivos)
"""

# ===================================================================================

"""
     _________
    / ======= \
   / __________\
  | ___________ |
  | | -       | |
  | |         | |
  | |_________| |________________________
  \=____________/       fim....          )
  / ''''''''''' \                       /
 / ::::::::::::: \                  =D-'
(_________________)

UNIVERSIDADE FEDERAL DO PARANÁ
Engenharia Cartográfica e de Agrimensura

Glória Maria Deitos Gomes da Silva, 2025-2


ASCII from: https://www.asciiart.eu/

"""
