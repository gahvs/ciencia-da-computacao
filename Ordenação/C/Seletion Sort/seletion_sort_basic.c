#include<stdio.h>
#define len 10

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<len; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

void selecao(int array[])
{
    //Complexidade O(N^2) em todos os casos
    int i;
    for(i=0; i<len; i++)
    {
        int min = i, temp, j;
        for(j=i+1; j<len; j++)
            if(array[j] < array[min]) min = j;
        temp = array[i]; array[i] = array[min]; array[min] = temp;

    }
}

int main()
{
    int array[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};
    int _[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};

    selecao(array);
    printf("before: ");print(_);
    printf("after : ");print(array);
}
