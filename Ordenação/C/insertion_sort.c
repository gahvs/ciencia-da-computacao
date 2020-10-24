#include<stdio.h>

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<10; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

void insercao(int array[])
{
    //Complexidade O(N^2) no pior caso
    //Complexidade proporcional a N em casos em que o array já está "quase ordenado"
    int j;
    for(j=1; j<10; j++)
    {
        print(array);
        int x = array[j], i;
        for(i=j-1; (i>= 0 && array[i]>x); i--)
            array[i+1] = array[i];
        array[i+1] = x;
    }
}

int main()
{
    int array[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}, i;
    insercao(array);
    print(array);
}
