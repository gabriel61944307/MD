valor_maior_sequencia=0 #definindo a variavel auxiliar que salva o maior valor da sequencia temporario
for i in range(2,1000000):
    maior_sequencia = 1 #definindo o valor que sera a maior sequencia
    valor = i
    while(valor!=1): #definindo o loop enquanto o valor for maior que 1, que é onde a sequencia termina
        if (valor%2==0): #se o valor for par se divide o mesmo por 2
            valor = valor/2
        else: #se for impar é aplicado a formula n = 3n+1
            valor = (3*valor+1)
        maior_sequencia = maior_sequencia+1   #é somado mais um na maior sequencia
    if(maior_sequencia>valor_maior_sequencia): #se a sequencia calulada anteriormente for menor que a atual, 
                                               #é substituido o valor da maior sequencia e atribuido o numero a i
        valor_maior_sequencia=maior_sequencia
        resposta = i
print(resposta)  #apresentando o valor de i que é o da maior sequencia
