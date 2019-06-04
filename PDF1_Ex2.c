#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=0, b=1, c=0, verif=1;
    int respa=0, respb=0, respc=0;
    for(a=1; a<1000; a++)
        for(b=a+1; b<1000; b++){
            c=1000-a-b;
            if(a*a+b*b==c*c){
                respa = a;
                respb = b;
                respc = c;
            }
        }
    printf("%d", respa*respb*respc);
    return 0;
}
