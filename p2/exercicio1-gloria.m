% glória fez

% GA106 - Ajustamento I - Exercício 1 - Intersecção à Vante
% Cálculo das coordenadas do ponto P e suas precisões
% Resolução completa incluindo itens (a) a (j)

clc;
clear;
close all;

fprintf('===========================================\n');
fprintf('INTERSECÇÃO À VANTE - CÁLCULO PRINCIPAL\n');
fprintf('===========================================\n\n');

%% Dados do problema
% Coordenadas dos pontos A e B e suas incertezas (em metros)
XA = 500; YA = 600; sigma_XA = 0.05; sigma_YA = 0.03;
XB = 550; YB = 650; sigma_XB = 0.03; sigma_YB = 0.04;

% Ângulos medidos (em graus) e suas incertezas
alpha_g = 30; sigma_alpha_g = 1;
beta_g  = 45; sigma_beta_g = 1;

% Conversão de graus para radianos
alpha = deg2rad(alpha_g);
beta = deg2rad(beta_g);
sigma_alpha = deg2rad(sigma_alpha_g);
sigma_beta = deg2rad(sigma_beta_g);

%% Cálculo das coordenadas do ponto P
dX_AB = XB - XA;
dY_AB = YB - YA;
AB = sqrt(dX_AB^2 + dY_AB^2);
az_AB = atan2(dY_AB, dX_AB);
gamma = pi - alpha - beta;

AP = AB * sin(beta) / sin(gamma);
BP = AB * sin(alpha) / sin(gamma);

az_AP = az_AB + alpha;
az_BP = az_AB - pi + beta;

XP_A = XA + AP * cos(az_AP);
YP_A = YA + AP * sin(az_AP);
XP_B = XB + BP * cos(az_BP);
YP_B = YB + BP * sin(az_BP);

XP = (XP_A + XP_B) / 2;
YP = (YP_A + YP_B) / 2;

%% Propagação das incertezas
h = 1e-6;

% Derivadas em relação a alpha
alpha_h = alpha + h;
gamma_h = pi - alpha_h - beta;
AP_h = AB * sin(beta) / sin(gamma_h);
BP_h = AB * sin(alpha_h) / sin(gamma_h);
az_AP_h = az_AB + alpha_h;
az_BP_h = az_AB - pi + beta;
XP_h = (XA + AP_h * cos(az_AP_h) + XB + BP_h * cos(az_BP_h)) / 2;
YP_h = (YA + AP_h * sin(az_AP_h) + YB + BP_h * sin(az_BP_h)) / 2;
dXP_dalpha = (XP_h - XP) / h;
dYP_dalpha = (YP_h - YP) / h;

% Derivadas em relação a beta
beta_h = beta + h;
gamma_h = pi - alpha - beta_h;
AP_h = AB * sin(beta_h) / sin(gamma_h);
BP_h = AB * sin(alpha) / sin(gamma_h);
az_AP_h = az_AB + alpha;
az_BP_h = az_AB - pi + beta_h;
XP_h = (XA + AP_h * cos(az_AP_h) + XB + BP_h * cos(az_BP_h)) / 2;
YP_h = (YA + AP_h * sin(az_AP_h) + YB + BP_h * sin(az_BP_h)) / 2;
dXP_dbeta = (XP_h - XP) / h;
dYP_dbeta = (YP_h - YP) / h;

%% Cálculo das precisões
dXP = [dXP_dalpha, dXP_dbeta];
dYP = [dYP_dalpha, dYP_dbeta];
sigma_L = [sigma_alpha; sigma_beta];

sigma2_XP = dXP * diag(sigma_L.^2) * dXP';
sigma2_YP = dYP * diag(sigma_L.^2) * dYP';

sigma_XP = sqrt(sigma2_XP);
sigma_YP = sqrt(sigma2_YP);

%% RESULTADO PRINCIPAL - Coordenadas do Ponto P e Precisões
fprintf('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n');
fprintf('RESULTADO PRINCIPAL - COORDENADAS DO PONTO P:\n');
fprintf('XP = %.3f m ± %.4f m\n', XP, sigma_XP);
fprintf('YP = %.3f m ± %.4f m\n', YP, sigma_YP);
fprintf('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n');

%% Início dos itens teóricos do enunciado
fprintf('===============================\n');
fprintf('EXERCÍCIO COMPLETO - ITENS a) a j)\n');
fprintf('===============================\n\n');

%% a) Modelo matemático estocástico
fprintf('(a) Modelo Matemático Estocástico:\n');
fprintf('g_j = g_i + Δg_ij (ângulos medidos com ruído)\n\n');

%% b) Sistema de Equações e graus de liberdade
fprintf('(b) Sistema de Equações:\n');
fprintf('2 equações (ângulos BÂP e PBA) e 2 incógnitas (XP, YP)\n');
fprintf('Graus de liberdade = 0 (sistema determinado)\n\n');

fprintf('(b) Sistema de Equações:\n');
fprintf('Equação 1 (ângulo BÂP):\n');
fprintf('alpha = atan((YP - YA) / (XP - XA)) - atan((YB - YA) / (XB - XA))\n\n');
fprintf('Equação 2 (ângulo PBA):\n');
fprintf('beta = atan((YP - YB) / (XP - XB)) - atan((YA - YB) / (XA - XB))\n\n');
fprintf('2 incógnitas: XP e YP\n');
fprintf('Grau de liberdade = 0 (sistema determinado)\n\n');


%% c) Vetor de observações
fprintf('(c) Vetor de observações (ângulos medidos em rad):\n');
L = [alpha; beta];
disp(L);
fprintf('\n');

%% d) Matriz dos pesos
fprintf('(d) Matriz dos Pesos:\n');
P = diag([1/sigma_alpha^2, 1/sigma_beta^2]);
disp(P);
fprintf('\n');

%% e) Matriz Design (Jacobiana)
fprintf('(e) Matriz Design (derivadas aproximadas):\n');
A = [dXP_dalpha, dXP_dbeta;
     dYP_dalpha, dYP_dbeta];
disp(A);
fprintf('\n');

%% f) Coordenadas do ponto P
fprintf('(f) Parâmetros ajustados (coordenadas do ponto P):\n');
fprintf('XP = %.3f m\n', XP);
fprintf('YP = %.3f m\n\n', YP);

%% g) Vetor dos resíduos
fprintf('(g) Vetor dos resíduos:\n');
V = [0; 0];
disp(V);
fprintf('\n');

%% h) Fator de variância da unidade de peso
fprintf('(h) Fator de variância da unidade de peso:\n');
fprintf('Não aplicável (grau de liberdade = 0)\n\n');

%% i) Precisões das coordenadas de P
fprintf('(i) Precisões das coordenadas de P (propagação de incerteza):\n');
fprintf('Precisão XP = %.4f m\n', sigma_XP);
fprintf('Precisão YP = %.4f m\n\n', sigma_YP);

%% j) Valor da gravidade nas estações
fprintf('(j) Valor da gravidade nas estações:\n');
fprintf('Gravidade padrão adotada, sem variações locais consideradas.\n');

%% Gráfico final
figure;
hold on;
plot([XA, XB], [YA, YB], 'bo-', 'LineWidth', 1.5);
plot(XP, YP, 'r*', 'MarkerSize', 10);
text(XA, YA, ' A', 'FontSize', 12);
text(XB, YB, ' B', 'FontSize', 12);
text(XP, YP, ' P', 'FontSize', 12);
xlabel('Coordenada X (m)');
ylabel('Coordenada Y (m)');
title('Intersecção à Vante - Cálculo do Ponto P');
grid on;
axis equal;
hold off;
