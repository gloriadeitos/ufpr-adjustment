% GA106 - Ajustamento I - Exercício 2 - Rede Gravimétrica
% Ajustamento pelo Método dos Mínimos Quadrados Paramétrico Linear
% Todas as respostas de (a) a (j) claramente identificadas
 
clc; clear all; close all; format long g;
 
fprintf('=== EXERCÍCIO 2 - AJUSTAMENTO DE REDE GRAVIMÉTRICA ===\n\n');
 
%% DADOS DO PROBLEMA
 
% Estações da rede (índices)
% 1-Curitiba, 2-São Mateus do Sul, 3-Bituruna, 4-Guarapuava,
% 5-Ponta Grossa, 6-Ortigueira, 7-Londrina, 8-Jaguariaiva,
% 9-Joaquim Távora, 10-Maringá, 11-Iretama
 
% Valor fixo (datum)
g_Curitiba = 978760.387; % mGal (estação 1)
 
% Observações: desníveis gravimétricos (mGal)
obs_data = [
    % [estação_inicial, estação_final, desnível, variância]
    1, 2, 17.174, 791;     % I1: Curitiba - São Mateus do Sul
    2, 3, 19.77, 331;      % I2: São Mateus do Sul - Bituruna
    4, 3, -100.289, 281;   % I3: Guarapuava - Bituruna (negativo pois final<inicial)
    4, 5, 39.395, 231;     % I4: Guarapuava - Ponta Grossa
    5, 1, -41.821, 405;    % I5: Ponta Grossa - Curitiba (negativo)
    5, 6, 39.836, 781;     % I6: Ponta Grossa - Ortigueira
    6, 7, 42.021, 605;     % I7: Ortigueira - Londrina
    5, 8, 66.519, 500;     % I8: Ponta Grossa - Jaguariaíva
    8, 9, 18.103, 845;     % I9: Jaguariaíva - Joaquim Távora
    7, 9, -33.512, 1201;   % I10: Londrina - Joaquim Távora (negativo)
    7, 10, 30.063, 281;    % I11: Londrina - Maringá
    10, 11, 48.542, 980;   % I12: Maringá - Iretama
    4, 11, 36.078, 720;    % I13: Guarapuava - Iretama
    8, 1, -108.267, 1000   % I14: Jaguariaíva - Curitiba (negativo, variância estimada)
];
 
n_obs = size(obs_data, 1);  % número de observações
n_est = 11;                 % número total de estações
n_param = n_est - 1;        % parâmetros livres (exceto Curitiba)
 
% Vetor das observações
L = obs_data(:, 3);
 
% Variâncias das observações
variancias = obs_data(:, 4);
 
fprintf('DADOS DA REDE GRAVIMÉTRICA:\n');
fprintf('Número de observações: %d\n', n_obs);
fprintf('Número de estações: %d\n', n_est);
fprintf('Número de parâmetros livres: %d\n\n', n_param);
 
%% (a) MODELO MATEMÁTICO ESTOCÁSTICO
 
fprintf('(a) MODELO MATEMÁTICO ESTOCÁSTICO:\n');
fprintf('    Modelo funcional: L = A*X + v\n');
fprintf('    onde:\n');
fprintf('    L = vetor das observações (desníveis gravimétricos)\n');
fprintf('    A = matriz design (coeficientes das incógnitas)\n');
fprintf('    X = vetor dos parâmetros (valores de gravidade)\n');
fprintf('    v = vetor dos resíduos\n\n');
fprintf('    Modelo estocástico: E[v] = 0, D[L] = σ₀²*Q_L = σ₀²*P⁻¹\n');
fprintf('    onde P é a matriz dos pesos\n\n');
 
%% (b) SISTEMA DE EQUAÇÕES E GRAUS DE LIBERDADE
 
