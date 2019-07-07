verificaprimo = 1
sumprimo = 0		#Armazena a soma dos primos
cont = 2
while (cont<=2000000):		#Laço que incrementa cont para que ele seja
	verificaprimo = 1	#verificado como primo ou não.
	for x in range(2,cont):		#Laço que decide se o número é primo ou não.
		if(x>cont**0.5):
			break
		if(cont%x==0):
			verificaprimo = 0
	if(verificaprimo):
			sumprimo = sumprimo + cont 	#Se o número for primo ele é
	cont+=1						#acrescido a variável.
print(sumprimo)
