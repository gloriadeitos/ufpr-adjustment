% talvez esteja errado n sei

% Questão 6 - Cálculo do desnível por nivelamento trigonométrico (versão correta)
function questao6_nivelamento_trigonometrico()
    % Dados fornecidos
    ZAB_deg = 87 + 21/60 + 58.1/3600;  % Ângulo zenital em graus decimais
    sigma_ZAB_deg = 2.3/3600;           % Incerteza do ângulo em graus
    D_inc_cm = 15.543;                  % Distância inclinada em cm
    sigma_D_inc_cm = 0.008;             % Incerteza da distância em cm
    hA = 2.000;                         % Altura do instrumento (m)
    h1 = 1.82;                          % Altura do prisma (m)
    sigma_h1 = 0.019;                   % Incerteza da altura do prisma (m)

    % Conversões necessárias
    D_inc_m = D_inc_cm/100;             % Convertendo para metros
    sigma_D_inc_m = sigma_D_inc_cm/100;  % Convertendo para metros

    % Cálculo do desnível (fórmula correta com cotangente)
    delta_H = D_inc_m * cotd(ZAB_deg) + hA - h1;

    % Cálculo das derivadas parciais para propagação de incertezas
    partial_D = cotd(ZAB_deg);
    partial_Z = -D_inc_m * (1 + sind(ZAB_deg)^2) / sind(ZAB_deg)^2 * (pi/180);
    partial_h1 = -1;

    % Propagação de incertezas
    sigma_delta_H = sqrt(...
        (partial_D * sigma_D_inc_m)^2 + ...
        (partial_Z * sigma_ZAB_deg)^2 + ...
        (partial_h1 * sigma_h1)^2 ...
    );

    % Exibição dos resultados
    fprintf('=== QUESTÃO 6 - RESULTADOS ===\n');
    fprintf('Desnível entre A e B: %.4f ± %.4f m\n', delta_H, sigma_delta_H);
    fprintf('--------------------------------\n');
    fprintf('Detalhes dos cálculos:\n');
    fprintf('Ângulo zenital ZAB: %.6f° ± %.6f°\n', ZAB_deg, sigma_ZAB_deg);
    fprintf('Distância inclinada: %.3f cm ± %.3f cm\n', D_inc_cm, sigma_D_inc_cm);
    fprintf('Altura do instrumento: %.3f m\n', hA);
    fprintf('Altura do prisma: %.3f ± %.3f m\n', h1, sigma_h1);
end
