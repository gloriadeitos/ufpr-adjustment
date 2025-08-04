function questao2_transformacao_SAD69_SIRGAS2000()
    % Dados fornecidos (coordenadas SAD69 e incertezas)
    X_sad = 4192135.603;    % m
    Y_sad = -4114543.969;   % m
    Z_sad = -2477249.614;   % m
    sigma_X_sad = 0.065;    % m
    sigma_Y_sad = 0.038;    % m
    sigma_Z_sad = 0.074;    % m

    % Parâmetros de transformação (substitua pelos valores oficiais!)
    delta_X = -67.35;       % m (translação em X)
    delta_Y = 3.88;         % m (translação em Y)
    delta_Z = -38.22;       % m (translação em Z)

    % Transformação de coordenadas
    X_sirgas = X_sad + delta_X;
    Y_sirgas = Y_sad + delta_Y;
    Z_sirgas = Z_sad + delta_Z;

    % Exibição dos resultados (sem retorno no workspace)
    fprintf('Coordenadas SIRGAS 2000:\n');
    fprintf('X: %.3f ± %.3f m\n', X_sirgas, sigma_X_sad);
    fprintf('Y: %.3f ± %.3f m\n', Y_sirgas, sigma_Y_sad);
    fprintf('Z: %.3f ± %.3f m\n', Z_sirgas, sigma_Z_sad);
end
