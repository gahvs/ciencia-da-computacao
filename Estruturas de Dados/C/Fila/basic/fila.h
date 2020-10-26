#ifndef LISTA_H
#define LISTA_H

struct list {
    int value;
    struct list *next;
};
typedef struct list List;

struct queue {
    List*init;
    List*end;

};
typedef struct queue Queue;

Queue* newQueue();
int isEmpty(Queue* queue_);
void insert(Queue* queue_, int value);
int removeValue(Queue* queue_);
void show(Queue* queue_);

#endif
