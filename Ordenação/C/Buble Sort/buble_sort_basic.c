#include<stdio.h>
#define len 10

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<len; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

int buble_sort(int array[])
{
    //O(n) no melhor caso
    //O(n^2) no pior caso
    int i, j, swap = 1, aux;
    for(i=len-1; i>=0 && swap; i--)
    {
        swap = 0;
        for(j=0; j<i; j++)
            if(array[j] > array[j+1])
                aux = array[j], array[j] = array[j+1], array[j+1] = aux, swap = 1;
    }
}

int main()
{
    int array[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};
    int _[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};

    buble_sort(array);
    printf("before: ");print(_);
    printf("after : ");print(array);
}


