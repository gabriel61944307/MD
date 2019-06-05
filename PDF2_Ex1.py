verificaprimo = 1
sumprimo = 0
cont = 2
while (cont<=2000000):
	verificaprimo = 1
	for x in range(2,cont):
		if(x>cont**0.5):
			break
		if(cont%x==0):
			verificaprimo = 0
	if(verificaprimo):
			sumprimo = sumprimo + cont
	cont+=1
print(sumprimo)
