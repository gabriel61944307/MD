respa=0
respb=0
respc=0
for a in range(1,1000):
	for b in range(a+1,1000):
		c =1000-a-b
		if(a*a+b*b==c*c):
			respa=a
			respb=b
			respc=c
print(respa*respb*respc)
