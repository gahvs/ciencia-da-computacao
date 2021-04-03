package main

import (
	"fmt"
	"math/rand"
	"time"
)

const (
	length     = 12
	capacity   = 35
	structures = 4
)

func detailSolution(solution [length]int) {
	fmt.Println("SOLUÇÃO  :", solution)
	fmt.Printf("PESO     : %d\n", calculateSolutionWeight(solution))
	fmt.Printf("BENEFÍCIO: %d\n\n", calculateSolutionBenefit(solution))
}

func getTwoDifferRandomValues(limit int) (int, int) {
	var value1, value2 int
	for true {
		value1 = rand.Intn(limit)
		value2 = rand.Intn(limit)
		if value1 != value2 {
			break
		}
	}
	return value1, value2
}

func changeBinaryValue(value int) int {
	if value == 1 {
		return 0
	} else {
		return 1
	}
}

func shuffle(array []int) []int {
	var randIndex, temp int
	copyArray := array

	for i := 3; i > 0; i-- {
		randIndex = rand.Intn(i)
		temp = copyArray[i]
		copyArray[i] = copyArray[randIndex]
		copyArray[randIndex] = temp
	}
	return copyArray
}

func generateValidInitialSolution() [length]int {

	var solution [length]int

	for true {
		for i := 0; i < length; i++ {
			solution[i] = rand.Intn(2)
		}
		if calculateSolutionWeight(solution) <= capacity {
			break
		}
	}

	return solution
}

func calculateSolutionWeight(solution [length]int) int {
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

func calculateSolutionBenefit(solution [length]int) int {
	benefits := [length]int{2, 2, 3, 4, 4, 2, 3, 4, 2, 1, 1, 2}
	var totalBenefits int
	for i, element := range solution {
		if element == 1 {
			totalBenefits += benefits[i]
		}
	}
	return totalBenefits
}

func neighborhoodStructure1(solution [length]int) [length][length]int {
	//this structure generates neighbors that differ 1 bit from the solution
	var neighborhood [length][length]int
	var neighbor [length]int

	for i := 0; i < length; i++ {
		neighbor = solution

		neighbor[i] = changeBinaryValue(neighbor[i])

		neighborhood[i] = neighbor
	}
	return neighborhood
}

func neighborhoodStructure2(solution [length]int) [length][length]int {
	// this structure generates neighbors by exchanging the value of a random
	// position with another position also random
	var neighborhood [length][length]int
	var neighbor [length]int

	for i := 0; i < length; i++ {
		neighbor = solution
		frst, scnd := getTwoDifferRandomValues(length)

		aux := neighbor[frst]
		neighbor[frst] = neighbor[scnd]
		neighbor[scnd] = aux

		neighborhood[i] = neighbor
	}

	return neighborhood
}

func neighborhoodStructure3(solution [length]int) [length][length]int {
	//this structure chooses two random positions and changes its value
	var neighborhood [length][length]int
	var neighbor [length]int

	for i := 0; i < length; i++ {
		neighbor = solution
		frst, scnd:= getTwoDifferRandomValues(length)

		neighbor[frst] = changeBinaryValue(neighbor[frst])
		neighbor[scnd] = changeBinaryValue(neighbor[scnd])

		neighborhood[i] = neighbor
	}

	return neighborhood
}

func neighborhoodStructure4(solution [length]int) [length][length]int {
	// this structure randomly chooses a range of 4 values ​​and shuffles them
	var neighborhood [length][length]int
	var neighbor [length]int

	for i := 0; i < length; i++ {
		neighbor = solution
		init, _ := getTwoDifferRandomValues(length - 4)
		end := init + 4

		shuffle(neighbor[init:end])
		neighborhood[i] = neighbor
	}

	return neighborhood
}

func generateNeighborhood(solution [length]int, structure int) [length][length]int {
	if structure == 1 {
		return neighborhoodStructure1(solution)
	} else if structure == 2 {
		return neighborhoodStructure2(solution)
	} else if structure == 3 {
		return neighborhoodStructure3(solution)
	} else {
		return neighborhoodStructure4(solution)
	}
}

func bestImprovementMethod(solution [length]int, structure int) [length]int {
	var bestNeighbor [length]int
	bestBenefit := 0
	neighborhood := generateNeighborhood(solution, structure)

	for _, neighbor := range neighborhood {
		neighborWeight := calculateSolutionWeight(neighbor)
		neighborBenefit := calculateSolutionBenefit(neighbor)

		if neighborWeight <= capacity && neighborBenefit > bestBenefit {
			bestNeighbor = neighbor
			bestBenefit = neighborBenefit
		}
	}
	return bestNeighbor
}

func vnd(initialSolution [length]int) [length]int {
	currentSolution := initialSolution
	bestBenefit := calculateSolutionBenefit(currentSolution)

	for currentStructure := 0; currentStructure < structures; currentStructure++ {
		bestNeighbor := bestImprovementMethod(currentSolution, currentStructure)
		bestNeighborBenefit := calculateSolutionBenefit(bestNeighbor)
		bestNeighborWeight := calculateSolutionWeight(bestNeighbor)

		if bestNeighborBenefit > bestBenefit && bestNeighborWeight <= capacity {
			currentSolution = bestNeighbor
			bestBenefit = bestNeighborBenefit
			currentStructure = 0
		} else {
			currentStructure++
		}
	}

	return currentSolution
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())

	initialSolution := generateValidInitialSolution()
	finalSolution := vnd(initialSolution)

	detailSolution(initialSolution)
	detailSolution(finalSolution)
}
