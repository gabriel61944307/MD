a = 2**1000	#2 elevado a 100.
soma = 0
while(a!=0):			#Quando o ultimo algarismo do número
	soma = soma + a%10	#passar neste laço a variável a passará a ser 
	a=a//10			#igual a 0, este é o momento em que o laço
print(soma)			#se encerra.
