import numpy as np
import time

tam = 1000 #impar sempre
m = np.zeros((tam,tam))
indiceX = int(tam/2)
indiceY = int(tam/2)
m[indiceX][indiceY] = 1

#Para construir a espiral foi obtido o numero do canto superior direito e gerenciado os indices foi se preenchendo as posições anteriores ate o canto superior direito anterior.

for n in range(3,tam+1,2):
    indiceX-=1
    indiceY+=1
    maximo = n*n #numero do canto superior direito
    m[indiceX][indiceY] = maximo

    for i in range (1,n):
        indiceY -= 1
        maximo -= 1 
        m[indiceX][indiceY] = maximo

    for i in range (1,n):
        indiceX += 1
        maximo -= 1 
        m[indiceX][indiceY] = maximo
        
    for i in range (1,n):
        indiceY += 1
        maximo -= 1 
        m[indiceX][indiceY] = maximo
        
    for i in range (1,n):
        indiceX -= 1
        maximo -= 1
        if(i!=(n-1)): #para nao sobreescrever o canto superior direito anterior
            m[indiceX][indiceY] = maximo


movKX = [-1,1,-2,-2,-1,1,2,2] #vetores para movimento do cavalo
movKY = [2,2,1,-1,-2,-2,-1,1]

cont2 = 0
for i in range(0,1000): # for para mostrar que em 1000 teste os resultados foram iguais
 menor_ant = 0
 indiceX = int(tam/2) #centro da matriz
 indiceY = int(tam/2)
 m2 = m.copy() 
 m2[indiceX][indiceY] = 0 # onde cavalo comeca
 cont2 +=1 
 print("Numero do teste:", cont2)
 cont = 0
 while(1):
    soma_mov = 0
    cont += 1 
    menor_valor = 1000000

    '''nesse for é simulado as possiveis posições pro cavalo se mover e seus numeros, é guardado a menor posição e seu valor para atualização posterior'''   
    for j in range(0,8):
        valor = m2[indiceX+movKX[j]][indiceY+movKY[j]]
        if valor < menor_valor and valor != 0 :
            menor_valor = valor
            indiceMOVX = indiceX+movKX[j]  #onde o cavalo ira
            indiceMOVY = indiceY+movKY[j] 
        soma_mov += valor
  
    if (soma_mov==0): #quando todas os movimetos possiveis forem 0
        print("Rodada do movimento:", cont)
        print("Ultima posicao cavalo:", menor_ant)
        break
    

    menor_ant = menor_valor    
    indiceX = indiceMOVX #atualizano indices com os novos valores
    indiceY = indiceMOVY
    m2[indiceX][indiceY] = 0 #marcando a posição que o cavalo já passou
 
 if(menor_ant != 2084): # obtido o resultado, foi colocado essa condição para que seja interrompido o teste caso falhe
     print("DIFERENTE")
     break   



