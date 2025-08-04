clc; clear all; format long g; close all; tic

% declarando as variaveis siombolicas para as derivadas
syms xa ya xb yb d_AP d_BP

% modelo matematico funcional
d_AB = sqrt ((xa-xb)^2 + (ya-yb)^2);
Az_ab = atan ((xb-xa)/(yb-ya));
alfa = acos (((d_AP^2) +(d_AB^2) - (d_BP^2)) / (2 * d_AP * d_AB))

xp = xa + d_AP * sin(Az_ab-alfa)
yp = ya + d_AP * cos(Az_ab-alfa)

% calculo das funcoes derivadas xa ya xb yb d_AP d_BP
Dxp_dxA = diff(xp,xa);
Dxp_dyA = diff(xp,ya);
Dxp_dxB = diff(xp,xb);
Dxp_dxB = diff(xp,yb);
Dxp_dAP = diff(xp,d_AP);
Dxp_dBP = diff(xp,d_BP);

Dyp_dxA = diff(yp,xa);
Dyp_dyA = diff(yp,ya);
Dyp_dxB = diff(yp,xb);
Dyp_dxB = diff(yp,yb);
Dyp_dAP = diff(yp,d_AP);
Dyp_dBP = diff(yp,d_BP);

% declarar valores das variaveis
xa = 100;
ya = 100;
xb = 110;
yb = 105;
d_AP = 12.5
d_BP = 8.5

% 2°) matriz design jacobiana
D = [eval(Dxp_dxA) eval(Dxp_dyA) eval(Dxp_dxB) eval(Dxp_dxB) eval(Dxp_dAP) eval(Dxp_dBP);
    eval(Dyp_dxA) eval(Dyp_dyA) eval(Dyp_dxB) eval(Dyp_dxB) eval(Dyp_dAP) eval(Dyp_dBP)]; %eval aplica valor numerico nas variaveis derivaveis

% 1°) MVC das quantidades que propagam xa ya xb yb d_AP d_BP
MVCq = diag ([0.05^2 0.03^2 0.03^2 0.04^2 0.03^2 0.03^2]);


% propagacao das variancias
MVC_xpyp = D * MVCq * D';

xp = eval(xp);
yp = eval(yp);
dp_xp = sqrt(MVC_xpyp(1,1));
dp_yp = sqrt(MVC_xpyp(2,2));
