package main

import "fmt"

type list struct {
	value int
	next  *list
}

type queue struct {
	init *list
	end  *list
}

func createQueue() *queue {
	return &queue{
		init: nil,
		end:  nil,
	}
}

func (ctxQueue *queue) insert(value_ int) {
	dude := &list{
		value: value_,
		next:  nil,
	}

	if ctxQueue.init != nil {
		ctxQueue.end.next = dude
	} else {
		ctxQueue.init = dude
	}

	ctxQueue.end = dude
}

func (ctxQueue *queue) quit() int {
	var retiredNumber int

	if ctxQueue.empty() {
		fmt.Printf("Empty Queue.\n\n")
		return 0
	}

	retiredNumber = ctxQueue.init.value
	ctxQueue.init = ctxQueue.init.next

	if ctxQueue.init == nil {
		ctxQueue.end = nil
	}

	return retiredNumber

}

func (ctxQueue *queue) print() {
	fmt.Printf("init < ")
	for iter := ctxQueue.init; iter != nil; iter = iter.next {
		fmt.Printf("%d < ", iter.value)
	}
	fmt.Printf("end\n\n")
}

func (ctxQueue *queue) empty() bool {
	return ctxQueue.init == nil
}
