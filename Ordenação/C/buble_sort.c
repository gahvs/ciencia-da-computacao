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

int buble_sort(int array[])
{
    //O(n) no melhor caso
    //O(n^2) no pior caso
    int i, j, swap = 1, aux, g=0;
    for(i=len-1; i>=0 && swap; i--, g++)
    {
        swap = 0;
        for(j=0; j<i; j++, g++)
        {
            if(array[j] > array[j+1])
            {
                aux = array[j], array[j] = array[j+1], array[j+1] = aux, swap = 1;
            }
            draw(array, g);
        }
    }
    return g; //returns iterations only presentation
}

int main()
{
    int array[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};
    int _[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};

    int iter = buble_sort(array);
    draw(array, iter);
    printf("before: ");print(_);
    printf("after : ");print(array);
}


