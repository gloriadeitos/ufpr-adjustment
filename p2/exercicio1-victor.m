% GA106 - Ajustamento I - Exercício I - Intersecção à Vante
% Cálculo das coordenadas do ponto P e suas precisões
% Todas as respostas de (a) a (j) claramente identificadas
 
clc; clear all; close all; format long g;
 
fprintf('=== EXERCÍCIO I - INTERSECÇÃO À VANTE ===\n\n');
 
%% DADOS DO PROBLEMA
% Coordenadas dos pontos A e B com suas incertezas
XA = 500.000; YA = 600.000;
sigma_XA = 0.050; sigma_YA = 0.030;
 
XB = 550.000; YB = 650.000;
sigma_XB = 0.030; sigma_YB = 0.040;
 
% Ângulos medidos e suas incertezas
alpha_deg = 30.0; sigma_alpha_deg = 1.0; % graus
beta_deg = 45.0; sigma_beta_deg = 1.0;   % graus
 
% Conversão para radianos
alpha = deg2rad(alpha_deg);
beta = deg2rad(beta_deg);
sigma_alpha = deg2rad(sigma_alpha_deg);
sigma_beta = deg2rad(sigma_beta_deg);
 
fprintf('DADOS FORNECIDOS:\n');
fprintf('Ponto A: X = %.3f ± %.3f m, Y = %.3f ± %.3f m\n', XA, sigma_XA, YA, sigma_YA);
fprintf('Ponto B: X = %.3f ± %.3f m, Y = %.3f ± %.3f m\n', XB, sigma_XB, YB, sigma_YB);
fprintf('Ângulo α = %.1f° ± %.1f°\n', alpha_deg, sigma_alpha_deg);
fprintf('Ângulo β = %.1f° ± %.1f°\n\n', beta_deg, sigma_beta_deg);
 
%% (a) CÁLCULO DAS COORDENADAS DO PONTO P
 
% Método de Collins para intersecção à vante
cot_alpha = cot(alpha);
cot_beta = cot(beta);
 
% Fórmulas de Collins
XP = (XA*cot_beta + XB*cot_alpha + (YB - YA))/(cot_alpha + cot_beta);
YP = (YA*cot_beta + YB*cot_alpha + (XA - XB))/(cot_alpha + cot_beta);
 
fprintf('(a) COORDENADAS DO PONTO P:\n');
fprintf('    XP = %.6f m\n', XP);
fprintf('    YP = %.6f m\n\n', YP);
 
%% (b) CÁLCULO DA DISTÂNCIA AB
 
dX_AB = XB - XA;
dY_AB = YB - YA;
AB = sqrt(dX_AB^2 + dY_AB^2);
 
fprintf('(b) DISTÂNCIA AB:\n');
fprintf('    AB = %.6f m\n\n', AB);
 
%% (c) CÁLCULO DO AZIMUTE AB
 
az_AB_rad = atan2(dX_AB, dY_AB);
az_AB_deg = rad2deg(az_AB_rad);
 
fprintf('(c) AZIMUTE AB:\n');
fprintf('    Az_AB = %.6f° = %.6f rad\n\n', az_AB_deg, az_AB_rad);
 
%% (d) CÁLCULO DAS DISTÂNCIAS AP E BP
 
% Ângulo no ponto P
gamma = pi - alpha - beta;
 
% Lei dos senos
AP = AB * sin(beta) / sin(gamma);
BP = AB * sin(alpha) / sin(gamma);
 
fprintf('(d) DISTÂNCIAS AP E BP:\n');
fprintf('    AP = %.6f m\n', AP);
fprintf('    BP = %.6f m\n\n', BP);
 
%% (e) CÁLCULO DOS AZIMUTES AP E BP
 
az_AP_rad = az_AB_rad + alpha;
az_BP_rad = az_AB_rad + pi - beta; % Azimute BA + ângulo PBA
 
az_AP_deg = rad2deg(az_AP_rad);
az_BP_deg = rad2deg(az_BP_rad);
 
fprintf('(e) AZIMUTES AP E BP:\n');
fprintf('    Az_AP = %.6f° = %.6f rad\n', az_AP_deg, az_AP_rad);
fprintf('    Az_BP = %.6f° = %.6f rad\n\n', az_BP_deg, az_BP_rad);
 
%% (f) VERIFICAÇÃO DAS COORDENADAS (usando as distâncias e azimutes)
 
XP_verif_A = XA + AP * sin(az_AP_rad);
YP_verif_A = YA + AP * cos(az_AP_rad);
 
