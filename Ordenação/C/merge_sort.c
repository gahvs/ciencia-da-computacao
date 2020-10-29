#include<stdio.h>
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

void draw(int array[])
{
    plot(array); //only presentation
    Sleep(280); //only presentation
}

void print(int array[])
{
    int i;printf("[ ");
    for(i=0;i<len;i++) printf("%d ", array[i]);
    printf("]\n");
}

void merge(int s, int m, int e, int array[])
{
    //s = start | m = middle | e = end
    int *aux;
    int i = s, j = m, k = 0;
    aux = malloc((e - s) * sizeof(int));
    while(i < m && j < e)
    {
        if(array[i] <= array[j]) aux[k++] = array[i++];
        else aux[k++] = array[j++];
        draw(array);system("cls"); //only presentation
    }
    while(i < m)
    {
        aux[k++] = array[i++];
        draw(array);system("cls"); //only presentation
    }
    while(j < e)
    {
        aux[k++] = array[j++];
        draw(array);system("cls"); //only presentation
    }
    for(i=s; i<e; i++)
    {
        array[i] = aux[i-s];
        draw(array);system("cls"); //only presentation
    }
    free(aux);
}

void mergesort(int s, int e, int array[])
{
    //s = start | e = end
    if(s < e-1)
    {
        draw(array);system("cls");
        int q = (s + e)/2;
        mergesort(s, q, array);
        mergesort(q, e, array);
        merge(s, q, e, array);
    }
}

int main()
{
    //Para rearranjar em ordem crescente um vetor v[0..n-1] basta executar mergesort (0, n, v)
    int array[10] = {7, 3, 9, 2, 1, 10, 4, 6, 8, 5};
    int _[10] = {7, 3, 9, 2, 1, 10, 4, 6, 8, 5};
    mergesort(0, 10, array);
    draw(array);
    printf("before: ");print(_);
    printf("after : ");print(array);
}
