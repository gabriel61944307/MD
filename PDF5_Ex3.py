# Procurada a intersecçao nas sequencias geradas, se nao achado e aumentado o tamanho da sequencia ate ser econtrado
tam = 100000
achou = 0

while(not achou):
 T = []
 P = []
 H = []
 for i in range(55386,tam):
    T.append((i*(i-1)/2))

 for i in range(32096,tam):
    P.append((i*(3*i-1)/2))

 for i in range(27834,tam):
    H.append((i*(2*i-1)))



 valor = set(T).intersection(H,P)

 valor = list(valor)
 if(valor):
    achou = 1
 tam +=100000
    
print(valor[0])
 
print(T.index(valor[0])+285)
