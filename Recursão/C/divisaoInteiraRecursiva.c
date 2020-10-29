#include<stdio.h>

//RECEBE DOIS INTEIROS A E B COM A >= B E RETORNA A DIVISAO INTEIRA DE A POR B

int div(int a, int b)
{
    if(a<b) return 0;
    else return 1 + div(a-b, b);
}

int main()
{
    int a = 12;
    int b =  2;

    printf("%d / %d = %d\n", a, b, div(a, b));
}
