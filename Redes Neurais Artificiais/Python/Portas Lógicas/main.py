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
    training = True
    if training:
        for i in range(10000):
            index = randint(0, 3)
            inp, out = andInputs[index], andOutput[index]
            neural.training(inp, [out])
        output1 = neural.feedforward([0, 0]).matrix[0][0]
        output2 = neural.feedforward([1, 1]).matrix[0][0]
        if output1 < 0.01 and output2 > 0.99:
            training = False
            print('treinada')
        
def main():
    train()


main()