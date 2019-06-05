verificaprimo = 1
primo = 2
cont = 3
while (primo<=10001):
	cont+=1
	verificaprimo = 1
	for x in range(2,cont):
		if(x>cont**0.5):
			break
		if(cont%x==0):
			verificaprimo = 0
	if(verificaprimo):
			primo+=1
print(cont)
