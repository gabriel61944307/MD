#include<stdio.h>

int main(){
	int soma = 0, qtddivisores = 0, cont = 0, divisor = 1;
	while(qtddivisores<=500){
		qtddivisores = 1; //Todo número é divisivel por si próprio.
		divisor = 1;
		cont++;
		soma = soma + cont;           //Soma dos números naturais.
		while(divisor<=(soma/2)+1){   //Vai até a metade da soma pois o maior numero que divide um
			if(soma%divisor==0){        //número qualquer sem ser ele mesmo é a sua metade
				qtddivisores++;
			}
			divisor++;
		}
	}
	printf("%d\n", soma);
	return 0;
}
