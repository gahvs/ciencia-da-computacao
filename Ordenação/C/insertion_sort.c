#include<stdio.h>
#include<windows.h>
#define len 10

void plot(int array[])
{
    int i, j;
    for(i=0; i<len; i++)
    {
        j=array[i];
        while(j--)
            printf("%c", 220);
        printf("\n");
    }
    printf("\n");
}

void draw(int array[], int iterations)
{
    plot(array); //only presentation
    printf("iteration: %d\n", iterations); //only presentation
    Sleep(280);system("cls"); //only presentation
}

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<len; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

int  insercao(int array[])
{
    //Complexidade O(N^2) no pior caso
    //Complexidade proporcional a N em casos em que o array já está "quase ordenado"
    int j, g=0;
    for(j=1; j<len; j++, g++)
    {
        int x = array[j], i;
        for(i=j-1; (i>= 0 && array[i]>x); i--, g++)
        {
            array[i+1] = array[i];

            draw(array, g);
        }
        array[i+1] = x;
    }
    return g;
}

int main()
{
    int array[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};
    int _[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};

    int iter = insercao(array);
    draw(array, iter);
    printf("before: ");print(_);
    printf("after : ");print(array);
}
