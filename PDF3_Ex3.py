i = 0
cont = 0
termos = []
for a in range(2,101):
  for b in range(2,101):
		cont+=1
		c = a**b
		termos.append(c)
termos.sort()
while(i<cont-1):
	if(termos[i]==termos[i+1]):
		termos.pop(i)
		cont-=1
	else:
		i+=1
print(cont)
