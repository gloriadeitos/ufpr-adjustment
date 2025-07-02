% Questão 3 - Cálculo de altitudes e incertezas por nivelamento geométrico (sem retorno 'ans')
function questao3_nivelamento_geometrico()
    % Dados fornecidos
    HRN = 98.652;      % m (altitude do RN)
    sigma_RN = 0.007;  % m (incerteza do RN)
    l1 = -0.581;       % m (leitura 1)
    sigma_l1 = 0.003;  % m (incerteza de l1)
    l2 = 0.776;        % m (leitura 2)
    sigma_l2 = 0.002;  % m (incerteza de l2)

    % Cálculo das altitudes
    H_A = HRN + l1;
    H_B = H_A + l2;

    % Cálculo das incertezas (propagação de variância)
    sigma_H_A = sqrt(sigma_RN^2 + sigma_l1^2);
    sigma_H_B = sqrt(sigma_H_A^2 + sigma_l2^2);

    % Exibição dos resultados (sem retorno no workspace)
    fprintf('=== QUESTÃO 3 ===\n');
    fprintf('Altitude do ponto A: %.3f ± %.3f m\n', H_A, sigma_H_A);
    fprintf('Altitude do ponto B: %.3f ± %.3f m\n', H_B, sigma_H_B);
end
