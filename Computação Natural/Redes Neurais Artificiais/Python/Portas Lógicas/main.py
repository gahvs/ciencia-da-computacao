from neuralNetwork import NeuralNetwork
from random import randint

neural = NeuralNetwork(2, 3, 1, 0.1)
andInputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
andOutput = [0, 0, 0, 1]


def train():
    print('treinando...')
    while True:

        for i in range(10000):
            index = randint(0, 3)
            inp, out = andInputs[index], andOutput[index]
            neural.training(inp, [out])

        output1 = neural.feedforward([0, 0]).matrix[0][0]
        output2 = neural.feedforward([1, 1]).matrix[0][0]

        if output1 < 0.01 and output2 > 0.99:
            print('treinada')
            break

def main():

    train()
    while True:
        _b, __b = map(int, input().split(' '))

        if _b == - 1 and __b -1:
            break
        else:
            output = neural.feedforward([_b, __b]).matrix[0][0]
            print(output)
main()