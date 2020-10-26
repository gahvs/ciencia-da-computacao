#include<stdio.h>
#include<stdlib.h>
#include"lista.h"

List* newList()
{
    List* list = (List*)malloc(sizeof(List));
    list->next = NULL;
    return list;
}

void append(List* list, int value_)
{
    List* newNode = (List*)malloc(sizeof(List));

    newNode->value = value_;
    newNode->next = list->next;
    list->next = newNode;
}

int len(List* list)
{
    int len;List*node;
    for(node=list->next, len=0; node!=NULL; node=node->next, len++){    }
    return len;
}

int include(List*list, int value_)
{
    List*node;
    for(node=list->next; node!=NULL; node=node->next)
        if(node->value == value_)
            return 1;
    return 0;
}

void listcat(List* destiny, List* origin)
{
    List*node;
    for(node=origin->next; node!=NULL; node=node->next)
        append(destiny, node->value);
}

void remnode(List*list, int value_)
{
    List*prev_node = list;
    List* aux = list->next;

    while(aux != NULL && aux->value != value_)
        prev_node = aux, aux = aux->next;

    if(aux != NULL)
        prev_node->next = aux->next;

    free(aux);
}

void print(List* list)
{
    List*node;printf("[ ");
    for(node = list->next; node != NULL; node = node->next)
    {
        if(node->next != NULL)
            printf("%d <- ", node->value);
        else
            printf("%d ", node->value);
    }printf("]\n");
}
