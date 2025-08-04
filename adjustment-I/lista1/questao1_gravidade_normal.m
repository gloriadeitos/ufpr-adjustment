% Questão 1 - Cálculo da gravidade normal e sua incerteza (sem retorno 'ans')
function questao1_gravidade_normal()
    % Dados fornecidos
    gamma = 978985.50;   % mGal (gravidade normal à latitude dada)
    dg_dn = -0.3086;    % mGal/m (gradiente médio)
    h_p = 12.632;       % m (altitude elipsoidal)
    sigma_h_p = 0.059;   % m (incerteza da altitude)

    % Cálculos
    gamma_p = gamma + dg_dn * h_p;
    sigma_gamma_p = abs(dg_dn) * sigma_h_p;

    % Exibição dos resultados (sem retorno no workspace)
    fprintf('=== QUESTÃO 1 ===\n');
    fprintf('Gravidade normal no ponto P (γp): %.2f mGal\n', gamma_p);
    fprintf('Incerteza de γp: ±%.4f mGal\n', sigma_gamma_p);
end
