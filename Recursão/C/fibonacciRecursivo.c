#include<stdio.h>

//RETORNA O N-ÉSIMO NÚMERO DA SEQUÊNCIA DE FIBONACCI
//1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...
//1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12,  13,  14,  15,  16, , 17,   18, ...
int fib(int n)
{
    if(n >= 2)
        return (fib(n-1) + fib(n-2));
    return n;
}

int main()
{
    int n = 14;
    printf("fib(%d): %d\n", n, fib(n));
}
