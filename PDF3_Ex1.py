somaDiv=0
for i in range (1, 10000): #loop que vai de 1 até ao 10000 que é a quantidade de numeros a ser analisado
  somaA = 0 # somaA é a soma de todos os numeros de j que dividem i com resto 0  
  for j in range (1, i):
    if (i%j==0): # Se o resto da divisão de i por j for 0 o programa soma todos os valores de j em somaA
      somaA = somaA + j
  
  somaB = 0 #somaB é a soma de todos os valores de k que dividem a somaA com resto 0
      
  for k in range(1, somaA): #loop que percorre todos divisiveis de somaA
    if (somaA%k==0): #se a somaA tiver resto 0 com a divisão por k soma em somaB tosos os valores de k
      somaB += k

  if (somaB == i and somaB != somaA): #se a somaB for igual ao contador até 10000 e for diferente da somaA, soma os valores de i para ser apresentado no final
    somaDiv += i  

print(somaDiv)
