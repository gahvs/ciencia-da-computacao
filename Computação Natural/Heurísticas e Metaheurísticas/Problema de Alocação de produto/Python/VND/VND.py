from Neighborhood import Structures
from functools import reduce
from random import randint
from copy import deepcopy
from IO import IO

reduceAdder = lambda v, v_ : v + v_

class VND(Structures):

    def __init__(self, filename, container_capacity, vnd_method):
        self.__vnd_method = vnd_method
        self.__data = VND._loadData(filename)
        self.__container_capacity = container_capacity

    @classmethod
    def _loadData(cls, filename):
        io = IO()
        io.load(filename)
        return io.getData()

    def generateInitialSolution(self):
        solution = list()
        for p in self.__data:
            solution.append(
                randint(0, p['quantity'])
            )
        return solution
    
    def solutionIsFeasible(self, solution):
        pool = list(zip(solution, self.__data))
        volumes = [p[1]['size'] * p[0] for p in pool]
        total = reduce(reduceAdder, volumes)
        return self.__container_capacity > total

    def calculateSolutionVolume(self, solution):
        pool = list(zip(solution, self.__data))
        volumes = [p[1]['size'] * p[0] for p in pool]
        return reduce(reduceAdder, volumes)
    
    def calculateSolutionValue(self, solution):
        pool = list(zip(solution, self.__data))
        prices = [p[1]['price'] * p[0] for p in pool]
        return reduce(reduceAdder, prices)

    def firstImprovementMethod(self, currentSolution, neighborhood):
        currentValue = self.calculateSolutionValue(currentSolution)
        currentIsFeasible = self.solutionIsFeasible(currentSolution)

        for neighbor in neighborhood:
            neighborValue = self.calculateSolutionValue(neighbor)
            neighborIsFeasible = self.solutionIsFeasible(neighbor)

            if neighborValue > currentValue and neighborIsFeasible:
                return neighbor
            if neighborValue < currentValue and neighborIsFeasible and not currentIsFeasible:
                return neighbor
        
        return currentSolution
    
    def run(self, iterations, neighborhoodSize):
        if self.__vnd_method == 1: 
            return self.__vndMethod1(iterations, neighborhoodSize)
        else: 
            return self.__vndMethod2(iterations, neighborhoodSize)

    def __vndMethod1(self, iterations, neighborhoodSize):
        copy = iterations
        solution = self.generateInitialSolution()
        bestValue = self.calculateSolutionValue(solution)
        neighbor = list()

        print('Initial value:', bestValue)
        
        k = int()
        while iterations:

            if k == 0:
                neighborhood = [self.NS1(solution, 2) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)

            elif k == 1:
                neighborhood = [self.NS1(solution, 3) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)
                
            elif k == 2:
                neighborhood = [self.NS2(solution, self.__data, 2) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)
                
            elif k == 3:
                neighborhood = [self.NS2(solution, self.__data, 3) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)
                
            elif k == 4:
                neighborhood = [self.NS3(solution, self.__data, 3) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)
                
            elif k == 5:
                neighborhood = [self.NS3(solution, self.__data, 3) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)
                
            elif k == 6:
                neighborhood = [self.NS4(solution, self.__data, 3) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)
                
            elif k == 7:
                neighborhood = [self.NS4(solution, self.__data, 3) for _ in range(neighborhoodSize)]
                neighbor = self.firstImprovementMethod(solution, neighborhood)
                
            
            neighborValue = self.calculateSolutionValue(neighbor)
            neighborIsFeasible = self.solutionIsFeasible(neighbor)
            solutionIsFeasible = self.solutionIsFeasible(solution)

            if neighborValue > bestValue and neighborIsFeasible:
                solution = deepcopy(neighbor)
                bestValue = neighborValue
                iterations = copy
                k = 0
                print('improvement', bestValue)
            
            elif neighborValue < bestValue and neighborIsFeasible and not solutionIsFeasible:
                solution = deepcopy(neighbor)
                bestValue = neighborValue
                iterations = copy
                k = 0
                print('improvement', bestValue)
            
            else:
                k += 1
                iterations -= 1

        return solution
    
    def __vndMethod2(self, iterations, neighborhoodSize):
        copy = iterations
        solution = self.generateInitialSolution()
        bestValue = self.calculateSolutionValue(solution)
        neighbor = list()

        print('Initial value:', bestValue)
        
        k = int()
        while iterations:

            if k == 0:
                neighbor = self.NS1(solution, 2)

            elif k == 1:
                neighbor = self.NS1(solution, 3)
                
            elif k == 2:
                neighbor = self.NS2(solution, self.__data, 2)
                
            elif k == 3:
                neighbor = self.NS2(solution, self.__data, 3)
                
            elif k == 4:
                neighbor = self.NS3(solution, self.__data, 3)
                
            elif k == 5:
                neighbor = self.NS3(solution, self.__data, 3)
                
            elif k == 6:
                neighbor = self.NS4(solution, self.__data, 3)
                
            elif k == 7:
                neighbor = self.NS4(solution, self.__data, 3)
                
            
            neighborValue = self.calculateSolutionValue(neighbor)
            neighborIsFeasible = self.solutionIsFeasible(neighbor)
            solutionIsFeasible = self.solutionIsFeasible(solution)

            if neighborValue > bestValue and neighborIsFeasible:
                solution = deepcopy(neighbor)
                bestValue = neighborValue
                iterations = copy
                k = 0
                print('improvement', bestValue)
            
            elif neighborValue < bestValue and neighborIsFeasible and not solutionIsFeasible:
                solution = deepcopy(neighbor)
                bestValue = neighborValue
                iterations = copy
                k = 0
                print('improvement', bestValue)
            
            else:
                k += 1
                iterations -= 1

        return solution