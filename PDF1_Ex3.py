#TA ERRADO
var = 0
sequencia = 0
resp = 0
aux = 0
for i in range(2,1000000):
	var = i
	while(var!=1):
		if(var%2==0):
			var = var/2
		else:
			var = (var*3)+1
		sequencia+=1
	if(sequencia>aux):
		resp = i
	aux = sequencia
	sequencia = 0
print(resp)
