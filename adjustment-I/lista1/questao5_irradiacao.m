function questao5_irradiacao()
    % Dados fornecidos
    xA = 1896.564; % m (coordenada x do ponto A)
    yA = 2485.693; % m (coordenada y do ponto A)
    sigma_xA = 0.036; % m (incerteza de xA)
    sigma_yA = 0.094; % m (incerteza de yA)

    dA1 = 41.672; % m (distância A-1)
    dA2 = 29.137; % m (distância A-2)
    sigma_dA1 = 0.009; % m (incerteza de dA1)
    sigma_dA2 = 0.012; % m (incerteza de dA2)

    AzA1 = deg2rad(dms2degrees([82 28 40])); % rad (azimute A-1)
    AzA2 = deg2rad(dms2degrees([103 41 54])); % rad (azimute A-2)
    sigma_AzA1 = deg2rad(5 / 3600); % rad (incerteza de AzA1 em radianos)
    sigma_AzA2 = deg2rad(2 / 3600); % rad (incerteza de AzA2 em radianos)

    % Cálculo das coordenadas dos pontos 1 e 2
    x1 = xA + dA1 * sin(AzA1);
    y1 = yA + dA1 * cos(AzA1);
    x2 = xA + dA2 * sin(AzA2);
    y2 = yA + dA2 * cos(AzA2);

    % Cálculo das incertezas (propagação de variância)
    sigma_x1 = sqrt((sin(AzA1) * sigma_dA1)^2 + (dA1 * cos(AzA1) * sigma_AzA1)^2 + sigma_xA^2);
    sigma_y1 = sqrt((cos(AzA1) * sigma_dA1)^2 + (dA1 * sin(AzA1) * sigma_AzA1)^2 + sigma_yA^2);
    sigma_x2 = sqrt((sin(AzA2) * sigma_dA2)^2 + (dA2 * cos(AzA2) * sigma_AzA2)^2 + sigma_xA^2);
    sigma_y2 = sqrt((cos(AzA2) * sigma_dA2)^2 + (dA2 * sin(AzA2) * sigma_AzA2)^2 + sigma_yA^2);

    % Exibição dos resultados
    fprintf('Coordenadas do ponto 1:\n');
    fprintf('x1: %.3f ± %.3f m\n', x1, sigma_x1);
    fprintf('y1: %.3f ± %.3f m\n', y1, sigma_y1);
    fprintf('\nCoordenadas do ponto 2:\n');
    fprintf('x2: %.3f ± %.3f m\n', x2, sigma_x2);
    fprintf('y2: %.3f ± %.3f m\n', y2, sigma_y2);
end
