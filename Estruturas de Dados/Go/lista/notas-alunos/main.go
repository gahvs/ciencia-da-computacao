package main

import "fmt"

func main() {

	fmt.Printf("Main is here\n\n")

	aluno := criarAluno("Gabriel Vinicius")

	aluno.adicionarNota("Arquitetura de Computadores", 98.0)
	aluno.adicionarNota("Cálculo Diferencial e Integral", 62.0)

	aluno.mostrarNotasAluno()

}
