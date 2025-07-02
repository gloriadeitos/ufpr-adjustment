% não conferi

% QUESTÃO 1 - Estimativa das coordenadas do vértice C1
% Ajustamento por mínimos quadrados de coordenadas a partir de distâncias medidas

% Dados dos pontos do SGB
E = [645545.053; 645945.053; 646445.053];
N = [8624964.644; 8625264.644; 8624864.644];

% Distâncias medidas (ΔE e ΔN para cada ponto)
delta_E = [558.856; 158.736; -341.368];
delta_N = [-1376.407; -1676.925; -1276.806];

% Precisões das distâncias (desvios padrão em metros)
sigma_delta_E = [0.031; 0.069; 0.038];
sigma_delta_N = [0.025; 0.047; 0.029];

% Matriz de pesos (inverso da variância)
P = diag([1./(sigma_delta_E.^2); 1./(sigma_delta_N.^2)]);

% Aproximação inicial para C1 (pode ser a média dos pontos conhecidos)
C1_approx = [mean(E); mean(N)];

% Ajustamento por mínimos quadrados iterativo
max_iter = 10;
tol = 1e-6;
for iter = 1:max_iter
    % Calcular ΔE e ΔN aproximados e Jacobiano
    delta_E_approx = [];
    delta_N_approx = [];
    J = [];
    for i = 1:3
        % ΔE e ΔN aproximados
        delta_E_approx_i = E(i) - C1_approx(1);
        delta_N_approx_i = N(i) - C1_approx(2);
        delta_E_approx = [delta_E_approx; delta_E_approx_i];
        delta_N_approx = [delta_N_approx; delta_N_approx_i];
        
        % Elementos do Jacobiano (derivadas de ΔE e ΔN em relação a E_C1 e N_C1)
        J_row_E = [-1, 0];
        J_row_N = [0, -1];
        J = [J; J_row_E; J_row_N];
    end
    
    % Vetor de observações (ΔE e ΔN medidos)
    d = [delta_E; delta_N];
    
    % Vetor de observações aproximadas (ΔE e ΔN calculados)
    d_approx = [delta_E_approx; delta_N_approx];
    
    % Vetor de discrepâncias
    delta_d = d - d_approx;
    
    % Solução do sistema normal
    delta_C1 = inv(J'*P*J)*J'*P*delta_d;
    
    % Atualizar estimativa
    C1_approx = C1_approx + delta_C1;
    
    % Critério de parada
    if norm(delta_C1) < tol
        break;
    end
end

% Resultados finais
E_C1 = C1_approx(1);
N_C1 = C1_approx(2);

% Matriz variância-covariância
Sigma_C1 = inv(J'*P*J);

% Exibir resultados
fprintf('Questão 1 - Coordenadas estimadas do vértice C1:\n');
fprintf('E = %.3f ± %.3f m\n', E_C1, sqrt(Sigma_C1(1,1)));
fprintf('N = %.3f ± %.3f m\n', N_C1, sqrt(Sigma_C1(2,2)));
fprintf('Matriz variância-covariância:\n');
disp(Sigma_C1);
