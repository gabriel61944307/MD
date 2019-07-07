termo = 2 #atribuindo termo=2 pois os dois primeiros termos da sequencia ja estão pré-definidos
fibonacci = [1, 1] #atribuindo o valor 1,1 na lista
while len(str(fibonacci[1]))<1000:#enquanto o tamanho dos caracteres da sequencia de fibonacci for men or que 1000
	termo = termo + 1 #continuando a contagem dos numeros ordinais que corresponde ao numero da sequencia de fibonacci
	fibonacci=[fibonacci[1], fibonacci[0]+fibonacci[1]] #calculando o proximo termo da sequencia de fibonacci

print (termo)#imprimindo o numero que corresponde ao numero que contem 1000 caracteres na sequencia de fibonacci
