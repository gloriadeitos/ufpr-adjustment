% não conferi

% QUESTÃO 4 - Modelagem de superfície geoidal
% Ajustamento de diferentes modelos funcionais para interpolação de altura geoidal

% Dados dos pontos
E = [5468792.235; 5468254.112; 5468312.758; 5468567.489; ...
     5468435.546; 5468296.463; 5468677.938];
N = [8618613.854; 8618105.967; 8618516.854; 8618425.347; ...
     8618551.204; 8618492.438; 8618397.105];
z = [4.135; 3.208; 3.561; 4.002; 3.746; 3.946; 4.224];

% Modelo 1: z = aE + bN + c
A1 = [E, N, ones(size(E))];
X1 = inv(A1'*A1)*A1'*z;
V1 = z - A1*X1;
sigma0_1 = sqrt((V1'*V1)/(length(z)-3));

% Modelo 2: z = aE + bN + cEN + d
A2 = [E, N, E.*N, ones(size(E))];
X2 = inv(A2'*A2)*A2'*z;
V2 = z - A2*X2;
sigma0_2 = sqrt((V2'*V2)/(length(z)-4));

% Modelo 3: z = aE + bN + cE^2 + dN^2 + e
A3 = [E, N, E.^2, N.^2, ones(size(E))];
X3 = inv(A3'*A3)*A3'*z;
V3 = z - A3*X3;
sigma0_3 = sqrt((V3'*V3)/(length(z)-5));

% Exibir resultados
fprintf('Questão 4 - Modelagem de superfície geoidal:\n');

fprintf('\nModelo 1: z = aE + bN + c\n');
fprintf('a = %.6f\n', X1(1));
fprintf('b = %.6f\n', X1(2));
fprintf('c = %.6f\n', X1(3));
fprintf('Desvio padrão a posteriori: %.6f m\n', sigma0_1);

fprintf('\nModelo 2: z = aE + bN + cEN + d\n');
fprintf('a = %.6f\n', X2(1));
fprintf('b = %.6f\n', X2(2));
fprintf('c = %.6f\n', X2(3));
fprintf('d = %.6f\n', X2(4));
fprintf('Desvio padrão a posteriori: %.6f m\n', sigma0_2);

fprintf('\nModelo 3: z = aE + bN + cE^2 + dN^2 + e\n');
fprintf('a = %.6f\n', X3(1));
fprintf('b = %.6f\n', X3(2));
fprintf('c = %.6f\n', X3(3));
fprintf('d = %.6f\n', X3(4));
fprintf('e = %.6f\n', X3(5));
fprintf('Desvio padrão a posteriori: %.6f m\n', sigma0_3);

% Comparação dos modelos
fprintf('\nComparação dos modelos:\n');
fprintf('Modelo 1 - Graus de liberdade: %d, Sigma0: %.6f\n', length(z)-3, sigma0_1);
fprintf('Modelo 2 - Graus de liberdade: %d, Sigma0: %.6f\n', length(z)-4, sigma0_2);
fprintf('Modelo 3 - Graus de liberdade: %d, Sigma0: %.6f\n', length(z)-5, sigma0_3);
