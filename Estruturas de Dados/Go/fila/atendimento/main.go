package main

import "fmt"

func main() {
	fmt.Printf("Main here\n\n")

	atendimentos := createQueue()

	atendimentos.insert("Gabriel Souto", "ADB723")
	atendimentos.insert("Clara Mendes", "DSD346")

	atendimentos.print()

	withdrew := atendimentos.quit()
	fmt.Printf("\n*** %s saiu da fila ***\n\n", withdrew.name)

	atendimentos.print()

	// fmt.Printf("\nTamanho da fila de Atendimentos: %d\n\n", atendimentos.len())
}
