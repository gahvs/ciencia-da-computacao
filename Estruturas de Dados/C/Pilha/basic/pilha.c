#include<stdio.h>
#include<stdlib.h>
#include "pilha.h"

Stack *newStack()
{
    Stack *stack_ = (Stack*)malloc(sizeof(Stack));
    stack_ -> length = 0;
    return stack_;
}

int isEmpty(Stack *stack_)
{
    return !stack_->length;
}

void push(Stack* stack_, int value)
{
    if(stack_ ->length < len)
    {
        stack_->values[stack_->length++] = value;
        return;
    }
    printf("stack overflow\n");
}

int pop(Stack *stack_)
{
    if(!isEmpty(stack_))
    {
        int value = stack_->values[stack_->length-1];
        stack_->length--;
        return value;
    }
}

Stack *stackCopy(Stack *stackOrigin)
{
    Stack *stackAux = newStack(); Stack *stackDestiny = newStack();

    while(!isEmpty(stackOrigin))
        push(stackAux, pop(stackOrigin));
    while(!isEmpty(stackAux))
    {
        int value = pop(stackAux);
        push(stackDestiny, value);
        push(stackOrigin, value);
    }
    free(stackAux);
    return stackDestiny;
}

void stackReverse(Stack *stack_)
{
    int stackAux[stack_->length], i = stack_->length;
    while(!isEmpty(stack_))
        stackAux[stack_->length] = pop(stack_);
    for(; i>0; i--)
        push(stack_, stackAux[i]);
}

void stackCat(Stack *stackDestiny, Stack *stackOrigin)
{
    Stack *stackAux = newStack();
    stackAux = stackCopy(stackOrigin);
    stackReverse(stackAux);
    while(!isEmpty(stackAux))
        push(stackDestiny, pop(stackAux));
}

int stackTop(Stack *stack_)
{
    int value = pop(stack_);
    push(stack_, value);
    return value;
}

void show(Stack *stack_)
{
    int i;
    for(i=stack_->length -1; i>=0; i--)
        printf(" %d\n", stack_->values[i]);
    printf(" \n\n");
}
