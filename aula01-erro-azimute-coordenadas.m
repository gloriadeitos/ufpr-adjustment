% Universidade Federal do Paraná
% Ajustamento I 
% Glória Maria Deitos Gomes da Silva
% 09.Maio.2025

% Calcular o desvio padrão (erro propagado) do azimute entre dois pontos (A e B) a partir dos erros nas coordenadas dos pontos,
% utilizando cálculo simbólico e a lei da propagação das variâncias.

clc; clear all; format long g

% Exercício: Determine o erro do Azimute A-B propagado a partir dos erros
% das coordenadas

% Desvios-padrão das coordenadas
s_xA = 0.003 %m
s_yA = 0.005 %m
s_xB = 0.001 %m
s_yB = 0.006 %m

% é não linear

% 1º passo) MVC das coordenadas x e y dos pontos A e B
MVC_xy = diag([s_xA^2 s_yA^2 s_xB^2 s_yB^2]);

% MVC_xy = [s_xA^2 0 0 0;
%           0 s_yA^2 0 0;
%           0 0 s_xB^2 0;
%           0 0 0 s_yB^2];

% 2º passo) Matriz da transformação D (derivadas parciais) 4x4
syms xA yA xB yB % transforma a variável de número para letra

Az_AB = pi+atan((xB-xA)/(yB-yA));

dAz_dxA = diff(Az_AB, xA);
dAz_dyA = diff(Az_AB, yA);
dAz_dxB = diff(Az_AB, xB);
dAz_dyB = diff(Az_AB, yB);

% Dados de entrada
xA = 9010.342;
yA = 2389.123;
xB = 9203.202;
yB = 2196.264;

D = [eval(dAz_dxA) eval(dAz_dyA) eval(dAz_dxB) eval(dAz_dyB)]

% 3º passo) Lei de propagação das variâncias
MVC_Az = D * MVC_xy*D';

desv_pad_Az = sqrt(MVC_Az(1,1))*180/pi*3600 % desvio padrão do Azimute AB em segundos 
