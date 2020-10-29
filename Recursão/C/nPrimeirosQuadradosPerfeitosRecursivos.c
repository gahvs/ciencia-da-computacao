#include<stdio.h>
#define len 15

void squares(int array[], int n)
{
    if(n)
    {
        array[n-1] = n*n;
        squares(array, n-1);
    }
}

int main()
{
    //n = 5 => 1, 4, 9, 16, 25
    int array[len], i;
    squares(array, len);

    printf("primeiros %d quadrados perfeitos: \n", len);
    for(i=0; i<len; i++)
        printf("%d ", array[i]);

}
