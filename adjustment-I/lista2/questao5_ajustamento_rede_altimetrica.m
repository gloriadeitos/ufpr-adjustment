% não conferi

% QUESTÃO 5 - Ajustamento de rede altimétrica
% Ajustamento por mínimos quadrados de uma rede de nivelamento

% Dados das linhas niveladas
desnivel = [0.786; -0.942; 1.279; -0.296; 0.045; -1.009; ...
            0.234; -1.641; 0.921; 0.659; -2.951; -3.354; ...
            -0.234; -2.065; 0.6454; 0.298; -0.352; -2.301; ...
            0.826; -2.7651];
comprimento = [613.4392; 476.1046; 580.6570; 378.9997; 446.2192; 460.3333; ...
               555.2597; 389.3580; 353.9457; 304.7903; 908.1987; 534.8984; ...
               583.8855; 405.7017; 329.1027; 496.6747; 297.9362; 566.4929; ...
               463.2291; 453.6255];

% Altitude conhecida do ponto A
HA = 763.245;

% Número de pontos na rede (assumindo que são 5 pontos: A, B, C, D, E)
n_pontos = 5;

% Matriz de pesos (inverso do comprimento)
P = diag(1./comprimento);

% Montagem da matriz de coeficientes A
% Assumindo a seguinte configuração:
% Linhas 1-5: A-B, A-C, A-D, A-E, B-C
% Linhas 6-10: B-D, B-E, C-D, C-E, D-E
% (Esta configuração precisa ser ajustada conforme o desenho real da rede)
A = zeros(20, 5);
A(1,:) = [-1, 1, 0, 0, 0];  % A-B
A(2,:) = [-1, 0, 1, 0, 0];  % A-C
A(3,:) = [-1, 0, 0, 1, 0];  % A-D
A(4,:) = [-1, 0, 0, 0, 1];  % A-E
A(5,:) = [0, -1, 1, 0, 0];  % B-C
A(6,:) = [0, -1, 0, 1, 0];  % B-D
A(7,:) = [0, -1, 0, 0, 1];  % B-E
A(8,:) = [0, 0, -1, 1, 0];  % C-D
A(9,:) = [0, 0, -1, 0, 1];  % C-E
A(10,:) = [0, 0, 0, -1, 1]; % D-E
% (Preencher o restante conforme necessário)

% Vetor de observações
L = desnivel;

% Introduzir a condição do ponto fixo (A)
A = [A; [1, 0, 0, 0, 0]]; % Equação adicional para o ponto A
L = [L; HA];
P = blkdiag(P, 1e6); % Peso muito alto para a condição

% Solução por mínimos quadrados
X = inv(A'*P*A)*A'*P*L;

% Altitudes ajustadas
HB = X(2);
HC = X(3);
HD = X(4);
HE = X(5);

% Resíduos
V = A*X - L;

% Variância a posteriori
sigma0_quadrado = (V'*P*V)/(20 + 1 - 5); % 21 equações (20 medidas + 1 condição), 5 parâmetros

% Matriz variância-covariância das altitudes
Sigma_X = sigma0_quadrado * inv(A'*P*A);

% Exibir resultados
fprintf('Questão 5 - Ajustamento da rede altimétrica:\n');
fprintf('Altitude de A (fixa): %.4f m\n', HA);
fprintf('Altitude de B: %.4f ± %.4f m\n', HB, sqrt(Sigma_X(2,2)));
fprintf('Altitude de C: %.4f ± %.4f m\n', HC, sqrt(Sigma_X(3,3)));
fprintf('Altitude de D: %.4f ± %.4f m\n', HD, sqrt(Sigma_X(4,4)));
fprintf('Altitude de E: %.4f ± %.4f m\n', HE, sqrt(Sigma_X(5,5)));
fprintf('\nVariância a posteriori: %.6f m²\n', sigma0_quadrado);
