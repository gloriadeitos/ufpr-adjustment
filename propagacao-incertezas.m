% Propagação de Incertezas em Coordenadas Cartesianas a partir de Distância e Azimute

clc; clear all; format long g; close all; tic

% Dados

desv_pad_DH_BM=0.003; % m
desv_pad_Az_BM=deg2rad(3/3600); % rad

% 1º passo

MVC_DH_Az=[desv_pad_DH_BM^2    0;
           0            desv_pad_Az_BM^2]; % MVC da distância e azimute

% 2º passo

syms DH_BM Az_BM

x_B=0;
y_B=0;

x_M=x_B+DH_BM*sin(Az_BM)
y_M=y_B+DH_BM*cos(Az_BM)

dx_M__dDH_BM=diff(x_M,DH_BM); % derivada de x_M em relação a DH_BM
dx_M__dAz_BM=diff(x_M,Az_BM); % derivada de x_M em relação a Az_BM
dy_M__dDH_BM=diff(y_M,DH_BM); % derivada de y_M em relação a DH_BM
dy_M__dAz_BM=diff(y_M,Az_BM); % derivada de y_M em relação a Az_BM

DH_BM=30; % m
Az_BM=deg2rad(45); % rad

D=[eval(dx_M__dDH_BM) eval(dx_M__dAz_BM);
   eval(dy_M__dDH_BM) eval(dy_M__dAz_BM)];

% 3º passo

MVC_xy=D*MVC_DH_Az*D';

% Interpretação

desvio_pad_xM=sqrt(MVC_xy(1,1))  % elemento da MVC na 1º linha e 1ª coluna
desvio_pad_yM=sqrt(MVC_xy(2,2))  % elemento da MVC na 2º linha e 2ª coluna
