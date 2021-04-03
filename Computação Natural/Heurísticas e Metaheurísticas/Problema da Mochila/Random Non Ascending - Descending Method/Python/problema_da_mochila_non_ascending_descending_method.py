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

Nesta solução, um vizinho aleatório da solução é analisado e o mesmo é aceito se for melhor ou 
igual a solução corrente e esse procedimento é interrompido após um número fixo, pré-definido, de 
iterações sem melhoria na solução.

Como a exploração não é feita em toda a vizinhança, não há garantias de que a solução final seja
um ótimo local.
"""
from random import randint
import random


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


def generateNeighborhood(solution):
    # generates the neighbors of the parameter solution
    # the neighborhood are solutions that differ 1bit from the current solution
    neighbors = []

    for i in range(len(solution)):
        neighbor = list(solution)  # in this function the solution is a tuple
        neighbor[i] = 1 if neighbor[i] == 0 else 0
        neighbors.append(neighbor)

    return neighbors


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


def uphill(initialSolution, capacity, iterMax):
    iter = 0
    currentSolution = initialSolution
    currentBenefit = calculateSolutionBenefit(initialSolution)

    neighborWeight = 0
    neighborBenefit = 0

    neighbors = generateNeighborhood(currentSolution)

    while iter < iterMax:
        iter = iter + 1

        neighbor = random.choice(neighbors)
        neighborWeight = calculateSolutionWeight(neighbor)
        neighborBenefit = calculateSolutionBenefit(neighbor)

        if neighborWeight < capacity:
            if neighborBenefit >= currentBenefit:
                iter = 0
                currentSolution = neighbor
                neighbors = generateNeighborhood(currentSolution)

    return currentSolution


def main():

    capacity = 35
    lenght = 12
    iterMax = 20

    initialSolution = generateValidInitialSolution(lenght, capacity)
    finalSolution = uphill(initialSolution, capacity, iterMax)

    print("\n\nProblema da Mochila - Non Ascending-Descending Method\n\n")

    print("Solução inicial  : ", initialSolution)
    print("Peso Inicial     : ", calculateSolutionWeight(initialSolution))
    print("Beneficio Inicial: ", calculateSolutionBenefit(
        initialSolution), end='\n\n')

    print("Solução Final    : ", finalSolution)
    print("Peso Final       : ", calculateSolutionWeight(finalSolution))
    print("Beneficio Final  : ", calculateSolutionBenefit(finalSolution))


main()
