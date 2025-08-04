% não conferi

% Questão 8 - Cálculo da distância plana entre pontos GNSS
function [D, sigma_D] = questao8_distancia_GNSS()
    % Dados fornecidos
    E00 = 459010.343; N00 = 8742389.123; sigma_E00 = 0.005; sigma_N00 = 0.004;
    E01 = 459203.202; N01 = 8742196.264; sigma_E01 = 0.007; sigma_N01 = 0.002;

    % Cálculo da distância plana
    delta_E = E01 - E00;
    delta_N = N01 - N00;
    D = sqrt(delta_E^2 + delta_N^2);

    % Cálculo da incerteza (propagação de variância)
    sigma_D = sqrt(...
        ((delta_E / D) * sigma_E00)^2 + ...
        ((delta_E / D) * sigma_E01)^2 + ...
        ((delta_N / D) * sigma_N00)^2 + ...
        ((delta_N / D) * sigma_N01)^2 ...
    );

    % Exibição dos resultados
    fprintf('Distância plana entre os pontos: %.3f ± %.3f m\n', D, sigma_D);
end