fprintf('(b) SISTEMA DE EQUAÇÕES (forma matricial):\n');
fprintf('    L = A*X + v\n');
fprintf('    onde a equação para cada observação i é:\n');
fprintf('    Δgᵢ = g_final - g_inicial + vᵢ\n\n');
fprintf('    Graus de liberdade = n° observações - n° parâmetros\n');
fprintf('    GL = %d - %d = %d\n\n', n_obs, n_param, n_obs - n_param);
 
%% (c) VETOR DAS OBSERVAÇÕES
 
fprintf('(c) VETOR DAS OBSERVAÇÕES L (mGal):\n');
for i = 1:n_obs
    fprintf('    L(%d) = %8.3f  (I%d)\n', i, L(i), i);
end
fprintf('\n');
 
%% (d) MATRIZ DOS PESOS
 
% Matriz dos pesos (inverso das variâncias, normalizada)
sigma0_aprior = 1; % valor a priori da variância da unidade de peso
P = diag(sigma0_aprior^2 ./ variancias);
 
fprintf('(d) MATRIZ DOS PESOS P:\n');
fprintf('    P = σ₀²/σᵢ² (matriz diagonal)\n');
fprintf('    Elementos da diagonal:\n');
for i = 1:n_obs
    fprintf('    P(%d,%d) = %.6f\n', i, i, P(i,i));
end
fprintf('\n');
 
%% (e) MATRIZ DESIGN
 
% Construção da matriz design A
% Cada linha representa uma observação
% Cada coluna representa uma estação (exceto Curitiba que é fixa)
A = zeros(n_obs, n_param);
 
% Mapeamento: estação -> índice no vetor de parâmetros
% Curitiba (1) é fixa, então:
% São Mateus do Sul (2) -> parâmetro 1
% Bituruna (3) -> parâmetro 2
% Guarapuava (4) -> parâmetro 3
% Ponta Grossa (5) -> parâmetro 4
% Ortigueira (6) -> parâmetro 5
% Londrina (7) -> parâmetro 6
% Jaguariaíva (8) -> parâmetro 7
% Joaquim Távora (9) -> parâmetro 8
% Maringá (10) -> parâmetro 9
% Iretama (11) -> parâmetro 10
 
est_to_param = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; % Curitiba=0 (fixa)
 
for i = 1:n_obs
    est_inicial = obs_data(i, 1);
    est_final = obs_data(i, 2);
   
    % Coeficiente da estação final (+1)
    if est_final > 1 % não é Curitiba
        param_final = est_to_param(est_final);
        A(i, param_final) = 1;
    end
   
    % Coeficiente da estação inicial (-1)
    if est_inicial > 1 % não é Curitiba
        param_inicial = est_to_param(est_inicial);
        A(i, param_inicial) = -1;
    end
   
    % Se uma das estações é Curitiba, o termo constante já está implícito
    % na observação (desnível em relação ao datum)
end
 
fprintf('(e) MATRIZ DESIGN A (%dx%d):\n', size(A,1), size(A,2));
estacoes = {'SMS', 'BIT', 'GUA', 'PG', 'ORT', 'LON', 'JAG', 'JT', 'MAR', 'IRE'};
fprintf('    Obs|');
for j = 1:n_param
    fprintf('%4s', estacoes{j});
end
fprintf('\n');
for i = 1:n_obs
    fprintf('    %2d |', i);
    for j = 1:n_param
        fprintf('%4.0f', A(i,j));
    end
    fprintf('\n');
end
fprintf('\n');
 
%% RESOLUÇÃO DO SISTEMA PELO MMQ
 
% Matriz normal
N = A' * P * A;
 
% Vetor dos termos independentes
% Para observações envolvendo Curitiba, ajustar o termo independente
L_ajustado = L;
for i = 1:n_obs
    est_inicial = obs_data(i, 1);
    est_final = obs_data(i, 2);
   
    if est_inicial == 1 % Curitiba é inicial
        L_ajustado(i) = L(i) + g_Curitiba;
    elseif est_final == 1 % Curitiba é final
        L_ajustado(i) = L(i) - g_Curitiba;
    end
