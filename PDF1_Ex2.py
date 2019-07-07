respa=0		#Armazena a resposta de a.
respb=0		#Armazena a resposta de b.
respc=0		#Armazena a resposta de c.
for a in range(1,1000):
	for b in range(a+1,1000):
		c =1000-a-b		#1000 = a+b+c logo c = 1000-a-b.
		if(a*a+b*b==c*c):	#Se a²+b²=c² armazena as respostas.
			respa=a
			respb=b
			respc=c
print(respa*respb*respc)	#Mostra o produto de a, b e c.
