# defina uma função que receba como argumento uma matriz de inteiros e retorna o indice da linha
# que a soma dos elementos é maior

def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma(lista[1:])

def sumLines(matrix):
    if len(matrix) == 1:
        return [soma(matrix[0])]
    else:
        return [soma(matrix[0])] + sumLines(matrix[1:])

def maxValue(sumMatrix):
    if len(sumMatrix) == 1:
        return sumMatrix[0]
    else:
        currentValue = sumMatrix[0]
        return currentValue if currentValue > maxValue(sumMatrix[1:]) else maxValue(sumMatrix[1:])

def func(matrix):

    sumMatrix = sumLines(matrix)
    maxValue_ = maxValue(sumMatrix)

    return sumMatrix.index(maxValue_)


matrix = [[1, 2, 3], [11, 11, 11], [6, 7, 8], [10, 11, 12]]

print(func(matrix))