end
 
U = A' * P * L_ajustado;
 
% Solução
X = N \ U;
 
%% (f) VETOR DOS PARÂMETROS AJUSTADOS
 
fprintf('(f) VETOR DOS PARÂMETROS AJUSTADOS X (valores de gravidade em mGal):\n');
fprintf('    Curitiba (fixo) = %.3f\n', g_Curitiba);
for i = 1:n_param
    fprintf('    %s = %.3f\n', estacoes{i}, X(i));
end
fprintf('\n');
 
%% (g) VETOR DOS RESÍDUOS E ANÁLISE
 
% Cálculo dos resíduos
L_calculado = A * X;
% Ajustar para observações envolvendo Curitiba
for i = 1:n_obs
    est_inicial = obs_data(i, 1);
    est_final = obs_data(i, 2);
   
    if est_inicial == 1 % Curitiba é inicial
        L_calculado(i) = L_calculado(i) - g_Curitiba;
    elseif est_final == 1 % Curitiba é final
        L_calculado(i) = L_calculado(i) + g_Curitiba;
    end
end
 
v = L_calculado - L;
 
fprintf('(g) VETOR DOS RESÍDUOS v (mGal):\n');
fprintf('    Obs | Observado | Calculado | Resíduo\n');
for i = 1:n_obs
    fprintf('    %2d  |  %8.3f |  %8.3f | %7.3f\n', i, L(i), L_calculado(i), v(i));
end
 
% Análise dos resíduos
v_max = max(abs(v));
v_medio = mean(abs(v));
fprintf('\n    ANÁLISE DOS RESÍDUOS:\n');
fprintf('    Resíduo máximo (absoluto): %.3f mGal\n', v_max);
fprintf('    Resíduo médio (absoluto): %.3f mGal\n', v_medio);
fprintf('    Soma dos resíduos: %.6f mGal (deve ser ≈ 0)\n\n', sum(v));
 
%% (h) FATOR DE VARIÂNCIA DA UNIDADE DE PESO A POSTERIORI E TESTE QUI-QUADRADO
 
% Graus de liberdade
GL = n_obs - n_param;
 
