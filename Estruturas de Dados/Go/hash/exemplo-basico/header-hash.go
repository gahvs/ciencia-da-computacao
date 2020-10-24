package main

const modulo = 17

type client struct {
	name  string
	cpf   string
	birth string
}

var hash [modulo]*client

func _hash_(key int) int {
	return key % modulo
}

func startHash(tab *client) {
	for i := 0; i < modulo; i++ {
		hash[i] = nil
	}
}

func showHash(tab *client) {
	var counter int
	for i := 0 ; i < modulo; i++ {
		if hash
	}
}