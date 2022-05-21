#include<stdio.h>

/*
Max-Min. Escreva uma fun��o recursiva que calcule a diferen�a entre o valor
de um elemento m�ximo e o valor de um elemento m�nimo do vetor v[0..n-1].
*/

int sub(int v[], int n )
{
    if(n == 1) return v[0];
    else
    {
        int x = sub(v, n-1);
        int a = sub(v, n-1);

        if(x > v[n-1] && a < v[n-1]) return x - a;
        if(x < v[n-1] && a > v[n-1]) return a - x;
        if(x > v[n-1] && a > v[n-1]) return x - v[n-1];
        if(x < v[n-1] && a < v[n-1]) return v[n-1] - x;
        printf("%d %d", x, a);
    }

}

int main()
{
    int n = 10;
    int v[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    printf("Max-Min: %d\n", sub(v, n));
}
