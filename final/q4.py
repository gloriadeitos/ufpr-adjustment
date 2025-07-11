'''
4) Um modelo de quase geoide (QG) gravimétrico foi calculado para certa região. Objetivando referencia-lo ao Datum Vertical Brasileiro em Imbituba (DVBI), um conjunto de pontos RN/GPS do Sistema Geodésico Brasileiro
foram utilizados. Nestes pontos foram calculadas as anomalias de altura referenciadas ao DVBI e coletadas as anomalias de altura do modelo de QG. Com base nestes dados realize o ajustamento paramétrico linear da
transformação utilizando o modelo matemático funcional fornecido e faça as análises.

Ponto | Anomalia de altura vinculada ao DVBI (m) | Anomalia de altura do modelo de QG (m)
1
2
3
4
5

MMF: Δζ = a₀ + a₁

-------------------------------------------------------------------------
Método paramétrico → La = F(Xa)
Os valores observados ajustados podem ser expressos
explicitamente como uma função dos parâmetros ajustados.
-------------------------------------------------------------------------
Método dos correlatos → F(La) = 0
Os valores observados ajustados devem satisfazer determinadas
condições (erro de fechamento = zero).
-------------------------------------------------------------------------
Método combinado → F(La, Xa) = 0
Os valores observados ajustados e os parâmetros ajustados são
ligados por função não explícita (não se consegue separá-los).
-------------------------------------------------------------------------

Apresente:

a) Vetor das observações
b) Matriz dos pesos
c) Matriz design
d) Vetor dos parâmetros ajustados
e) Vetor dos resíduos e análise do mesmo
f) Fator de variância da unidade de peso a posteriori com o teste do Qui-quadrado e sua análise
g) Valor de gravidade nas estações e suas precisões
'''
