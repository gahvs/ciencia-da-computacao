#include <stdio.h>
#define MAXN 999999

int memo[MAXN];

//IMPLEMENTA��O INEFICIENTE:
//algoritmo exponencial
/* int fib(int n)
{
    if(n <= 1)
        return 1;
    return fib(n-1) + fib(n-2);
} */

//Implenta��o eficiente
//algoritmo linear (� poss�vel melhorar para logar�tmico)
int fib(int n)
{
    if(memo[n] == -1) memo[n] = fib(n-1) + fib(n-2);
    return memo[n];
}

int main()
{
    int i;
    for(i=0; i<MAXN; i++) memo[i] = -1; //flag para n�o calculado
    memo[0] = memo[1] = 1; //o que seria o caso base em uma recurs�o normal

    printf("%d\n", fib(6));
}