XP_verif_B = XB + BP * sin(az_BP_rad);
YP_verif_B = YB + BP * cos(az_BP_rad);
 
fprintf('(f) VERIFICAÇÃO DAS COORDENADAS:\n');
fprintf('    A partir de A: XP = %.6f m, YP = %.6f m\n', XP_verif_A, YP_verif_A);
fprintf('    A partir de B: XP = %.6f m, YP = %.6f m\n', XP_verif_B, YP_verif_B);
fprintf('    Diferenças: ΔX = %.6f m, ΔY = %.6f m\n\n', XP_verif_A-XP_verif_B, YP_verif_A-YP_verif_B);
 
%% (g) PROPAGAÇÃO DE ERROS - CÁLCULO DAS DERIVADAS PARCIAIS
 
% Usando diferenciação numérica
h = 1e-8;
 
% Função para calcular XP e YP
calc_P = @(xa, ya, xb, yb, a, b) deal(...
    (xa*cot(b) + xb*cot(a) + (yb - ya))/(cot(a) + cot(b)), ...
    (ya*cot(b) + yb*cot(a) + (xa - xb))/(cot(a) + cot(b)));
 
% Derivadas parciais de XP
[XP0, YP0] = calc_P(XA, YA, XB, YB, alpha, beta);
 
[XP_h, ~] = calc_P(XA+h, YA, XB, YB, alpha, beta);
dXP_dXA = (XP_h - XP0)/h;
 
[XP_h, ~] = calc_P(XA, YA+h, XB, YB, alpha, beta);
dXP_dYA = (XP_h - XP0)/h;
 
[XP_h, ~] = calc_P(XA, YA, XB+h, YB, alpha, beta);
dXP_dXB = (XP_h - XP0)/h;
 
[XP_h, ~] = calc_P(XA, YA, XB, YB+h, alpha, beta);
dXP_dYB = (XP_h - XP0)/h;
 
[XP_h, ~] = calc_P(XA, YA, XB, YB, alpha+h, beta);
dXP_dalpha = (XP_h - XP0)/h;
 
[XP_h, ~] = calc_P(XA, YA, XB, YB, alpha, beta+h);
dXP_dbeta = (XP_h - XP0)/h;
 
% Derivadas parciais de YP
[~, YP_h] = calc_P(XA+h, YA, XB, YB, alpha, beta);
dYP_dXA = (YP_h - YP0)/h;
 
[~, YP_h] = calc_P(XA, YA+h, XB, YB, alpha, beta);
dYP_dYA = (YP_h - YP0)/h;
 
[~, YP_h] = calc_P(XA, YA, XB+h, YB, alpha, beta);
dYP_dXB = (YP_h - YP0)/h;
 
[~, YP_h] = calc_P(XA, YA, XB, YB+h, alpha, beta);
dYP_dYB = (YP_h - YP0)/h;
 
[~, YP_h] = calc_P(XA, YA, XB, YB, alpha+h, beta);
dYP_dalpha = (YP_h - YP0)/h;
 
[~, YP_h] = calc_P(XA, YA, XB, YB, alpha, beta+h);
dYP_dbeta = (YP_h - YP0)/h;
 
fprintf('(g) DERIVADAS PARCIAIS:\n');
fprintf('    ∂XP/∂XA = %.6f\n', dXP_dXA);
fprintf('    ∂XP/∂YA = %.6f\n', dXP_dYA);
fprintf('    ∂XP/∂XB = %.6f\n', dXP_dXB);
fprintf('    ∂XP/∂YB = %.6f\n', dXP_dYB);
fprintf('    ∂XP/∂α = %.6f\n', dXP_dalpha);
fprintf('    ∂XP/∂β = %.6f\n', dXP_dbeta);
fprintf('    ∂YP/∂XA = %.6f\n', dYP_dXA);
fprintf('    ∂YP/∂YA = %.6f\n', dYP_dYA);
fprintf('    ∂YP/∂XB = %.6f\n', dYP_dXB);
fprintf('    ∂YP/∂YB = %.6f\n', dYP_dYB);
fprintf('    ∂YP/∂α = %.6f\n', dYP_dalpha);
fprintf('    ∂YP/∂β = %.6f\n\n', dYP_dbeta);
 
%% (h) MATRIZ JACOBIANA
 
J = [dXP_dXA, dXP_dYA, dXP_dXB, dXP_dYB, dXP_dalpha, dXP_dbeta;
     dYP_dXA, dYP_dYA, dYP_dXB, dYP_dYB, dYP_dalpha, dYP_dbeta];
 
