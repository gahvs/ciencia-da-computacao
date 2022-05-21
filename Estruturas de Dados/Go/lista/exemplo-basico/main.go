package main

import "fmt"

func main() {

	fmt.Printf("Main is here.\n\n")

	myList := createList()

	myList.append(10)
	myList.append(20)
	myList.append(30)
	myList.append(40)
	myList.append(50)
	myList.append(60)
	myList.append(70)

	myList.print()
	myList.len()

	myList.delete(10)
	myList.print()
	myList.delete(30)
	myList.print()
	myList.delete(70)
	myList.print()

	myList.len()

}
