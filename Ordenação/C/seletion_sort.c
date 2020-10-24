#include<stdio.h>

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<10; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

void selecao(int array[])
{
    //Complexidade O(N^2) em todos os casos
    int i;
    for(i=0; i<10; i++)
    {
        print(array);
        int min = i, temp, j;
        for(j=i+1; j<10; j++)
            if(array[j] < array[min]) min = j;
        temp = array[i]; array[i] = array[min]; array[min] = temp;
    }
}

int main()
{
    int array[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}, i;
    selecao(array);
    print(array);
}
