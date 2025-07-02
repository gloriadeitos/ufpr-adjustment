% filepath: c:\Users\victo\Downloads\ufpr-adjustment-main\new.m
% GA106 - Ajustamento I - Exercício I - Intersecção à Vante
% Resolução completa usando Método dos Mínimos Quadrados
% Respostas de (a) a (j) conforme solicitado
 
clc; clear all; close all; format long g;
 
fprintf('=== EXERCÍCIO I - INTERSECÇÃO À VANTE ===\n');
fprintf('=== MÉTODO DOS MÍNIMOS QUADRADOS ===\n\n');
 
%% DADOS DO PROBLEMA
% Coordenadas dos pontos A e B com suas incertezas
XA = 500.000; YA = 600.000;
sigma_XA = 0.050; sigma_YA = 0.030;
 
XB = 550.000; YB = 650.000;
sigma_XB = 0.030; sigma_YB = 0.040;
 
% Ângulos observados e suas incertezas
alpha_deg = 30.0; sigma_alpha_deg = 1.0; % ângulo B-A-P
beta_deg = 45.0; sigma_beta_deg = 1.0;   % ângulo P-B-A
 
% Conversão para radianos
alpha_obs = deg2rad(alpha_deg);
beta_obs = deg2rad(beta_deg);
sigma_alpha = deg2rad(sigma_alpha_deg);
sigma_beta = deg2rad(sigma_beta_deg);
 
fprintf('DADOS:\n');
fprintf('A: (%.3f±%.3f, %.3f±%.3f) m\n', XA, sigma_XA, YA, sigma_YA);
fprintf('B: (%.3f±%.3f, %.3f±%.3f) m\n', XB, sigma_XB, YB, sigma_YB);
fprintf('α = %.1f°±%.1f°, β = %.1f°±%.1f°\n\n', alpha_deg, sigma_alpha_deg, beta_deg, sigma_beta_deg);
 
%% (a) MODELO MATEMÁTICO ESTOCÁSTICO
 
fprintf('(a) MODELO MATEMÁTICO ESTOCÁSTICO:\n');
fprintf('------------------------------------\n');
fprintf('Modelo funcional:\n');
fprintf('L1 = α = atan2(XP-XA, YP-YA) - atan2(XB-XA, YB-YA)\n');
fprintf('L2 = β = atan2(XB-XP, YB-YP) - atan2(XA-XP, YA-YP)\n\n');
fprintf('Onde:\n');
fprintf('- L1, L2 = observações (ângulos α e β)\n');
fprintf('- XP, YP = parâmetros a estimar (coordenadas do ponto P)\n');
fprintf('- XA, YA, XB, YB = coordenadas conhecidas dos pontos A e B\n\n');
fprintf('Modelo estocástico:\n');
fprintf('E[L] = E[α, β]ᵀ (valor esperado das observações)\n');
fprintf('D[L] = Σ_L = diag[σ²_α, σ²_β] (matriz variância-covariância)\n\n');
 
%% Valores aproximados iniciais para XP e YP (usando método direto)
cot_alpha = cot(alpha_obs);
cot_beta = cot(beta_obs);
XP0 = (XA*cot_beta + XB*cot_alpha + (YB - YA))/(cot_alpha + cot_beta);
YP0 = (YA*cot_beta + YB*cot_alpha + (XA - XB))/(cot_alpha + cot_beta);
 
%% (b) SISTEMA DE EQUAÇÕES E GRAUS DE LIBERDADE
 
fprintf('(b) SISTEMA DE EQUAÇÕES E GRAUS DE LIBERDADE:\n');
fprintf('----------------------------------------------\n');
fprintf('Sistema linearizado: V = AX - L\n');
fprintf('Onde:\n');
fprintf('V = [v1, v2]ᵀ = vetor dos resíduos\n');
fprintf('A = matriz design (2×2)\n');
fprintf('X = [dXP, dYP]ᵀ = correções aos parâmetros\n');
fprintf('L = [l1, l2]ᵀ = vetor das observações reduzidas\n\n');
fprintf('Número de observações (n) = 2\n');
fprintf('Número de parâmetros (u) = 2\n');
fprintf('Graus de liberdade (r) = n - u = 2 - 2 = 0\n\n');
 
