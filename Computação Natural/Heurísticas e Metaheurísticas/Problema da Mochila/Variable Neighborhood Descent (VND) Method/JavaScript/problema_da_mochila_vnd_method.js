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

// Nesta solução, o espaço de soluções é explorado através de trocas determinísticas das estruturas de vizi-
// nhança, aceitando somente soluções estritamente melhores que a solução corrente e retornando à primeira 
// estrutura quando uma melhoria na solução é realizada.

const length = 12
const capacity = 35
const structures = 4

function generateValidInitialSolution() {
    while (true) {
        let copyLen = length
        let solution = []
        while (copyLen) {
            solution.push(Math.round(Math.random()))
            copyLen--
        }
        if (calculateSolutionWeight(solution) < capacity) {
            return solution
        }
    }
}

function getTwoDifferRandomValues(limit) {
    while (true) {
        let value1 = Math.round(Math.random() * limit)
        let value2 = Math.round(Math.random() * limit)

        if (value1 != value2) {
            return [value1, value2]
        }
    }
}

function shuffleArray(array) {
    let randomIndex = 0 
    let temp        = 0
    for (let i = array.length - 1; i > 0; i--) {
        randomIndex = Math.floor(Math.random() * (i + 1))
        temp = array[i]
        array[i] = array[randomIndex]
        array[randomIndex] = temp
    }
    return array
}

function insertShufledSlice(array, slice, init) {
    for (let iter = 0; iter < slice.length; iter++, init++) {
        array[init] = slice[iter]
    }
    return array
}

function neighborhoodStructure1(solution) {
    // this structure generates neighbors that differ 1 bit from the solution
    let neighbors = []
    for (let i = 0; i < length; i++) {
        neighbor = solution.slice()
        neighbor[i] = 1 ? neighbor[i] == 0 : 0
        neighbors.push(neighbor)
    }
    return neighbor
}

function neighborhoodStructure2(solution) {
    // this structure generates neighbors by exchanging the value of a random
    // position with another position also random
    let neighbors = []
    let iter = 0

    while (iter < length) {
        let neighbor = solution.slice()
        let indexes = getTwoDifferRandomValues(length - 1)

        let aux = neighbor[indexes[0]]
        neighbor[indexes[0]] = neighbor[indexes[1]]
        neighbor[indexes[1]] = aux

        if (neighbors.includes(neighbor)) {
            iter = iter - 1
        } else {
            neighbors.push(neighbor)
        }
        iter = iter + 1
    }

    return neighbors
}

function neighborhoodStructure3(solution) {
    // this structure chooses two random positions and changes its value
    let neighbors = []
    let iter = 0

    while (iter < length) {
        let neighbor = solution.slice()
        let indexes = getTwoDifferRandomValues(length - 1)
        let frst = indexes[0]
        let scnd = indexes[1]

        neighbor[frst] = 1 ? neighbor[frst] == 0 : 0
        neighbor[scnd] = 1 ? neighbor[scnd] == 0 : 0

        if (neighbors.includes(neighbor)) {
            iter = iter - 1
        } else {
            neighbors.push(neighbor)
        }
        iter = iter + 1
    }

    return neighbors
}

function neighborhoodStructure4(solution) {
    // this structure randomly chooses a range of 4 values ​​and shuffles them
    let neighbors = []
    let iter = 0

    while (iter < length) {
        let neighbor = solution.slice()
        let init = Math.round(Math.random() * length - 4)
        let end = init + 4

        let slice = neighbor.slice(init, end)
        neighbor = insertShufledSlice(neighbor.slice(), slice, init)

        if (neighbors.includes(neighbor)) {
            iter = iter - 1
        } else {
            neighbors.push(neighbor)
        }
        iter = iter + 1
    }

    return neighbors
}

function generateNeighborhood(solution, index) {
    const structures = [
        neighborhoodStructure1,
        neighborhoodStructure2,
        neighborhoodStructure3,
        neighborhoodStructure4
    ]
    return structures[index](solution)
}

function calculateSolutionWeight(solution) {
    const weights = [4, 5, 7, 9, 6, 3, 9, 1, 2, 9, 4, 5]
    let totalWeight = 0
    for (let i = 0; i < length; i++) {
        if (solution[i]) {
            totalWeight += weights[i]
        }
    }
    return totalWeight
}

function calculateSolutionBenefit(solution) {
    const benefits = [2, 2, 3, 4, 4, 2, 3, 4, 2, 1, 1, 2]
    let totalBenefit = 0
    for (let i = 0; i < length; i++) {
        if (solution[i]) {
            totalBenefit += benefits[i]
        }
    }
    return totalBenefit
}

function firstImprovementMethod(solution, currentStructure) {
    let currerntBenefit = calculateSolutionBenefit(solution)
    let neighbors = generateNeighborhood(solution, currentStructure)

    for (let i = 0; i < length; i++) {
        neighborWeight = calculateSolutionWeight(neighbors[i])
        neighborBenefit = calculateSolutionBenefit(neighbors[i])

        if (neighborWeight <= capacity && neighborBenefit > currerntBenefit) {
            return neighbors[i].slice()
        }
    }

    return solution.slice() //no improvement
}

function vnd(initialSolution) {
    let currentStructure = 0
    let currentSolution = initialSolution.slice()
    let currentBenefit = calculateSolutionBenefit(currentSolution)

    while (currentStructure < structures) {
        bestNeighbor = firstImprovementMethod(currentSolution, currentStructure)
        bestNeighborWeight = calculateSolutionWeight(bestNeighbor)
        bestNeighborBenefit = calculateSolutionBenefit(bestNeighbor)

        if (bestNeighborBenefit > currentBenefit) {
            if (bestNeighborWeight <= capacity) {
                currentBenefit  = bestNeighborBenefit
                currentSolution = bestNeighbor.slice()
                currentStructure = 0
            }
        } else {
            currentStructure = currentStructure + 1
        }
    }

    return currentSolution
}

function main() {
    initialSolution = generateValidInitialSolution()
    finalSolution = vnd(initialSolution)

    console.log("Problema da Mochila - Variable Neighborhood Descent Method\n\n")

    console.log("Solução inicial  : ", initialSolution)
    console.log("Peso Inicial     : ", calculateSolutionWeight(initialSolution))
    console.log("Beneficio Inicial: ", calculateSolutionBenefit(initialSolution))

    console.log("\n\nSolução Final    : ", finalSolution)
    console.log("Peso Final       : ", calculateSolutionWeight(finalSolution))
    console.log("Beneficio Final  : ", calculateSolutionBenefit(finalSolution))

}

main()