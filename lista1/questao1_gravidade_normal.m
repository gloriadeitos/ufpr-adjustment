% Questão 1 - Cálculo da gravidade normal e sua incerteza
function [gamma_p, sigma_gamma_p] = questao1_gravidade_normal()
    % Dados fornecidos
    gamma = 978985.50; % mGal (gravidade normal à latitude dada)
    dg_dn = -0.3086; % mGal/m (gradiente médio da gravidade)
    h_p = 12.632; % m (altitude elipsoidal)
    sigma_h_p = 0.059; % m (incerteza da altitude)

    % Cálculo da gravidade normal no ponto P (gamma_p)
    gamma_p = gamma + dg_dn * h_p;

    % Cálculo da incerteza de gamma_p (propagação de incerteza)
    sigma_gamma_p = abs(dg_dn) * sigma_h_p;

    % Exibição dos resultados
    fprintf('Gravidade normal no ponto P (γp): %.2f mGal\n', gamma_p);
    fprintf('Incerteza de γp: ±%.4f mGal\n', sigma_gamma_p);
end
