package main

import "fmt"

type people struct {
	name     string
	protocol string
	next     *people
}

type queue struct {
	init *people
	end  *people
}

func createQueue() *queue {
	return &queue{
		init: nil,
		end:  nil,
	}
}

func (ctxQueue *queue) insert(name_, protocol_ string) {
	people := &people{
		name:     name_,
		protocol: protocol_,
		next:     nil,
	}

	if ctxQueue.init != nil {
		ctxQueue.end.next = people
	} else {
		ctxQueue.init = people
	}

	ctxQueue.end = people

}

func (ctxQueue *queue) quit() people {
	var retiredPeople people

	if ctxQueue.empty() {
		fmt.Printf("Empty Queue\n\n")
		return people{name: "", protocol: ""}
	}

	retiredPeople.name = ctxQueue.init.name
	retiredPeople.protocol = ctxQueue.init.protocol
	ctxQueue.init = ctxQueue.init.next

	if ctxQueue.init == nil {
		ctxQueue.end = nil
	}

	return retiredPeople

}

func (ctxQueue *queue) print() {
	counter := 1
	fmt.Printf("Fila de Atendimentos: \n\n")
	for iter := ctxQueue.init; iter != nil; iter = iter.next {
		fmt.Printf("	%d) Name: %s - Protocol: %s  \n", counter, iter.name, iter.protocol)
		counter++
	}
	fmt.Printf("\n")
}

func (ctxQueue *queue) len() int {
	counter := 0
	for iter := ctxQueue.init; iter != nil; iter = iter.next {
		counter++
	}
	return counter
}

func (ctxQueue *queue) empty() bool {
	return ctxQueue.init == nil
}
