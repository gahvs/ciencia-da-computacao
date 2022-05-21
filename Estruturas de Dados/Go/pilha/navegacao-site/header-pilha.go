package main

import "fmt"

const len = 50

type urlStack struct {
	currentLen int
	array      [len]string
}

func createStack() *urlStack {
	return &urlStack{
		currentLen: 0,
	}
}

func (ctxStack *urlStack) push(url string) {
	if ctxStack.currentLen == len {
		fmt.Printf("Overflow.")
	}

	position := ctxStack.currentLen
	ctxStack.array[position] = url
	ctxStack.currentLen++
}

func (ctxStack *urlStack) pop() string {
	if ctxStack.currentLen == 0 {
		return ""
	}

	position := ctxStack.currentLen
	if position == len {
		position--
	}
	url := ctxStack.array[position]
	fmt.Println(ctxStack.array[position])
	ctxStack.currentLen--

	return url

}

func (ctxStack *urlStack) print() {
	if ctxStack.currentLen == 0 {
		return
	} else {
		fmt.Printf("Acessed pages:\n")
		for iter := ctxStack.currentLen - 1; iter >= 0; iter-- {
			fmt.Println(ctxStack.array[iter])
		}
	}
}