n_obs = 2;    % número de observações
n_param = 2;  % número de parâmetros
graus_lib = n_obs - n_param;
 
%% (c) VETOR DAS OBSERVAÇÕES
 
fprintf('(c) VETOR DAS OBSERVAÇÕES:\n');
fprintf('---------------------------\n');
 
% Observações originais
L_obs = [alpha_obs; beta_obs];
 
% Valores calculados com aproximações iniciais
az_AB = atan2(XB-XA, YB-YA);
az_AP0 = atan2(XP0-XA, YP0-YA);
az_BP0 = atan2(XP0-XB, YP0-YB);
az_BA = az_AB + pi;
 
alpha_calc = az_AP0 - az_AB;
beta_calc = az_BA - az_BP0;
 
% Observações reduzidas (diferença entre observado e calculado)
L_red = L_obs - [alpha_calc; beta_calc];
 
fprintf('L_obs = [%.6f; %.6f] rad = [%.3f°; %.3f°]\n', ...
    L_obs(1), L_obs(2), rad2deg(L_obs(1)), rad2deg(L_obs(2)));
fprintf('L_red = [%.8f; %.8f] rad\n\n', L_red(1), L_red(2));
 
%% (d) MATRIZ DOS PESOS
 
fprintf('(d) MATRIZ DOS PESOS:\n');
fprintf('---------------------\n');
 
% Matriz variância-covariância das observações
Sigma_L = diag([sigma_alpha^2, sigma_beta^2]);
 
% Fator de variância da unidade de peso a priori
sigma0_2 = 1; % assumindo variância unitária
 
% Matriz dos pesos
P = (sigma0_2 * inv(Sigma_L));
 
fprintf('Sigma_L = \n');
disp(Sigma_L);
fprintf('P = \n');
disp(P);
fprintf('\n');
 
%% (e) MATRIZ DESIGN
 
fprintf('(e) MATRIZ DESIGN:\n');
fprintf('-------------------\n');
 
% Cálculo das derivadas parciais (matriz A)
% Para α = atan2(XP-XA, YP-YA) - atan2(XB-XA, YB-YA)
dX_AP = XP0 - XA;
dY_AP = YP0 - YA;
r_AP2 = dX_AP^2 + dY_AP^2;
 
% Para β = atan2(XB-XP, YB-YP) - atan2(XA-XP, YA-YP)  
dX_BP = XB - XP0;
dY_BP = YB - YP0;
r_BP2 = dX_BP^2 + dY_BP^2;
 
dX_AP_inv = XA - XP0;
dY_AP_inv = YA - YP0;
r_AP_inv2 = dX_AP_inv^2 + dY_AP_inv^2;
 
% Derivadas parciais
% ∂α/∂XP
dalpha_dXP = -dY_AP/r_AP2;
% ∂α/∂YP  
dalpha_dYP = dX_AP/r_AP2;
 
% ∂β/∂XP
dbeta_dXP = dY_BP/r_BP2 + dY_AP_inv/r_AP_inv2;
% ∂β/∂YP
dbeta_dYP = -dX_BP/r_BP2 - dX_AP_inv/r_AP_inv2;
 
% Matriz design A
A = [dalpha_dXP, dalpha_dYP;
     dbeta_dXP,  dbeta_dYP];
 
fprintf('A = \n');
disp(A);
fprintf('\n');
 
%% (f) VETOR DOS PARÂMETROS AJUSTADOS
 
fprintf('(f) VETOR DOS PARÂMETROS AJUSTADOS:\n');
fprintf('------------------------------------\n');
 
% Solução por mínimos quadrados
N = A' * P * A;  % Matriz normal
U = A' * P * L_red;  % Vetor dos termos independentes
 
