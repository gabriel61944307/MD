# Procurada a intersecçao nas sequencias geradas, se nao achado e aumentado o tamanho da sequencia ate ser econtrado
tam = 10000
achou = 0

while(not achou):
 T = [] #Vetores que armazenam a sequencia
 P = []
 H = []
 for i in range(286,tam): #Obtendo sequencia dos numeros Triangulares
    T.append((i*(i-1)/2))

 for i in range(166,tam): #Obtendo sequencia dos numeros Pentagonais
    P.append((i*(3*i-1)/2))

 for i in range(144,tam): #Obtendo sequencia dos numeros Hexagonais
    H.append((i*(2*i-1)))



 valor = set(T).intersection(H,P) #Obtendo a intersecção

 valor = list(valor) 
 if(valor): #se lista for nula  entao o intervalo é aumentado e refeito o while
    achou = 1
 tam +=10000
    
print(valor[0])
 
print(T.index(valor[0])+285)
