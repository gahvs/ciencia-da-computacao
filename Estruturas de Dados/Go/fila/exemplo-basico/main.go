package main

import "fmt"

func main() {
	fmt.Printf("Main here.\n\n")

	queue := createQueue()

	queue.insert(10)
	queue.insert(20)
	queue.insert(30)

	queue.print()

	fmt.Printf("%d retired\n\n", queue.quit())

	queue.print()
}
