#include <stdio.h>
#include <stdlib.h>
#include"fila.h"
int main()
{
    Queue* myQueue = newQueue();

    insert(myQueue, 10);
    insert(myQueue, 20);
    insert(myQueue, 30);

    show(myQueue);

    printf("%d\n", removeValue(myQueue));
    printf("%d\n", removeValue(myQueue));
    printf("%d\n", removeValue(myQueue));

    show(myQueue);

    return 0;
}
