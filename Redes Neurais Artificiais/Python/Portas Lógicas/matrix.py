from random import random
from functools import reduce

class Matrix:

    def __init__(self, rows, cols):
        def row(cols): return [0 for x in range(cols)]
        self.rows = rows
        self.cols = cols
        self.matrix = [row(cols) for _ in range(rows)]

    def print(self):
        for row in self.matrix:
            print(row)
        print()

    def randomize(self):
        def rowMap(row): return [random() for _ in range(self.cols)]
        self.matrix = list(map(rowMap, self.matrix))

    @staticmethod
    def matrixToArray(matrix):
        arr = []
        for row in matrix.matrix:
            arr += [e for e in row]
        return arr

    @staticmethod
    def arrayToMatrix(arr):
        matrix = Matrix(len(arr), 1)
        for i in range(len(arr)):
            matrix.matrix[i][0] = arr[i]
        return matrix

    @staticmethod
    def matrixMap(matrixA, function):
        def mapRow(row): return list(map(function, row))
        result = Matrix(matrixA.rows, matrixA.cols)
        result.matrix = list(map(mapRow, matrixA.matrix))
        return result
    
    @staticmethod
    def transpose(matrix):
        transpose = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                transpose.matrix[j][i] = matrix.matrix[i][j]
        return transpose

    @staticmethod
    def add(matrixA, matrixB):
        result = Matrix(matrixA.rows, matrixB.cols)
        for i in range(matrixA.rows):
            for j in range(matrixB.cols):
                result.matrix[i][j] = matrixA.matrix[i][j] + matrixB.matrix[i][j]
        return result
    
    @staticmethod
    def substract(matrixA, matrixB):
        result = Matrix(matrixA.rows, matrixB.cols)
        for i in range(matrixA.rows):
            for j in range(matrixB.cols):
                result.matrix[i][j] = matrixA.matrix[i][j] - matrixB.matrix[i][j]
        return result

    @staticmethod
    def hadamard(matrixA, matrixB):
        result = Matrix(matrixA.rows, matrixB.cols)
        for i in range(matrixA.rows):
            for j in range(matrixB.cols):
                result.matrix[i][j] = matrixA[i][j] * matrixB[i][j]
        return result
    
    @staticmethod
    def escalarMult(matrixA, escalar):
        def rowMap(row): return list(map(lambda e: e * escalar, row))
        result = Matrix(matrixA.rows, matrixA.cols)
        result.matrix = list(map(rowMap, matrixA.matrix))
        return result

    @staticmethod
    def multiply(matrixA, matrixB):
        def getColumn(matrix, col):return [matrix.matrix[i][col] for i in range(matrix.rows)]
        def acc(_e, __e): return _e + __e
        result = Matrix(matrixA.rows, matrixB.cols)

        for row in matrixA.matrix:
            k = matrixA.matrix.index(row)
            for i in range(matrixB.cols):
                col = getColumn(matrixB, i)
                mults = [a * b for a, b in zip(row, col)]
                result.matrix[k][i] = reduce(acc, mults)
        return result