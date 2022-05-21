#include<stdio.h>

//RETORNA A SOMA DOS ELEMENTOS DE UM VETOR

int sum(int array[], int n)
{
    if(n == 0) return array[0];
    return array[n] + sum(array, n-1);
}

int main()
{
    int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int len = sizeof(array)/sizeof(array[0]);
    printf("sum: %d\n", sum(array, len-1));
}
