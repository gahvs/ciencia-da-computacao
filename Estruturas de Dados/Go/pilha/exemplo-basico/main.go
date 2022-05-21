package main

import "fmt"

func main() {
	fmt.Printf("Main here.\n\n")

	myStack := createStack()

	myStack.push(10)
	myStack.push(20)
	myStack.push(30)
	myStack.push(40)

	myStack.pop()

	myStack.print()

}
