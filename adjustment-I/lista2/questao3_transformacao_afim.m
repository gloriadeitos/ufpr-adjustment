% não conferi

% QUESTÃO 3 - Transformação afim para georreferenciamento de imagens
% Ajustamento para estimar parâmetros de transformação entre imagem e terreno

% Dados dos pontos
col = [3145.25; 2238.436; 2974.154; 1782.074];
linha = [814.75; 1499.397; 1217.432; 1297.547];
E = [636640.89; 609418.498; 631457.733; 595816.27];
N = [7520309.75; 7499756.56; 7508218.73; 7505732.91];

% Precisão das observações (0.5 pixel)
sigma = 0.5;
P = eye(8)/(sigma^2); % Matriz de pesos (8 observações)

% Modelo funcional:
% col = a1 + a2*E + a3*N
% linha = b1 + b2*E + b3*N

% Montagem da matriz de coeficientes A
A = [];
L = [];
for i = 1:4
    A_row_col = [1, E(i), N(i), 0, 0, 0];
    A_row_linha = [0, 0, 0, 1, E(i), N(i)];
    A = [A; A_row_col; A_row_linha];
    
    L = [L; col(i); linha(i)];
end

% Solução por mínimos quadrados
X = inv(A'*P*A)*A'*P*L;

% Parâmetros estimados
a1 = X(1); a2 = X(2); a3 = X(3);
b1 = X(4); b2 = X(5); b3 = X(6);

% Variância a posteriori
V = L - A*X;
sigma0_quadrado = (V'*P*V)/(8 - 6); % 8 observações, 6 parâmetros

% Matriz variância-covariância dos parâmetros
Sigma_X = sigma0_quadrado * inv(A'*P*A);

% Exibir resultados
fprintf('Questão 3 - Parâmetros da transformação afim:\n');
fprintf('Para coluna:\n');
fprintf('a1 = %.6f ± %.6f\n', a1, sqrt(Sigma_X(1,1)));
fprintf('a2 = %.6f ± %.6f\n', a2, sqrt(Sigma_X(2,2)));
fprintf('a3 = %.6f ± %.6f\n', a3, sqrt(Sigma_X(3,3)));
fprintf('\nPara linha:\n');
fprintf('b1 = %.6f ± %.6f\n', b1, sqrt(Sigma_X(4,4)));
fprintf('b2 = %.6f ± %.6f\n', b2, sqrt(Sigma_X(5,5)));
fprintf('b3 = %.6f ± %.6f\n', b3, sqrt(Sigma_X(6,6)));
fprintf('\nVariância a posteriori: %.6f (pixel^2)\n', sigma0_quadrado);
