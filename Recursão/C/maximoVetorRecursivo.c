#include<stdio.h>

//RETORNA O MÁXIMO DO VETOR (MAIOR ELEMENTO)

int max(int array[], int n)
{
    if (n == 1) return array[0];
    else
    {
        int x = max(array, n-1);
        if(x > array[n-1]) return x;
        else return array[n-1];
    }
}

int main()
{
    int array[] = {12, 32, 554, 54, 1239, 123254};
    int len = sizeof(array)/sizeof(array[0]);

    printf("maximo do vetor: %d\n", max(array, len));
}
