#include<stdio.h>
#include<stdlib.h>
#define len 1000

void getData(int array[])
{
    char value[50];int i=0;
    FILE* arq;
    arq = fopen("binary_search_numbers.txt", "r");
    while(fscanf(arq, "%s", value) != EOF)
    {
        array[i++] = atoi(value);
    }
}

int sequential_search(int array[], int value)
{
    int i=0;
    while(array[i]!=value)
        i++;
    printf("Sequential Search iterations: %d\n", i);
    if(array[i] != i) return -1;
    return i;
}

int binary_search(int array[], int value)
{
    //l = left | r = right
    int l = -1, r = len, i=0;
    while(l < r-1)
    {
        int p = (l + r) / 2;
        if(array[p] < value) l = p;
        else r = p;
        i++;
    }
    printf("Binary Search Iterations: %d\n", i);
    if(value != array[r]) return -1; //this function returns the len of array or 0 if the elemente don't exists in the same, this if solve this;
    return r;
}

int main()
{
    int array[len], i;
    getData(array);

    int search = -2;
    int bIndex = binary_search(array, search);
    int sIndex = sequential_search(array, search);
    printf("\n\nIndex of %d: %d\n", search, bIndex);
}
