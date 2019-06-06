#include <stdio.h>
#include <stdlib.h>

int main(){
    int var=0, sequencia=0, resp=0, aux=0;
    for(int i=2; i<1000000; i++){
        var = i;
        while(var!=1){
            if(var%2==0){
                var = var/2;
            }
            else if(var%2!=0){
                var = (var*3)+1;
            }
            sequencia++;
        }
        if(sequencia>aux){
            resp = i;
        }
        aux = sequencia;
    }
    printf("%d", resp);
    return 0;
}
