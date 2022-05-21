#include<stdio.h>

//RECEBE DOIS VETORES E RETORNA TRUE SE ELES FOREM IGUALS E FALSE CASO CONTRÁRIO

int equal(int a[], int b[], int lenA, int lenB)
{
    lenA--, lenB--;
    if(lenA == 0 && lenB == 0)  return 1;
    else if(a[lenA] != b[lenB]) return 0;
    equal(a, b, lenA, lenB);
}

int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int b[] = {1, 2, 3, 4, 5, 0, 7, 8, 9, 10};
    int lenA = sizeof(a)/sizeof(a[0]);
    int lenB = sizeof(b)/sizeof(b[0]);


    if(equal(a, b, lenA, lenB)) printf("vetores iguais\n");
    else printf("vetores diferentes\n");
}
