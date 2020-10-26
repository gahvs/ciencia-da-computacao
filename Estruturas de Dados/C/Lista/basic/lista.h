#ifndef LISTA_H
#define LISTA_H

struct node{
    int value;
    struct node* next;
};typedef struct node List;

List* newList();
void append(List* list, int value_);
List* copy(List* listOrigin);
void print(List* list);
void listcat(List* destiny, List*origin);
void reverse(List* list);
void remnode(List*list, int value_); //removes the node containing the parameter
int len(List* list);
int include(List* list, int value_);


#endif // LISTA_H
