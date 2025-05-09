% Universidade Federal do Paraná
% Ajustamento I 
% Glória Maria Deitos Gomes da Silva
% 09.Maio.2025

% clc = limpa o terminal
% clear all = limpa a variável
% format long g = 15 casas decimais
% format long e = notação científica
% format long short = só 4 casas decimais

clc; clear all; format long g

% Dados de entrada
% dBC = 297.002
% dCD = 307.141
% dDE = 381.310

% ==

% Dados
DH_AB = 30.123;
Az_AB = (63+10/60+15/3600)*pi/100 % grau,min,seg -> grau decimal -> radianos
% ou função: Az_AB = deg2rad(63+10/60+15/3600);

% Matriz de transformação 2x2
D = [sin(Az_AB) DH_AB*cos(Az_AB);
    cos(Az_AB) -DH_AB*sin(Az_AB)];

% Matriz de variância-covariância da DH e Az
MVC_DH_Az = [0.005^2 0;
             0 (2.42D-5)^2]; % D-5 = -10^-5

% ou função: MVC_DH_Az = diag([0.005^2 (2.42D-5)^2]); 

% Lei da propagação de variâncias
MVC_xy = D*MVC_DH_Az*D' % D' = transposta

desv_pad_xB = sqrt(MVC_xy(1,1)) % desvio padrão de xB
desv_pad_yB = sqrt(MVC_xy(2,2))
