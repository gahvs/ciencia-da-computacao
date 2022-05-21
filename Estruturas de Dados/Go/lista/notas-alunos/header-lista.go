package main

import "fmt"

type nota struct {
	materia string
	pontos  float32
	next    *nota
}

type aluno struct {
	nome string
	head *nota
}

func criarAluno(nome string) *aluno {
	return &aluno{
		nome: nome,
	}
}

func (ctxAluno *aluno) adicionarNota(materia string, pontos float32) error {
	nota := &nota{
		materia: materia,
		pontos:  pontos,
	}

	if ctxAluno.head == nil {
		ctxAluno.head = nota
	} else {
		noAtual := ctxAluno.head

		for noAtual.next != nil {
			noAtual = noAtual.next
		}

		noAtual.next = nota

	}

	return nil

}

func (ctxAluno *aluno) mostrarNotasAluno() error {
	noAtual := ctxAluno.head

	if noAtual == nil {
		fmt.Printf("Não há notas registradas para o aluno %s\n\n", ctxAluno.nome)
		return nil
	}

	fmt.Printf("Notas - Aluno: %s\n", ctxAluno.nome)
	for noAtual != nil {
		fmt.Printf("%+v\n", *noAtual)
		noAtual = noAtual.next
	}
	return nil
}
