#include<stdio.h>
#define len 10

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<len; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

void  insercao(int array[])
{
    //Complexidade O(N^2) no pior caso
    //Complexidade proporcional a N em casos em que o array já está "quase ordenado"
    int j;
    for(j=1; j<len; j++)
    {
        int x = array[j], i;
        for(i=j-1; (i>= 0 && array[i]>x); i--)
            array[i+1] = array[i];
        array[i+1] = x;
    }
}

int main()
{
    int array[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};
    int _[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};

    insercao(array);
    printf("before: ");print(_);
    printf("after : ");print(array);
}
