#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"

int main()
{
    Stack *myStack = newStack();
    Stack *myNewStack = newStack();

    push(myStack, 10);
    push(myStack, 20);
    push(myStack, 30);

    push(myNewStack, 40);
    push(myNewStack, 50);
    push(myNewStack, 60);

    show(myStack);
    show(myNewStack);

    stackCat(myStack, myNewStack);


    show(myStack);


    free(myStack); free(myNewStack);
    return 0;
}
