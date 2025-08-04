% não conferi

% QUESTÃO 6 - Ajustamento da trajetória de satélite
% Ajustamento por mínimos quadrados de um modelo polinomial de 2º grau

% Dados da trajetória
t = [0; 1; 2; 3; 4; 5; 6]; % tempo em segundos
Xs = [6509399.707; 6506451.417; 6503496.051; 6500533.613; ...
      6497564.107; 6494587.535; 6491603.901];
Ys = [-1261084.883; -1261725.022; -1262363.788; -1263001.183; ...
      -1263637.203; -1264271.850; -1264905.121];
Zs = [-2696126.041; -2702950.158; -2709771.328; -2716589.544; ...
      -2723404.798; -2730217.083; -2737026.392];

% Modelo funcional para cada componente:
% Xs = X0 + a1*t + a2*t^2
% Ys = Y0 + b1*t + b2*t^2
% Zs = Z0 + c1*t + c2*t^2

% Ajuste para componente X
A_X = [ones(size(t)), t, t.^2];
X_X = inv(A_X'*A_X)*A_X'*Xs;

% Ajuste para componente Y
A_Y = [ones(size(t)), t, t.^2];
X_Y = inv(A_Y'*A_Y)*A_Y'*Ys;

% Ajuste para componente Z
A_Z = [ones(size(t)), t, t.^2];
X_Z = inv(A_Z'*A_Z)*A_Z'*Zs;

% Estimativa da posição no instante t = 2.3 s
t_est = 2.3;
Xs_est = X_X(1) + X_X(2)*t_est + X_X(3)*t_est^2;
Ys_est = X_Y(1) + X_Y(2)*t_est + X_Y(3)*t_est^2;
Zs_est = X_Z(1) + X_Z(2)*t_est + X_Z(3)*t_est^2;

% Exibir resultados
fprintf('Questão 6 - Ajustamento da trajetória de satélite:\n');

fprintf('\nParâmetros para componente X:\n');
fprintf('X0 = %.6f m\n', X_X(1));
fprintf('a1 = %.6f m/s\n', X_X(2));
fprintf('a2 = %.6f m/s²\n', X_X(3));

fprintf('\nParâmetros para componente Y:\n');
fprintf('Y0 = %.6f m\n', X_Y(1));
fprintf('b1 = %.6f m/s\n', X_Y(2));
fprintf('b2 = %.6f m/s²\n', X_Y(3));

fprintf('\nParâmetros para componente Z:\n');
fprintf('Z0 = %.6f m\n', X_Z(1));
fprintf('c1 = %.6f m/s\n', X_Z(2));
fprintf('c2 = %.6f m/s²\n', X_Z(3));

fprintf('\nPosição estimada em t = 2.3 s:\n');
fprintf('Xs = %.3f m\n', Xs_est);
fprintf('Ys = %.3f m\n', Ys_est);
fprintf('Zs = %.3f m\n', Zs_est);
