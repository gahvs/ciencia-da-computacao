#include<stdio.h>
#include<stdlib.h>
#include"fila.h"

Queue* newQueue()
{
    Queue* queue_ = (Queue*)malloc(sizeof(Queue));
    queue_->init = queue_->end = NULL;
    return queue_;
}

int isEmpty(Queue* queue_)
{
    return queue_->init == NULL;
}

void insert(Queue* queue_, int value)
{
    List* node = (List*)malloc(sizeof(List));
    node->value = value;
    node->next = NULL;

    if(queue_->init != NULL)
    {
        queue_->end->next = node;
    }
    else
    {
        queue_->init = node;
    }
    queue_->end = node;
}

int removeValue(Queue* queue_)
{
    if(isEmpty(queue_))
    {
        printf("Fatal Error [EMPTY QUEUE]\n");
        exit(1);
    }
    int value = queue_->init->value;
    queue_->init = queue_->init->next;

    if(queue_->init == NULL)
        queue_->end = NULL;

    return value;
}

void show(Queue* queue_)
{
    List* node;
    printf("[ ");
    for(node = queue_->init; node != NULL; node = node->next)
    {
        if(node->next == NULL)
            printf("%d ", node->value);
        else
            printf("%d <- ", node->value);
    }
    printf("]\n");
}





