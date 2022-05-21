from Perceptron import Perceptron
from linearalg.vector import Vector as v

comprimentos = list(map(lambda v : (v - 80) / (130 -80), (100, 100, 100, 100, 102, 105, 107, 110, 114, 114, 116, 118)))
pesos = list(map(lambda v: (v - 15) / (15 - 45), (20, 26, 30, 32, 21, 22, 32, 35, 25, 24, 36, 27)))
entradas = list()

for c, p in zip(comprimentos, pesos):
    entradas.append(v(c, p))


saidas = (0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0)


perceptron = Perceptron(numero_entradas=2, taxa_aprendizagem=0.1, pesos=None, limiar=0.5)

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
    p, c = map(int, input().split(" "))
    p = (p - 80) / (130 -80)
    c = (c - 15) / (15 - 45)
    print(perceptron.feedforward(v(p, c)))
