package main

import "fmt"

type produto struct {
	desc     string
	preco    float64
	desconto float64
}

//Método: função com receiver

func (p produto) retornarPrecoComDesconto() float64 {
	return p.preco * (1 - p.desconto)
}

func main() {
	var produto_1 produto
	produto_1 = produto{
		desc:     "Lapis",
		preco:    0.99,
		desconto: 0.1,
	}

	fmt.Println(produto_1)
	fmt.Println(produto_1.retornarPrecoComDesconto())

	produto2 := produto{"Notebook Dell", 2499, 0.1}
	fmt.Println(produto2.retornarPrecoComDesconto())
}
