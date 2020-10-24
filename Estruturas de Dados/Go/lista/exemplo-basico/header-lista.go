package main

import "fmt"

type node struct {
	value int
	next  *node
}

func createList() *node {
	return &node{
		next: nil,
	}
}

func (ctxNode *node) append(value int) {
	node := &node{
		value: value,
	}

	for ctxNode.next != nil {
		ctxNode = ctxNode.next
	}

	ctxNode.next = node

}

func (ctxNode *node) print() {

	for iterNode := ctxNode.next; iterNode != nil; iterNode = iterNode.next {
		fmt.Printf("%d => ", iterNode.value)
	}
	fmt.Printf("nil\n\n")
}

func (ctxNode *node) len() {
	var counter int

	for iterNode := ctxNode.next; iterNode != nil; iterNode = iterNode.next {
		counter++
	}

	fmt.Printf("The list size is: %d\n\n", counter)

}

func (ctxNode *node) delete(valueToDelete int) error {
	var prev *node

	for ; ctxNode != nil; ctxNode = ctxNode.next {
		if ctxNode.value == valueToDelete {
			break
		}
		prev = ctxNode
	}
	if ctxNode != nil {
		if prev == nil {
			ctxNode = ctxNode.next
		} else {
			prev.next = ctxNode.next
		}
		fmt.Printf("The value %d has been deleted from list\n\n", valueToDelete)
		return nil
	}
	fmt.Printf("The list not contains the parameter value (%d)\n\n", valueToDelete)
	return nil
}
