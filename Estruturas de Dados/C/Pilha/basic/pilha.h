#ifndef PILHA_H_INCLUDED
#define PILHA_H_INCLUDED

#define len 50

struct stack {

    int length;
    int values[len];

};typedef struct stack Stack;

Stack *newStack();
void push(Stack *stack_, int value);
int pop(Stack *stack_);
int isEmpty(Stack *stack_);
int stackTop(Stack *stack_);
void show(Stack *stack_);
Stack *stackCopy(Stack *stackOrigin);
void stackCat(Stack *stackDestiny, Stack *stackOrigin); //concatenates two stacks
void stackReverse(Stack *stack_);

#endif // PILHA_H_INCLUDED
