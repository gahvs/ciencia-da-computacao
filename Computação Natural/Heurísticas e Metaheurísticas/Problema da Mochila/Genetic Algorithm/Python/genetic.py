from functools import reduce
from copy import copy
import random

populationLength = 50
individualLenght = 12
probMutation = 0.01
iterations = 100
capacity = 35

def getRandomSolution(individualLenght):
    return [random.randint(0, 1) for x in range(individualLenght)]

def getRandomPopulation(populationLength, individualLenght):
    population = []
    while populationLength:
        population.append(getRandomSolution(individualLenght))
        populationLength -= 1
    return population

def getRoll():
    roll = []
    mutation = int(probMutation * 100) 
    for i in range(mutation):
        roll.append(1)

    while len(roll) != 100:
        roll.append(0)
    return roll

def calculateIndividualWeight(solution):
    # calculates the total weight of the solution
    weights = (4, 5, 7, 9, 6, 3, 9, 1, 2, 9, 4, 5)
    totalWeight = 0
    for i in range(len(solution)):
        if solution[i]:
            totalWeight += weights[i]

    return totalWeight

def calculateIndividualBenefit(solution):
    # calculates the total benefit weight of the solution
    benefits = (2, 2, 3, 4, 4, 2, 3, 4, 2, 1, 1, 2)
    totalBenefit = 0

    for i in range(len(benefits)):
        if solution[i]:
            totalBenefit += benefits[i]

    return totalBenefit

def pushRandomMembers(nMembers, reprodutionMembers):
    while nMembers:
        member = random.randint(0, populationLength - 1)
        if not member in reprodutionMembers:
            reprodutionMembers.append(member)
            nMembers -= 1

def evaluation(population):
    rank = []
    for individual in population:
        weight = calculateIndividualWeight(individual)
        index = population.index(individual)
        if weight > capacity:
            benefit = calculateIndividualBenefit(individual)
            rank.append((-benefit, index))
        elif weight <= capacity:
            benefit = calculateIndividualBenefit(individual)
            rank.append((benefit, index))
    return rank # [ (value, member) ]

def getBestIndividuals(population, nIndividuals):
    ''' 10 best individuals '''
    getMember = lambda item: item[-1]
    populationRank = evaluation(population)
    populationRank.sort(key=lambda item: item[0] * -1)
    return list(map(getMember, populationRank[:nIndividuals]))

def crossover(reprodutionMembers):
    cut = int(individualLenght / 2)
    children = []
    while len(children) < 40:
        
        dad1 = random.choice(reprodutionMembers)
        reprodutionMembers.remove(dad1)
        dad2 = random.choice(reprodutionMembers)
        reprodutionMembers.remove(dad2)

        children.append(dad1[:cut] + dad2[cut:])
        children.append(dad1[cut:] + dad2[:cut])

    return children
  
def haveMutation():
    roll = getRoll()
    choiced = random.choice(roll)
    return True if choiced else False

def getRandomMemberAndIndex():
    member = random.randint(0, populationLength - 1)
    index = random.randint(0, individualLenght - 1)
    return member, index

def newGeneration(population):
    ''' 
        Population: 50 Members
        Elitism: 10 (20%)
        Crossover: 40 (80%)
    '''
    newPopulation = []
    reprodutionMembers = []
    elitismMembers = []

    membersForCrossover = getBestIndividuals(population, 30)
    pushRandomMembers(10, membersForCrossover)
    membersForElitism = getBestIndividuals(population, 10)

    for member in membersForCrossover:
        reprodutionMembers.append(population[member])

    for member in membersForElitism:
        elitismMembers.append(population[member])
    
    crossoverMembers = crossover(reprodutionMembers)

    newPopulation += elitismMembers
    newPopulation += crossoverMembers

    if haveMutation():
        member, index = getRandomMemberAndIndex()
        if newPopulation[member][index]:
            newPopulation[member][index] = 0
        else:
            newPopulation[member][index] = 1
    
    return newPopulation


def genetic():
    def adder(item1, item2): return item1 + item2
    def getValue(item): return item[0]

    withoutImprovement, generation = 0, 0
    population = getRandomPopulation(populationLength, individualLenght)

    while withoutImprovement < iterations:
        generation += 1
        newPopulation = newGeneration(population)

        populationRankValues = list(map(getValue, evaluation(population)))
        newPopulationRankValues = list(map(getValue, evaluation(newPopulation)))

        fitness1 = reduce(adder, populationRankValues)
        fitness2 = reduce(adder, newPopulationRankValues)
        print('1',fitness1)
        print('2',fitness2)
        if fitness2 >= fitness1:
            population = copy(newPopulation)
        else:
            withoutImprovement += 1

        # randMember = random.choice(population)
        # print('Membro aleatório '+str(generation)+'° geração: ', end='')
        # print(randMember, 'valor:', calculateIndividualBenefit(randMember))
    
    return population

def main():
    testIterations = 1000
    data = []

    while testIterations:

        bestSolution = genetic()
        bestSolution = max(bestSolution, key=lambda elem: calculateIndividualBenefit(elem))
        data.append((bestSolution, calculateIndividualBenefit(bestSolution)))
    
        testIterations -= 1

    bestSolution = max(data, key=lambda item: item[1])
    badSolution = min(data, key=lambda item: item[1])

    totalValue = 0
    for item in data:
        totalValue += item[-1]

    print('========= Resultados - Avaliação com 1000 iterações =========')
    print('    Melhor solução:', bestSolution[0], ', Valor:', bestSolution[-1])
    print('    Pior solução:', badSolution[0], ', Valor:', badSolution[-1])
    print('    Valor médio:', totalValue/ 1000)
    print(calculateIndividualWeight(bestSolution[0]))
    results = open('results.txt', 'w')
    results.write(str(bestSolution[0])+' '+str(bestSolution[1]))

main()
