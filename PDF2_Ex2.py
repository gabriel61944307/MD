#NÃO TESTADO, FUNCIONA NOS PRIMEIROS NÚMEROS (TESTES RETORNAM RAPIDO PELO MENOS ATÉ <=112) MAS NAO FOI TESTADO COM <=500
soma = 0
divisores = 0
cont = 1
while(divisores<=500):
	divisores = 1	#Todo numero é divisivel por 1
	soma = soma + cont
	x=soma
	b=1
	while(int(x)>1):
		if(x == int(x)):
			divisores+=1
		b+=1
		x = soma/b
	cont+=1
print(soma)
print(cont)
