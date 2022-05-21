package main

import "fmt"

const len = 2

type stack struct {
	currentLen int
	array      [len]int
}

func createStack() *stack {
	return &stack{
		currentLen: 0,
	}
}

func (ctxStack *stack) push(value int) {
	if ctxStack.currentLen == len {
		fmt.Printf("Failed push(%d): Overflow\n\n", value)
		return
	}

	position := ctxStack.currentLen
	ctxStack.array[position] = value
	ctxStack.currentLen++

}

func (ctxStack *stack) pop() int {
	if ctxStack.currentLen == 0 {
		fmt.Printf("Empty stack\n\n")
		return 0
	}
	position := ctxStack.currentLen
	if position == len {
		position--
	}
	value := ctxStack.array[position]
	ctxStack.currentLen--
	return value

}

func (ctxStack *stack) print() {
	if ctxStack.currentLen == 0 {
		return
	} else {
		fmt.Printf("Stack:\n\n")
		for iter := ctxStack.currentLen - 1; iter >= 0; iter-- {
			fmt.Printf("   %d\n", ctxStack.array[iter])
		}
		fmt.Println()
	}

}

func (ctxStack *stack) empty() bool {
	return ctxStack.currentLen == 0
}
