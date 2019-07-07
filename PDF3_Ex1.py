somaDiv=0
for i in range (1, 10000):
  somaA = 0
  for j in range (1, i):
    if (i%j==0):    
      somaA = somaA + j
  
  somaB = 0
      
  for k in range(1, somaA): 
    if (somaA%k==0):
      somaB += k

  if (somaB == i and somaB != somaA):
    somaDiv += i  

print(somaDiv)
