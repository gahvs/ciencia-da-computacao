#include <stdio.h>
#include <stdlib.h>
#include"lista.h"
int main()
{
    List* myList = newList();

    append(myList, 10);
    append(myList, 20);
    append(myList, 30);

    print(myList);
    reverse(myList);
    print(myList);

    return 0;
}
