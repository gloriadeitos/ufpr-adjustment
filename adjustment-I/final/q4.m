% MMF: dado
% MME: a0_1 + a1_1 = dZ_1
%      a0_2 + a1_2 = dZ_2   
%      a0_3 + a1_3 = dZ_3 
%      a0_4 + a1_4 = dZ_4 
%      a0_5 + a1_5 = dZ_5 


% matriz dos pesos
P = diag ([ ??????? ]);


% matriz desing a0_1 a1_1 a0_2 a1_2 a0_3 a1_3 a0_4 a1_4 a0_5 a1_5

A = [1 1 0 0 0 0 0 0 0 0
     0 0 1 1 0 0 0 0 0 0
     0 0 0 0 1 1 0 0 0 0
     0 0 0 0 0 0 1 1 0 0
     0 0 0 0 0 0 0 0 1 1
     ];


% Lb vetor das observacoes (valores conhecidos --> a direita da equacao)
Zqg_1 = ?
Zqg_2 = ?
Zqg_3 = ?
Zqg_4 = ?
Zqg_5 = ?
Zdvbi_1 = ?
Zdvbi_2 = ?
Zdvbi_3 = ?
Zdvbi_4 = ?
Zdvbi_5 = ?
dZ_1 = Zqg_1 - Zdvbi_1 
dZ_2 = Zqg_2 - Zdvbi_2  
dZ_3 = Zqg_3 - Zdvbi_3  
dZ_4 = Zqg_4 - Zdvbi_4  
dZ_5 = Zqg_5 - Zdvbi_5  

Lb = [dZ_1 
      dZ_2 
      dZ_3 
      dZ_4 
      dZ_5 ]; % ja sendo delta

Xa= inv(A'*P*A)*A'*P*Lb
