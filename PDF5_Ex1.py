#Number Spiral Diagonals

soma_ds = 0 #direita superior
soma_di = 0 #direita inferior
soma_es = 0 #esquerda superior
soma_ei = 0 #esquerda inferior

for n in range(1,1002,2):
    maximo_por_nivel = n*n
    soma_ds += maximo_por_nivel
    if((n-1)>0):  
            soma_es += maximo_por_nivel - (n-1)
            soma_ei += maximo_por_nivel - ((n-1)*2)
            soma_di += maximo_por_nivel - ((n-1)*3)
        

print(soma_es + soma_ei +soma_ds + soma_di)        
