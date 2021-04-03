"""
Seja então uma mochila de capacidade b = 35 e os 12 objetos da tabela a seguir com os respectivos pesos e benefícios

Objeto (j)      1 2 3 4 5 6 7 8 9 10 11 12
Peso (wj)       4 5 7 9 6 3 9 1 2  9  4  5
Benefício (pj)  2 2 3 4 4 2 3 4 2  1  1  2 

buscaremos uma solução que possua maior beneficio sem ferir nenhuma restrição de integridade, neste caso, sem ultrapassar
a capacidade da mochila. Não é possível repetir os objetos.

Para o problema da mochila, representemos uma solução s por um vetor binário de n posições (0,0,1,1,1) e consideremos como 
movimento m a troca de valor de um bit. Assim, a vizinhança de uma solução s, e se escreve N(s), é o conjunto de todos os 
vizinhos s' que diferem de s pelo valor de um bit. Formalmente, representamos N(s) = {s' : s' ← s⊕m}, onde m siginifica a 
troca do valor de um bit. É necessário, agora, definir uma função de avaliação para guiar a busca no espaço de soluções do 
problema.

Nesta solução, o espaço de soluções é explorado através de trocas determinísticas das estruturas de vizi-
nhança, aceitando somente soluções estritamente melhores que a solução corrente e retornando à primeira 
estrutura quando uma melhoria na solução é realizada.
"""
from random import randint
import random
import copy


def generateValidInitialSolution(len, capacity):
    # Generates a random initial solution

    while True:
        copyLen = len
        solution = []
        while copyLen:
            solution.append(randint(0, 1))
            copyLen -= 1

        if calculateSolutionWeight(solution) <= capacity:
            return tuple(solution)


def getTwoDifferRandomValues(limit):
    while True:

        value1 = randint(0, limit)
        value2 = randint(0, limit)

        if value1 != value2:
            return value1, value2


def neighborhoodStructure1(solution):
    # this structure generates neighbors that differ 1 bit from the solution
    neighbors = []

    for i in range(len(solution)):
        neighbor = list(solution)
        neighbor[i] = 1 if neighbor[i] == 0 else 0
        neighbors.append(neighbor)

    return neighbors


def neighborhoodStructure2(solution):
    # this structure generates neighbors by exchanging the value of a random
    # position with another position also random
    neighbors = []
    iter = 0
    lenght = len(solution)

    while iter < lenght:
        iter = iter + 1
        neighbor = list(solution)
        first, second = getTwoDifferRandomValues(lenght - 1)

        aux = neighbor[first]
        neighbor[first] = neighbor[second]
        neighbor[second] = aux

        if neighbor in neighbors:
            # ignore the iteration because the neighbor already exists in the neighborhood
            iter = iter - 1
        else:
            # add the neighbor in the neighborhood because he doesn't exist in the same
            neighbors.append(neighbor)

    return neighbors


def neighborhoodStructure3(solution):
    # this structure chooses two random positions and changes its value
    neighbors = []
    iter = 0
    lenght = len(solution)

    while iter < lenght:
        iter = iter + 1
        neighbor = list(solution)
        first, second = getTwoDifferRandomValues(lenght - 1)

        neighbor[first] = 1 if neighbor[first] == 0 else 0
        neighbor[second] = 1 if neighbor[second] == 0 else 0

        if neighbor in neighbors:
            # ignore the iteration because the neighbor already exists in the neighborhood
            iter = iter - 1
        else:
            # add the neighbor in the neighborhood because he doesn't exist in the same
            neighbors.append(neighbor)

    return neighbors


def neighborhoodStructure4(solution):
    # this structure randomly chooses a range of 4 values ​​and shuffles them
    neighbors = []
    iter = 0
    lenght = len(solution)

    while iter < lenght:
        iter = iter + 1

        init = randint(0, len(solution) - 4)
        end = init + 4
        neighbor = list(solution)

        slice_ = neighbor[init:end]  # solution slice
        random.shuffle(slice_)      # shuffling
        neighbor[init:end] = slice_  # returning the shuffled slice to neighbor

        if neighbor in neighbors:
            # ignore the iteration because the neighbor already exists in the neighborhood
            iter = iter - 1
        else:
            # add the neighbor in the neighborhood because he doesn't exist in the same
            neighbors.append(neighbor)

    return neighbors


def generateNeighborhood(solution, index):
    structures = (
        neighborhoodStructure1,
        neighborhoodStructure2,
        neighborhoodStructure3,
        neighborhoodStructure4,
    )

    return structures[index](solution)


def calculateSolutionWeight(solution):
    # calculates the total weight of the solution
    weights = (4, 5, 7, 9, 6, 3, 9, 1, 2, 9, 4, 5)
    totalWeight = 0
    for i in range(len(solution)):
        if solution[i]:
            totalWeight += weights[i]

    return totalWeight


def calculateSolutionBenefit(solution):
    # calculates the total benefit weight of the solution
    benefits = (2, 2, 3, 4, 4, 2, 3, 4, 2, 1, 1, 2)
    totalBenefit = 0

    for i in range(len(benefits)):
        if solution[i]:
            totalBenefit += benefits[i]

    return totalBenefit


def firstImprovementMethod(solution, currentStructure, capacity):
    currentBenefit = calculateSolutionBenefit(solution)

    neighbors = generateNeighborhood(solution, currentStructure)
    for neighbor in neighbors:

        neighborWeight = calculateSolutionWeight(neighbor)
        neighborBenefit = calculateSolutionBenefit(neighbor)

        if neighborWeight <= capacity and neighborBenefit > currentBenefit:
            return neighbor
            
    return list(solution)


def vnd(initialSolution, capacity, iterMax, structures):
    currentStructure = 0

    currentSolution = copy.copy(initialSolution)
    currentBenefit = calculateSolutionBenefit(currentSolution)

    while currentStructure < structures:
        bestNeighbor = firstImprovementMethod(currentSolution, currentStructure, capacity)
        bestNeighborWeight = calculateSolutionWeight(bestNeighbor)
        bestNeighborBenefit = calculateSolutionBenefit(bestNeighbor)

        if bestNeighborBenefit > currentBenefit:
            if bestNeighborWeight <= capacity:
                currentBenefit = bestNeighborBenefit
                currentSolution = copy.copy(bestNeighbor)
                currentStructure = 0
        else:
            currentStructure = currentStructure + 1

    return currentSolution


def main():

    structures = 4
    capacity = 35
    lenght = 12
    iterMax = 20

    initialSolution = generateValidInitialSolution(lenght, capacity)
    finalSolution = vnd(initialSolution, capacity, iterMax, structures)

    print("\n\nProblema da Mochila - Variable Neighborhood Descent Method\n\n")

    print("Solução inicial  : ", initialSolution)
    print("Peso Inicial     : ", calculateSolutionWeight(initialSolution))
    print("Beneficio Inicial: ", calculateSolutionBenefit(
        initialSolution), end='\n\n')

    print("Solução Final    : ", finalSolution)
    print("Peso Final       : ", calculateSolutionWeight(finalSolution))
    print("Beneficio Final  : ", calculateSolutionBenefit(finalSolution))


main()
