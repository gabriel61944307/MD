verificaprimo = 1
primo = 2		#2 e 3 ja estão incluidos como primos.
cont = 2
while (primo<=10001):	#Quando chegar no 10001º numero primo o laço é finalizado.
	cont+=1
	verificaprimo = 1
	for x in range(2,cont):		#Laço que decide se o número é primo ou não.
		if(x>cont**0.5):
			break
		if(cont%x==0):
			verificaprimo = 0
	if(verificaprimo):		#Se ao terminar o laço acima o verificador estiver no 1
			primo+=1	#significa que o numero é primo.
print(cont)				#O resultado esta em cont pois o laço parou no 10001 número primo.
