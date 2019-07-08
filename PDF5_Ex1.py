#Number Spiral Diagonals

soma_ds = 0 #Soma da diagonal direita superior
soma_di = 0 #Soma da diagonal direita inferior
soma_es = 0 #Soma da diagonal esquerda superior
soma_ei = 0 #Soma da diagonal esquerda inferior

for n in range(1,1002,2): #for com todos os valores usados para obter os cantos superiores direitos
    maximo_por_nivel = n*n #Obtido canto superior direito
    soma_ds += maximo_por_nivel 
    if((n-1)>0):  
            soma_es += maximo_por_nivel - (n-1) #n-1 : valores a ser subtraidos para chegar no proximo 
                                                #canto (Esquerdo Superior)
            soma_ei += maximo_por_nivel - ((n-1)*2)
            soma_di += maximo_por_nivel - ((n-1)*3)
        

print(soma_es + soma_ei +soma_ds + soma_di)        
