'''
Cidade 1 2 3 4 5 6
   1   0 2 1 4 9 1
   2   2 0 5 9 7 2
   3   1 5 0 3 8 6
   4   4 9 3 0 2 5
   5   9 7 8 2 0 2
   6   1 2 6 5 2 0

   Problema com 6 cidades
   Exemplo de vetor solução -> (2, 5, 1, 3, 6, 4)
   2 -> 5 = 7
   5 -> 1 = 9
   1 -> 3 = 1
   3 -> 6 = 6
   6 -> 4 = 5
   4 -> 2 = 9
   custo total = 37
'''
import random
import copy


def detailSolution(solution, routeCosts):
    print("SOLUÇÃO: ", solution)
    print("CUSTO  : ", calculateCost(solution, routeCosts), end='\n\n')


def getTwoDifferRandomValues(init, end):
    while True:
        value1 = random.randint(init, end)
        value2 = random.randint(init, end)
        if value1 != value2:
            if value1 > value2:
                return value2, value1
            else:
                return value1, value2


def generateInitialSolution(cities):
    solution = []
    i = len(cities)

    while i:
        city = random.choice(cities)
        if city not in solution:
            solution.append(city)
            i -= 1

    solution.append(solution[0])
    return solution


def calculateCost(solution, routeCosts):
    cost = 0
    i = 1

    while i < len(solution):
        l, c = solution[i-1] - 1, solution[i] - 1
        cost += routeCosts[l][c]
        i += 1

    return cost


def neighborhoodStructure1(solution):
    #(start, #, #, #, #, #, end)#
    # this structure exchanges the values ​​of two different positions of the solution
    neighbor = list()
    neighborhood = list()
    iter = 0
    neighbors = 6

    while iter < neighbors:
        neighbor = copy.copy(solution)
        # the parameter is an interval (start, end)
        fst, snd = getTwoDifferRandomValues(1, 6)

        aux = neighbor[fst]
        neighbor[fst] = neighbor[snd]
        neighbor[snd] = aux

        neighborhood.append(neighbor)
        iter += 1

    return neighborhood


def neighborhoodStructure2(solution):
    # this structure defines a random interval of 3 numbers in the array and shuffle this interval
    neighbor = list()
    neighborhood = list()
    iter = 0
    neighbors = 6

    while iter < neighbors:
        neighbor = copy.copy(solution)
        init = random.randint(1, len(solution)-2)
        end = init + 3

        _slice = neighbor[init:end]
        random.shuffle(_slice)
        neighbor[init:end] = _slice

        neighborhood.append(neighbor)
        iter += 1

    return neighborhood


def generateNeighborhood(solution, i):
    structures = (neighborhoodStructure1, neighborhoodStructure2)
    return structures[i](solution)


def bestImprovementMethod(solution, structure, routeCosts):
    bestSolution = copy.copy(solution)
    bestCost     = calculateCost(solution, routeCosts)
    neighborhood = generateNeighborhood(solution, structure)

    for neighbor in neighborhood:
        neighborCost = calculateCost(neighbor, routeCosts)
        if neighborCost < bestCost:
            bestSolution = copy.copy(neighbor)
            bestCost = neighborCost

    return bestSolution


def vnd(initialSolution, structures, routeCosts):
    currentStrucure = 0
    bestSolution = copy.copy(initialSolution)
    bestCost = calculateCost(bestSolution, routeCosts)

    while currentStrucure < structures:
        bestNeighbor = bestImprovementMethod(
            bestSolution, currentStrucure, routeCosts)
        bestNeighborCost = calculateCost(bestNeighbor, routeCosts)

        if bestNeighborCost < bestCost:
            bestSolution = copy.copy(bestNeighbor)
            bestCost = bestNeighborCost
            currentStrucure = 0
        else:
            currentStrucure = currentStrucure + 1

    return bestSolution


def main():
    structures = 2
    cities = (1, 2, 3, 4, 5, 6)
    routeCosts = (
        (0, 2, 1, 4, 9, 1),
        (2, 0, 5, 9, 7, 2),
        (1, 5, 0, 3, 8, 6),
        (4, 9, 3, 0, 2, 5),
        (9, 7, 8, 2, 0, 2),
        (1, 2, 6, 5, 2, 0),
    )

    initialSolution = generateInitialSolution(cities)
    finalSolution = vnd(initialSolution, structures, routeCosts)

    detailSolution(initialSolution, routeCosts)
    detailSolution(finalSolution, routeCosts)


main()
