% Questão 4 - Transformação de coordenadas UTM para topográficas locais (sem retorno 'ans')
function questao4_transformacao_UTM_para_topografico()
    % Dados fornecidos
    E = 212729.2789;    % m (coordenada UTM E)
    N = 7656862.3784;   % m (coordenada UTM N)
    sigma_E = 0.005;     % m (incerteza de E)
    sigma_N = 0.002;     % m (incerteza de N)

    % Parâmetros de transformação
    a = 0.999373768;
    b = 0.017436700;
    delta_x = -344600.776;  % m
    delta_y = -7645843.148; % m

    % Transformação de coordenadas
    x = delta_x + a * E + b * N;
    y = delta_y - b * E + a * N;

    % Cálculo das incertezas (propagação de variância)
    sigma_x = sqrt((a * sigma_E)^2 + (b * sigma_N)^2);
    sigma_y = sqrt((b * sigma_E)^2 + (a * sigma_N)^2);

    % Exibição dos resultados (sem retorno no workspace)
    fprintf('=== QUESTÃO 4 ===\n');
    fprintf('Coordenadas topográficas locais:\n');
    fprintf('x: %.4f ± %.4f m\n', x, sigma_x);
    fprintf('y: %.4f ± %.4f m\n', y, sigma_y);
    fprintf('--------------------------------\n');
    fprintf('Parâmetros de transformação:\n');
    fprintf('a = %.9f\n', a);
    fprintf('b = %.9f\n', b);
    fprintf('Δx = %.3f m\n', delta_x);
    fprintf('Δy = %.3f m\n', delta_y);
end