fprintf('(h) MATRIZ JACOBIANA J:\n');
disp(J);
 
%% (i) MATRIZ VARIÂNCIA-COVARIÂNCIA DOS DADOS INICIAIS
 
Sigma_dados = diag([sigma_XA^2, sigma_YA^2, sigma_XB^2, sigma_YB^2, sigma_alpha^2, sigma_beta^2]);
 
fprintf('(i) MATRIZ VARIÂNCIA-COVARIÂNCIA DOS DADOS INICIAIS:\n');
fprintf('    Diagonal principal: [%.6f, %.6f, %.6f, %.6f, %.6f, %.6f]\n\n', ...
    diag(Sigma_dados));
 
%% (j) PRECISÕES DAS COORDENADAS DO PONTO P
 
% Lei da propagação de variâncias
Sigma_P = J * Sigma_dados * J';
 
% Desvios padrão das coordenadas de P
sigma_XP = sqrt(Sigma_P(1,1));
sigma_YP = sqrt(Sigma_P(2,2));
sigma_XY = Sigma_P(1,2); % Covariância entre X e Y
 
fprintf('(j) PRECISÕES DAS COORDENADAS DO PONTO P:\n');
fprintf('    σ_XP = %.6f m\n', sigma_XP);
fprintf('    σ_YP = %.6f m\n', sigma_YP);
fprintf('    σ_XY = %.6f m² (covariância)\n\n', sigma_XY);
 
fprintf('MATRIZ VARIÂNCIA-COVARIÂNCIA DE P:\n');
disp(Sigma_P);
 
%% RESPOSTA PRINCIPAL DO EXERCÍCIO
fprintf('\n================================================\n');
fprintf('RESPOSTA PRINCIPAL DA QUESTÃO:\n');
fprintf('COORDENADAS DO PONTO P E SUAS PRECISÕES:\n');
fprintf('================================================\n');
fprintf('XP = %.3f ± %.3f m\n', XP, sigma_XP);
fprintf('YP = %.3f ± %.3f m\n', YP, sigma_YP);
fprintf('================================================\n');
fprintf('\nInterpretação:\n');
fprintf('- O ponto P está localizado na coordenada (%.3f, %.3f)\n', XP, YP);
fprintf('- A incerteza da coordenada X é de ± %.3f m\n', sigma_XP);
fprintf('- A incerteza da coordenada Y é de ± %.3f m\n', sigma_YP);
fprintf('- Isso significa que as coordenadas reais do ponto P estão\n');
fprintf('  dentro desses intervalos com 68%% de confiança (1σ)\n');
 
 
%% VISUALIZAÇÃO GRÁFICA
 
figure('Position', [100, 100, 800, 600]);
hold on;
 
% Plotar pontos A e B
plot(XA, YA, 'bo', 'MarkerSize', 10, 'MarkerFaceColor', 'blue');
plot(XB, YB, 'go', 'MarkerSize', 10, 'MarkerFaceColor', 'green');
 
% Plotar ponto P
plot(XP, YP, 'r*', 'MarkerSize', 15, 'LineWidth', 2);
 
% Plotar linhas AB, AP e BP
plot([XA, XB], [YA, YB], 'k-', 'LineWidth', 1);
plot([XA, XP], [YA, YP], 'b--', 'LineWidth', 1);
plot([XB, XP], [YB, YP], 'g--', 'LineWidth', 1);
 
% Elipses de erro (simplificadas)
theta = 0:0.1:2*pi;
ellipse_XP = XP + 2*sigma_XP*cos(theta);
ellipse_YP = YP + 2*sigma_YP*sin(theta);
plot(ellipse_XP, ellipse_YP, 'r:', 'LineWidth', 1);
 
% Rótulos
text(XA-5, YA-5, 'A', 'FontSize', 12, 'FontWeight', 'bold');
text(XB+2, YB-5, 'B', 'FontSize', 12, 'FontWeight', 'bold');
text(XP+2, YP+2, 'P', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'red');
 
% Formatação do gráfico
xlabel('Coordenada X (m)', 'FontSize', 12);
ylabel('Coordenada Y (m)', 'FontSize', 12);
title('Intersecção à Vante - Determinação do Ponto P', 'FontSize', 14);
grid on;
axis equal;
legend('Ponto A', 'Ponto B', 'Ponto P', 'Linha AB', 'Linha AP', 'Linha BP', ...
       'Elipse de erro (2σ)', 'Location', 'best');
 
hold off;
 
fprintf('\nGráfico gerado com a configuração dos pontos e elipse de erro.\n');
