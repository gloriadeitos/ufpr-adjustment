% não conferi

% QUESTÃO 2 - Transformação de similaridade no plano
% Ajustamento pelo método combinado para estimar parâmetros de transformação

% Dados dos pontos (coordenadas UTM - consideradas sem erro)
E_UTM = [212729.2789; 212754.9376; 212716.3034; 212590.6534];
N_UTM = [7656862.3784; 7656910.8808; 7656716.5359; 7656993.0930];

% Coordenadas locais com suas precisões
x_local = [1505.6975; 1532.1860; 1490.1870; 1369.4380];
y_local = [2514.9592; 2562.9840; 2369.4340; 2648.0090];
sigma_x = [0.005; 0.002; 0.003; 0.005];
sigma_y = [0.002; 0.005; 0.007; 0.001];

% Matriz de pesos
P = diag([1./(sigma_x.^2); 1./(sigma_y.^2)]);

% Modelo funcional: 
% x = Δx + a*E + b*N
% y = Δy - b*E + a*N

% Montagem da matriz de coeficientes A
A = [];
L = [];
for i = 1:4
    A_row_x = [1, E_UTM(i), N_UTM(i), 0];
    A_row_y = [0, -N_UTM(i), E_UTM(i), 1];
    A = [A; A_row_x; A_row_y];
    
    L = [L; x_local(i); y_local(i)];
end

% Solução por mínimos quadrados
X = inv(A'*P*A)*A'*P*L;

% Parâmetros estimados
delta_x = X(1);
a = X(2);
b = X(3);
delta_y = X(4);

% Observações ajustadas
L_ajustado = A*X;

% Resíduos
V = L - L_ajustado;

% Variância a posteriori
sigma0_quadrado = (V'*P*V)/(2*4 - 4); % n=8 observações, u=4 parâmetros

% Matriz variância-covariância dos parâmetros
Sigma_X = sigma0_quadrado * inv(A'*P*A);

% Exibir resultados
fprintf('Questão 2 - Parâmetros da transformação:\n');
fprintf('Δx = %.6f ± %.6f m\n', delta_x, sqrt(Sigma_X(1,1)));
fprintf('a = %.6f ± %.6f\n', a, sqrt(Sigma_X(2,2)));
fprintf('b = %.6f ± %.6f\n', b, sqrt(Sigma_X(3,3)));
fprintf('Δy = %.6f ± %.6f m\n', delta_y, sqrt(Sigma_X(4,4)));
fprintf('\nVariância a posteriori: %.6f\n', sigma0_quadrado);
fprintf('\nMatriz variância-covariância dos parâmetros:\n');
disp(Sigma_X);
