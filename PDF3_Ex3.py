i = 0
cont = 0
termos = []	#Lista termos de a elevado a b.
for a in range(2,101):			#Estes laços em conjunto fazem a e b oscilarem
  for b in range(2,101):		#em todas combinações posíveis.
		cont+=1
		c = a**b
		termos.append(c)	#Adiciona c a lista de termos.
termos.sort()	#Organiza a lista de termos de forma crescente.
while(i<cont-1):
	if(termos[i]==termos[i+1]):	#Remove termos iguais da lista.
		termos.pop(i)
		cont-=1
	else:
		i+=1
print(cont)
