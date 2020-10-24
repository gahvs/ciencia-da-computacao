// Seja então uma mochila de capacidade b = 35 e os 12 objetos da tabela a seguir com os respectivos pesos e benefícios
// Objeto (j)      1 2 3 4 5 6 7 8 9 10 11 12
// Peso (wj)       4 5 7 9 6 3 9 1 2  9  4  5
// Benefício (pj)  2 2 3 4 4 2 3 4 2  1  1  2
// buscaremos uma solução que possua maior beneficio sem ferir nenhuma restrição de integridade, neste caso, sem ultrapassar
// a capacidade da mochila. Não é possível repetir os objetos.
// Para o problema da mochila, representemos uma solução s por um vetor binário de n posições (0,0,1,1,1) e consideremos como
// movimento m a troca de valor de um bit. Assim, a vizinhança de uma solução s, e se escreve N(s), é o conjunto de todos os
// vizinhos s' que diferem de s pelo valor de um bit. Formalmente, representamos N(s) = {s' : s' ← s⊕m}, onde m siginifica a
// troca do valor de um bit. É necessário, agora, definir uma função de avaliação para guiar a busca no espaço de soluções do
// problema.
// Nesta solução, quando um vizinho que possui benefício menor que a solução corrente é encontrado, o algoritmo para e retorna
// a solução corrente, assumindo que a mesma é um ótimo local.

package main

import (
	"fmt"
	"math/rand"
	"time"
)

const (
	length   = 12
	capacity = 35
)

func generateValidInitialSolution() [length]int {
	// Generates a random initial solution
	var solution [length]int
	for true {
		for iter := 0; iter < length; iter++ {
			solution[iter] = rand.Intn(2)
		}
		if calculateSolutionWeight(solution) <= capacity {
			break
		}
	}
	return solution
}

func generateNeighborhood(solution [length]int) [length][length]int {
	// generates the neighbors of the parameter solution
	// the neighborhood are solutions that differ 1bit from the current solution
	var neighbors [length][length]int

	for i := 0; i < length; i++ {

		neighbor := solution

		if neighbor[i] == 1 { //exchange a value at the neighbor
			neighbor[i] = 0
		} else {
			neighbor[i] = 1
		}

		if calculateSolutionWeight(neighbor) <= capacity {
			neighbors[i] = neighbor
		} else {
			i--
		}
	}
	return neighbors
}

func calculateSolutionWeight(solution [12]int) int {
	//calculates the total weight of the solution
	weights := [length]int{4, 5, 7, 9, 6, 3, 9, 1, 2, 9, 4, 5}
	var totalWeight int
	for i, element := range solution {
		if element == 1 {
			totalWeight += weights[i]
		}
	}
	return totalWeight
}

func calculateSolutionBenefit(solution [12]int) int {
	benefits := [length]int{2, 2, 3, 4, 4, 2, 3, 4, 2, 1, 1, 2}
	var totalBenefits int
	for i, element := range solution {
		if element == 1 {
			totalBenefits += benefits[i]
		}
	}
	return totalBenefits
}

func uphill(initialSolution [length]int) [length]int {
	currentSolution := initialSolution
	currentBenefit := calculateSolutionBenefit(initialSolution)

	for true {
		neighbors := generateNeighborhood(currentSolution)

		for _, neighbor := range neighbors {

			neighborBenefit := calculateSolutionBenefit(neighbor)

			if neighborBenefit < currentBenefit {
				return currentSolution
			}

			if neighborBenefit > currentBenefit {
				currentBenefit = neighborBenefit
				currentSolution = neighbor
			}
		}

	}
	return currentSolution
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())

	initialSolution := generateValidInitialSolution()
	finalSolution := uphill(initialSolution)

	fmt.Printf("\n\nProblema da Mochila - Descent-Uphill Method\n\n")
	fmt.Println("Solução inicial   : ", initialSolution)
	fmt.Println("Peso inicial      : ", calculateSolutionWeight(initialSolution))
	fmt.Println("Benefício inicial : ", calculateSolutionBenefit(initialSolution))

	fmt.Println("\n\nSolução final   : ", finalSolution)
	fmt.Println("Peso final      : ", calculateSolutionWeight(initialSolution))
	fmt.Println("Benefício final : ", calculateSolutionBenefit(finalSolution))
}
