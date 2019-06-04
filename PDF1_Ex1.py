verificador = 1
verificadorprimo = 1
cont = 2
primo = 1
while(verificador==1):
	cont+=1
	verificadorprimo=1
	for y in range(2, cont):
		if(y>cont**0.5):
			break
		elif(cont%y==0):
			verificadorprimo=0
	if(verificadorprimo):
		primo+=1
	if(primo==10001):
		verificador=0
print(cont)
