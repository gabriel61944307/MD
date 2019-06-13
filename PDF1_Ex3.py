valor_maior_sequencia=0
for i in range(2,1000000):
    maior_sequencia = 1
    valor = i
    while(valor!=1):
        if (valor%2==0):
            valor = valor/2
        else:
            valor = (3*valor+1)
        maior_sequencia = maior_sequencia+1    
    if(maior_sequencia>valor_maior_sequencia):
        valor_maior_sequencia=maior_sequencia
        resposta = i
print(resposta)  
