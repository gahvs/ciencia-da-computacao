#include<stdio.h>

//RETORNA O N-�SIMO N�MERO DA SEQU�NCIA DE FIBONACCI

int fib(int n)
{
    if(n <= 1)
        return 1;
    return fib(n-1) + fib(n-2);
}

int main()
{
    int n = 6;
    printf("fib(%d): %d\n", n, fib(n));
}
