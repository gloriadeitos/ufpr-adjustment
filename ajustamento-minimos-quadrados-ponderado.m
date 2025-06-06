% Universidade Federal do Paraná
% Ajustamento I 
% Glória Maria Deitos Gomes da Silva
% 06.Junho.2025

% Ajustamento de mínimos quadrados ponderado para determinar os parâmetros de uma reta (coeficientes)
% com base em observações com diferentes precisões (representadas na matriz de pesos).

clc; clear all; format long g; close all; tic

% Vetor das observações
Lb=[0.10; 0.97; 2.06; 3.11];

% Matriz desenho A
A=[-6 1;
   -4 1;
   -2 1;
    0 1];

% Matriz dos pesos - identidade
% P=eye(4,4);
P=1*[1/0.05^2 0 0 0;
    0 1/0.02^2 0 0;
    0 0 1/0.08^2 0;
    0 0 0 1/0.10^2];

% Vetor dos parâmetros ajustados
X=inv(A'*P*A)*A'*P*Lb;