% Correções aos parâmetros
dX = inv(N) * U;
 
% Parâmetros ajustados
XP_ajust = XP0 + dX(1);
YP_ajust = YP0 + dX(2);
 
X_ajust = [XP_ajust; YP_ajust];
 
fprintf('Valores aproximados iniciais:\n');
fprintf('XP0 = %.6f m\n', XP0);
fprintf('YP0 = %.6f m\n\n', YP0);
 
fprintf('Correções:\n');
fprintf('dXP = %.8f m\n', dX(1));
fprintf('dYP = %.8f m\n\n', dX(2));
 
fprintf('Parâmetros ajustados:\n');
fprintf('XP = %.6f m\n', XP_ajust);
fprintf('YP = %.6f m\n\n', YP_ajust);
 
%% (g) VETOR DOS RESÍDUOS E ANÁLISE
 
fprintf('(g) VETOR DOS RESÍDUOS E ANÁLISE:\n');
fprintf('----------------------------------\n');
 
% Resíduos
V = A * dX - L_red;
 
fprintf('V = [%.8f; %.8f] rad = [%.6f″; %.6f″]\n', ...
    V(1), V(2), rad2deg(V(1))*3600, rad2deg(V(2))*3600);
 
fprintf('\nAnálise dos resíduos:\n');
fprintf('- Soma dos resíduos: %.2e (deve ser ≈ 0)\n', sum(V));
fprintf('- RMS dos resíduos: %.2e rad\n', sqrt(mean(V.^2)));
 
if graus_lib == 0
    fprintf('- Sistema determinado (r=0): resíduos são nulos por definição\n\n');
else
    fprintf('- Sistema redundante (r>0): resíduos indicam qualidade do ajuste\n\n');
end
 
%% (h) FATOR DE VARIÂNCIA A POSTERIORI E TESTE QUI-QUADRADO
 
fprintf('(h) FATOR DE VARIÂNCIA A POSTERIORI E TESTE QUI-QUADRADO:\n');
fprintf('-----------------------------------------------------------\n');
 
