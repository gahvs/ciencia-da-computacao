from algebra.matrix import Matrix, MatrixComponent

matriz = Matrix()
matriz.add(component=MatrixComponent(row=1, col=1, number=1))
matriz.add(component=MatrixComponent(row=2, col=1, number=1))
matriz.add(component=MatrixComponent(row=3, col=1, number=1))
matriz.add(component=MatrixComponent(row=1, col=2, number=2))
matriz.add(component=MatrixComponent(row=1, col=3, number=3))
matriz.add(component=MatrixComponent(row=4, col=2, number=2))

restriction = matriz.numbers(rowPart=[4], colPart=",")

print(restriction)
print(matriz.matrix()[4])