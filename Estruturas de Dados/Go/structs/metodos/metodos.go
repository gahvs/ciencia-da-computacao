package main

import (
	"fmt"
	"strings"
)

type pessoa struct {
	nome string
	sobrenome string
}

func (p pessoa) getNomeCompleto() string {
	return p.nome + " " + p.sobrenome
}

func (p *pessoa) setNomeCompleto(getNomeCompleto string) {
	partes := strings.Split(getNomeCompleto, " ")
	p.nome = partes[0]
	p.sobrenome = partes[1]
}

func main(){
	pessoa_1 := pessoa{"Gabrel", "Vinicíus"}
	fmt.Println(pessoa_1.getNomeCompleto())
	pessoa_1.setNomeCompleto("Gabriel Vinícius")
	fmt.Println(pessoa_1.getNomeCompleto())
}