if graus_lib > 0
    % Fator de variância da unidade de peso a posteriori
    sigma0_2_post = (V' * P * V) / graus_lib;
   
    % Teste qui-quadrado
    chi2_calc = V' * P * V / sigma0_2;
    chi2_critico = chi2inv(0.95, graus_lib); % 95% confiança
   
    fprintf('σ₀²_posteriori = %.6f\n', sigma0_2_post);
    fprintf('χ²_calculado = %.6f\n', chi2_calc);
    fprintf('χ²_crítico(95%%, %d g.l.) = %.6f\n', graus_lib, chi2_critico);
   
    if chi2_calc <= chi2_critico
        fprintf('RESULTADO: Teste aceito (modelo adequado)\n\n');
    else
        fprintf('RESULTADO: Teste rejeitado (revisar modelo)\n\n');
    end
else
    fprintf('Sistema determinado (r=0): não é possível calcular σ₀²_posteriori\n');
    fprintf('Assumindo σ₀² = %.1f (valor a priori)\n\n', sigma0_2);
    sigma0_2_post = sigma0_2;
end
 
%% (i) MVC DOS PARÂMETROS AJUSTADOS E ANÁLISES
 
fprintf('(i) MVC DOS PARÂMETROS AJUSTADOS E ANÁLISES:\n');
fprintf('---------------------------------------------\n');
 
% Matriz variância-covariância dos parâmetros ajustados
Sigma_X = sigma0_2_post * inv(N);
 
% Precisões
sigma_XP = sqrt(Sigma_X(1,1));
sigma_YP = sqrt(Sigma_X(2,2));
sigma_XY = Sigma_X(1,2);
 
fprintf('Matriz variância-covariância dos parâmetros:\n');
fprintf('Sigma_X = \n');
disp(Sigma_X);
 
fprintf('Precisões:\n');
fprintf('σ_XP = %.6f m\n', sigma_XP);
fprintf('σ_YP = %.6f m\n', sigma_YP);
fprintf('σ_XY = %.6f m² (covariância)\n\n', sigma_XY);
 
% Elipse de erro
if abs(sigma_XY) > 1e-10
    % Parâmetros da elipse
    a = Sigma_X(1,1);
    b = Sigma_X(2,2);
    c = Sigma_X(1,2);
   
    lambda1 = 0.5 * (a + b + sqrt((a-b)^2 + 4*c^2));
    lambda2 = 0.5 * (a + b - sqrt((a-b)^2 + 4*c^2));
   
    semi_maior = sqrt(lambda1);
    semi_menor = sqrt(lambda2);
   
    if abs(c) > 1e-10
        theta = 0.5 * atan2(2*c, a-b);
    else
        theta = 0;
    end
   
    fprintf('Elipse de erro (1σ):\n');
    fprintf('Semi-eixo maior: %.6f m\n', semi_maior);
    fprintf('Semi-eixo menor: %.6f m\n', semi_menor);
    fprintf('Orientação: %.2f°\n\n', rad2deg(theta));
end
 
%% (j) COORDENADAS FINAIS E SUAS PRECISÕES
 
fprintf('(j) COORDENADAS FINAIS DO PONTO P E SUAS PRECISÕES:\n');
fprintf('====================================================\n');
fprintf('\n*** RESPOSTA PRINCIPAL DA QUESTÃO ***\n');
fprintf('COORDENADAS DO PONTO P:\n');
fprintf('XP = %.6f ± %.6f m\n', XP_ajust, sigma_XP);
fprintf('YP = %.6f ± %.6f m\n', YP_ajust, sigma_YP);
fprintf('====================================================\n\n');
 
fprintf('INTERPRETAÇÃO FINAL:\n');
fprintf('- Posição determinada: (%.3f, %.3f) m\n', XP_ajust, YP_ajust);
fprintf('- Precisão horizontal: ±%.1f cm em X, ±%.1f cm em Y\n', ...
    sigma_XP*100, sigma_YP*100);
fprintf('- Método: Intersecção à vante por mínimos quadrados\n');
 
%% VISUALIZAÇÃO GRÁFICA
figure('Position', [100, 100, 800, 600]);
hold on;
 
% Plotar pontos
plot(XA, YA, 'bo', 'MarkerSize', 10, 'MarkerFaceColor', 'blue');
plot(XB, YB, 'go', 'MarkerSize', 10, 'MarkerFaceColor', 'green');
plot(XP_ajust, YP_ajust, 'r*', 'MarkerSize', 15, 'LineWidth', 2);
 
% Plotar linhas
plot([XA, XB], [YA, YB], 'k-', 'LineWidth', 1);
plot([XA, XP_ajust], [YA, YP_ajust], 'b--', 'LineWidth', 1);
plot([XB, XP_ajust], [YB, YP_ajust], 'g--', 'LineWidth', 1);
 
% Elipse de erro
theta_plot = 0:0.1:2*pi;
ellipse_X = XP_ajust + 2*sigma_XP*cos(theta_plot);
ellipse_Y = YP_ajust + 2*sigma_YP*sin(theta_plot);
plot(ellipse_X, ellipse_Y, 'r:', 'LineWidth', 1);
 
% Rótulos
text(XA-8, YA-8, 'A', 'FontSize', 12, 'FontWeight', 'bold');
text(XB+3, YB-8, 'B', 'FontSize', 12, 'FontWeight', 'bold');
text(XP_ajust+3, YP_ajust+3, 'P', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'red');
 
xlabel('Coordenada X (m)');
ylabel('Coordenada Y (m)');
title('Intersecção à Vante - Ajustamento por Mínimos Quadrados');
grid on;
axis equal;
legend('Ponto A', 'Ponto B', 'Ponto P', 'Baseline AB', 'Linha AP', 'Linha BP', ...
       'Elipse de erro (2σ)', 'Location', 'best');
 
hold off;
