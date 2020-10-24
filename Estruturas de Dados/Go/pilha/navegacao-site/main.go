package main

import "fmt"

func main() {
	fmt.Printf("Main here.\n\n")

	siteStack := createStack()

	siteStack.push("lmway.com")
	siteStack.push("lmway.com/users")
	siteStack.push("lmway.com/users/3")

	// currentPage := 
	siteStack.pop()
	// fmt.Printf("Current page: %s\n\n", currentPage)

	siteStack.print()

}
