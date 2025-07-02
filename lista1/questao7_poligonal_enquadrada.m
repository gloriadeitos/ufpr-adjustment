% não conferi

% Questão 7 - Cálculo de coordenadas em poligonal enquadrada
function [xC, yC, xD, yD, xE, yE, sigma_xC, sigma_yC, sigma_xD, sigma_yD, sigma_xE, sigma_yE] = questao7_poligonal_enquadrada()
    % Dados fornecidos
    % Coordenadas dos pontos de referência
    xA = 1010.343; yA = 3389.123; sigma_xA = 0.004; sigma_yA = 0.002;
    xB = 1203.202; yB = 3196.264; sigma_xB = 0.001; sigma_yB = 0.003;
    xE = 2032.279; yE = 3460.288; sigma_xE_ref = 0.001; sigma_yE_ref = 0.002;
    xF = 2068.073; yF = 3627.213; sigma_xF = 0.002; sigma_yF = 0.001;

    % Ângulos e distâncias (convertidos para radianos e metros)
    angB_C = deg2rad(dms2degrees([83 10 51.9])); dist_BC = 297.082;
    angC_D = deg2rad(dms2degrees([251 42 24.9])); dist_CD = 307.141;
    angD_E = deg2rad(dms2degrees([139 22 51])); dist_DE = 381.310;
    angE_F = deg2rad(dms2degrees([122 50 04.7]));

    % Precisão da estação total
    sigma_ang = deg2rad(2 / 3600); % rad
    sigma_dist = 0.005; % m

    % Cálculo das coordenadas (simplificado - ajuste por mínimos quadrados seria ideal)
    % Aqui, apenas um cálculo sequencial é feito para exemplo
    Az_AB = atan2(xB - xA, yB - yA); % Azimute de A para B
    Az_BC = Az_AB + angB_C - pi; % Azimute de B para C
    xC = xB + dist_BC * sin(Az_BC);
    yC = yB + dist_BC * cos(Az_BC);

    Az_CD = Az_BC + angC_D - pi;
    xD = xC + dist_CD * sin(Az_CD);
    yD = yC + dist_CD * cos(Az_CD);

    Az_DE = Az_CD + angD_E - pi;
    xE = xD + dist_DE * sin(Az_DE);
    yE = yD + dist_DE * cos(Az_DE);

    % Incertezas (simplificadas - propagação sequencial)
    sigma_xC = sqrt(sigma_xB^2 + (sin(Az_BC) * sigma_dist)^2 + (dist_BC * cos(Az_BC) * sigma_ang)^2);
    sigma_yC = sqrt(sigma_yB^2 + (cos(Az_BC) * sigma_dist)^2 + (dist_BC * sin(Az_BC) * sigma_ang)^2);
    sigma_xD = sqrt(sigma_xC^2 + (sin(Az_CD) * sigma_dist)^2 + (dist_CD * cos(Az_CD) * sigma_ang)^2);
    sigma_yD = sqrt(sigma_yC^2 + (cos(Az_CD) * sigma_dist)^2 + (dist_CD * sin(Az_CD) * sigma_ang)^2);
    sigma_xE = sqrt(sigma_xD^2 + (sin(Az_DE) * sigma_dist)^2 + (dist_DE * cos(Az_DE) * sigma_ang)^2);
    sigma_yE = sqrt(sigma_yD^2 + (cos(Az_DE) * sigma_dist)^2 + (dist_DE * sin(Az_DE) * sigma_ang)^2);

    % Exibição dos resultados
    fprintf('Coordenadas do ponto C:\n');
    fprintf('xC: %.3f ± %.3f m\n', xC, sigma_xC);
    fprintf('yC: %.3f ± %.3f m\n', yC, sigma_yC);
    fprintf('\nCoordenadas do ponto D:\n');
    fprintf('xD: %.3f ± %.3f m\n', xD, sigma_xD);
    fprintf('yD: %.3f ± %.3f m\n', yD, sigma_yD);
    fprintf('\nCoordenadas do ponto E:\n');
    fprintf('xE: %.3f ± %.3f m\n', xE, sigma_xE);
    fprintf('yE: %.3f ± %.3f m\n', yE, sigma_yE);
end
