% Universidade Federal do Paraná
% Ajustamento I 
% Glória Maria Deitos Gomes da Silva
% 06.Junho.2025

clc; clear all; format long g; close all; tic

% Exercício: No georreferenciamento de imóveis rurais deve-se implantar
% uma base, denominadavértice C1, para ser utilizada como apoio básico
% dentro do levantamento da propriedade. As coordenadas deste vértice devem
% ser estimadas a partir de pelo menos dois pontos do Sistema Geodésico
% Brasileiro (SGB). A partir dos dados a seguir estime as coordenadas do
% vértice C1.

% Dados:

% Coordenadas dos pontos do SBG:
E1 = 645545.053;
N1 = 8624964.644;
E2 = 645945.053;
N2 = 8625264.644;
E3 = 646445.053;
N3 = 8624864.644;

% Distâncias:
% obs: os desvio-padrão(dp) é +- o valor, ou seja, módulo
DeltaE1C1 = 558.856;
dpE1C1 = 0.031;
DeltaN1C1 = -1376.407;
dpN1C1 = 0.025;

DeltaE2C1 = 158.736;
dpE2C1 = 0.069;
DeltaN2C1 = -1676.925;
dpN2C1 = 0.047;

DeltaE3C1 = -341.368;
dpE3C1 = 0.038;
DeltaN3C1 = -1276.806;
dpN3C1 = 0.029;

% Número de observações (2 por ponto: ΔE e ΔN)
n = 6;

% Número de incógnitas (coordenadas Este e Norte do ponto C1)
u = 2;

% Grau de liberdade
f = n - u;

% Montagem do vetor de observações (L)
L = [E1 + DeltaE1C1;
     N1 + DeltaN1C1;
     E2 + DeltaE2C1;
     N2 + DeltaN2C1;
     E3 + DeltaE3C1;
     N3 + DeltaN3C1];

% Matriz dos coeficientes (A)
A = [1 0;
     0 1;
     1 0;
     0 1;
     1 0;
     0 1];

% Matriz dos pesos (P) - inverso do quadrado dos desvios padrão
P = diag([1/dpE1C1^2, 1/dpN1C1^2, 1/dpE2C1^2, 1/dpN2C1^2, 1/dpE3C1^2, 1/dpN3C1^2]);

% Solução por mínimos quadrados: X̂ = (AᵗPA)^(-1) * AᵗPL
Nmat = A' * P * A;      % Matriz normal
U = A' * P * L;         % Vetor de termos independentes
X_hat = Nmat \ U;       % Estimativa das coordenadas de C1

% Coordenadas ajustadas do ponto C1
Este_C1 = X_hat(1);
Norte_C1 = X_hat(2);

% Cálculo das incertezas (variância-covariância)
v = A * X_hat - L;              % Vetor dos resíduos
sigma0_2 = (v' * P * v) / f;    % Variância a posteriori
Qx = inv(Nmat);                 % Matriz das variâncias das incógnitas
Cx = sigma0_2 * Qx;             % Matriz de covariância das incógnitas

% Desvio-padrão das coordenadas estimadas
dp_E = sqrt(Cx(1,1));
dp_N = sqrt(Cx(2,2));

% Resultados
fprintf('\nCoordenadas estimadas do vértice C1:\n');
fprintf('Este:  %.3f m ± %.3f m\n', Este_C1, dp_E);
fprintf('Norte: %.3f m ± %.3f m\n', Norte_C1, dp_N);

% Tempo de execução
toc

