#include<stdio.h>

//CALCULA O FATORIAL DE N

int fat(int n)
{
    if(n)
        return n*fat(n-1);
    return 1;
}

int main()
{
    // 5! = 5 * 4 * 3 * 2 * 1 = 120
    int n = 5;
    printf("%d!: %d\n", n, fat(5));
}
