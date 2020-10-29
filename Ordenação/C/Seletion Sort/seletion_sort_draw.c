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
    printf("iterations: %d\n", iterations); //only presentation
    Sleep(280); //only presentation
}

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<len; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

int selecao(int array[])
{
    //Complexidade O(N^2) em todos os casos
    int i, g=0;
    for(i=0; i<len; i++, g++)
    {
        int min = i, temp, j;
        for(j=i+1; j<len; j++, g++)
            if(array[j] < array[min]) min = j;
        temp = array[i]; array[i] = array[min]; array[min] = temp;

        draw(array, g);system("cls");
    }
    return g;
}

int main()
{
    int array[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};
    int _[len] = {4, 2, 8, 5, 9, 1, 10, 3, 6, 7};

    int iter = selecao(array);
    draw(array, iter);
    printf("before: ");print(_);
    printf("after : ");print(array);
}
