from VND import VND

vnd = VND(
    filename='produtos.csv',
    container_capacity=500,
    vnd_method=2
)

bestSolution = vnd.run(iterations=5000, neighborhoodSize=30)
print('\n\nBest Value:',vnd.calculateSolutionValue(bestSolution))
print('Volume:',vnd.calculateSolutionVolume(bestSolution))