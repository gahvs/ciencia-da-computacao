#include<stdio.h>
#define len 11

void print(int array[])
{
    int i;printf("[ ");
    for(i=0; i<len; i++)
        printf("%d ", array[i]);
    printf("]\n");
}

void reverse(int array[], int s, int e)
{
    //s = start | e = end
    if(s < e)
    {
        int temp = array[s];
        array[s] = array[e], array[e] = temp, s++, e--;
        reverse(array, s, e);
    }
}

int main()
{
    int array[] = {3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4};
    print(array);
    reverse(array, 0, len-1);
    print(array);
}