% Fator de variância a posteriori
sigma0_post_squared = (v' * P * v) / GL;
sigma0_post = sqrt(sigma0_post_squared);
 
% Teste Qui-quadrado
chi2_calc = v' * P * v;
chi2_critico_95 = chi2inv(0.95, GL);  % Valor crítico para 95% de confiança
chi2_critico_05 = chi2inv(0.05, GL);  % Valor crítico para 5% de confiança
 
fprintf('(h) FATOR DE VARIÂNCIA DA UNIDADE DE PESO A POSTERIORI:\n');
fprintf('    σ₀² a posteriori = %.6f\n', sigma0_post_squared);
fprintf('    σ₀ a posteriori = %.6f\n', sigma0_post);
fprintf('    Graus de liberdade = %d\n\n', GL);
 
fprintf('    TESTE QUI-QUADRADO:\n');
fprintf('    χ² calculado = %.3f\n', chi2_calc);
fprintf('    χ² crítico (95%%) = %.3f\n', chi2_critico_95);
fprintf('    χ² crítico (5%%) = %.3f\n', chi2_critico_05);
 
if chi2_calc <= chi2_critico_95 && chi2_calc >= chi2_critico_05
    fprintf('    RESULTADO: O modelo está adequado (5%% ≤ χ² ≤ 95%%)\n\n');
else
    fprintf('    RESULTADO: O modelo pode não estar adequado\n\n');
end
 
%% (i) MATRIZ VARIÂNCIA-COVARIÂNCIA DOS PARÂMETROS AJUSTADOS
 
% MVC dos parâmetros
Qxx = inv(N);
Sigma_XX = sigma0_post_squared * Qxx;
 
% Desvios padrão dos parâmetros
sigma_X = sqrt(diag(Sigma_XX));
 
fprintf('(i) MATRIZ VARIÂNCIA-COVARIÂNCIA DOS PARÂMETROS AJUSTADOS:\n');
fprintf('    Desvios padrão dos parâmetros (mGal):\n');
for i = 1:n_param
    fprintf('    σ_%s = %.4f\n', estacoes{i}, sigma_X(i));
end
fprintf('\n    Matriz de correlação:\n');
R = corrcov(Sigma_XX);
fprintf('         ');
for j = 1:min(5,n_param)
    fprintf('%6s', estacoes{j});
end
fprintf('\n');
for i = 1:min(5,n_param)
    fprintf('    %s ', estacoes{i});
    for j = 1:min(5,n_param)
        fprintf('%6.3f', R(i,j));
    end
    fprintf('\n');
end
fprintf('\n');
 
%% (j) VALORES DE GRAVIDADE NAS ESTAÇÕES E SUAS PRECISÕES
 
fprintf('(j) VALORES DE GRAVIDADE NAS ESTAÇÕES E SUAS PRECISÕES:\n');
fprintf('================================================\n');
fprintf('RESULTADO FINAL:\n');
fprintf('================================================\n');
fprintf('Estação              | Gravidade (mGal) | Precisão (±mGal)\n');
fprintf('---------------------|------------------|------------------\n');
fprintf('Curitiba (datum)     |    %10.3f   |     FIXO\n', g_Curitiba);
for i = 1:n_param
    fprintf('%-20s |    %10.3f   |    ±%.4f\n', estacoes{i}, X(i), sigma_X(i));
end
fprintf('================================================\n\n');
 
%% VISUALIZAÇÃO GRÁFICA
 
figure('Position', [100, 100, 1000, 600]);
 
% Subplot 1: Resíduos
subplot(2,2,1);
bar(1:n_obs, v);
xlabel('Observação');
ylabel('Resíduo (mGal)');
title('Resíduos das Observações');
grid on;
 
% Subplot 2: Valores de gravidade
subplot(2,2,2);
g_valores = [g_Curitiba; X];
g_sigmas = [0; sigma_X];
errorbar(1:n_est, g_valores, g_sigmas, 'o-');
xlabel('Estação');
ylabel('Gravidade (mGal)');
title('Valores de Gravidade Ajustados');
grid on;
estacoes_todas = {'CUR', 'SMS', 'BIT', 'GUA', 'PG', 'ORT', 'LON', 'JAG', 'JT', 'MAR', 'IRE'};
set(gca, 'XTick', 1:n_est, 'XTickLabel', estacoes_todas);
 
% Subplot 3: Teste Qui-quadrado
subplot(2,2,3);
x_chi = 0:0.1:2*chi2_critico_95;
y_chi = chi2pdf(x_chi, GL);
plot(x_chi, y_chi, 'b-', 'LineWidth', 1.5);
hold on;
plot([chi2_calc chi2_calc], [0 max(y_chi)], 'r-', 'LineWidth', 2);
plot([chi2_critico_05 chi2_critico_05], [0 max(y_chi)], 'g--', 'LineWidth', 1);
plot([chi2_critico_95 chi2_critico_95], [0 max(y_chi)], 'g--', 'LineWidth', 1);
xlabel('χ²');
ylabel('Densidade de Probabilidade');
title('Teste Qui-quadrado');
legend('Distribuição χ²', 'χ² calculado', 'Limites críticos', 'Location', 'best');
grid on;
 
% Subplot 4: Precisões
subplot(2,2,4);
bar(1:n_param, sigma_X);
xlabel('Parâmetro');
ylabel('Desvio Padrão (mGal)');
title('Precisões dos Parâmetros Ajustados');
set(gca, 'XTick', 1:n_param, 'XTickLabel', estacoes);
grid on;
 
% Ajustar layout
sgtitle('Ajustamento da Rede Gravimétrica - Resultados');
 
fprintf('Gráficos gerados com os resultados do ajustamento.\n');
