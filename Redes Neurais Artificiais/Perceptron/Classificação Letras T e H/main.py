from Perceptron import Perceptron
from linearalg.vector import Vector as v

entradas = (
    v(1, 1, 1, 0, 1, 0, 0, 1, 0), #T
    v(1, 0, 1, 1, 1, 1, 1, 0, 1), #H
)
saidas = (
    1, #T 
    0, #H
)


perceptron = Perceptron(taxa_aprendizagem=0.1, pesos=v(0, 0, 0, 0, 0, 0, 0, 0, 0), limiar=0.5)

while True:
    erros = []

    for i in range(len(entradas)):

        erro = perceptron.training(entrada=entradas[i], saida_esperada=saidas[i])
        erros.append(erro)
    
    if not any(erros):
        print('Treinamento Finalizado')
        break

print(perceptron.pesos.values())

while True:
    print(perceptron.feedforward(v(list(map(int, input().split(" "))))))
