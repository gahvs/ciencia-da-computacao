from VND import VND

vnd = VND(
    container_capacity= 500,
)

bestSolution = vnd.vndMethod(iterations=5000, neighborhoodSize=30)
print(vnd.calculateSolutionValue(bestSolution))
print(vnd.calculateSolutionVolume(bestSolution))