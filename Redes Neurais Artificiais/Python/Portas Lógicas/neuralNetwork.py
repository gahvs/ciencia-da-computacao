from matrix import Matrix
from numpy import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

def dsigmoid(x):
    return x * (1 - x)

class NeuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        self.iNodes = inputNodes
        self.hNodes = hiddenNodes
        self.oNodes = outputNodes
        self.learningRate = learningRate

        self.biasInputToHidden = Matrix(hiddenNodes, 1)
        self.biasHiddenToOutput = Matrix(outputNodes, 1)
        self.weightsInputToHidden = Matrix(hiddenNodes, inputNodes)
        self.weightsHiddenToOutput = Matrix(outputNodes, hiddenNodes)

        self.biasInputToHidden.randomize()
        self.biasHiddenToOutput.randomize()
        self.weightsInputToHidden.randomize()
        self.weightsHiddenToOutput.randomize()

    def feedforward(self, arrInput):
        # Input -> Hidden
        input = Matrix.arrayToMatrix(arrInput)
        hidden = Matrix.multiply(self.weightsInputToHidden, input)
        hidden = Matrix.add(hidden, self.biasInputToHidden)
        hidden = Matrix.matrixMap(hidden, sigmoid)

        # Hidden -> Output
        output = Matrix.multiply(self.weightsHiddenToOutput, hidden)
        output = Matrix.add(self.biasHiddenToOutput, output)
        output = Matrix.matrixMap(output, sigmoid)

        return output

    def training(self, arrInput, target):
        input = Matrix.arrayToMatrix(arrInput)
        hidden = Matrix.multiply(self.weightsInputToHidden, input)
        hidden = Matrix.add(hidden, self.biasInputToHidden)
        hidden = Matrix.matrixMap(hidden, sigmoid)
        output = Matrix.multiply(self.weightsHiddenToOutput, hidden)
        output = Matrix.add(self.biasHiddenToOutput, output)
        output = Matrix.matrixMap(output, sigmoid)

        # Backpropagation

        # Output -> Hidden
        expected = Matrix.arrayToMatrix(target)
        outputError = Matrix.substract(expected, output)
        derivateOutput = Matrix.matrixMap(output, dsigmoid)
        hiddenTranspose = Matrix.transpose(hidden)

        outputGradient = Matrix.hadamard(derivateOutput, outputError)
        outputGradient = Matrix.escalarMult(outputGradient, self.learningRate)
        self.biasHiddenToOutput = Matrix.add(self.biasHiddenToOutput, outputGradient)

        deltaWeightsHiddenToOutput = Matrix.multiply(outputGradient, hiddenTranspose)
        self.weightsHiddenToOutput = Matrix.add(self.weightsHiddenToOutput, deltaWeightsHiddenToOutput)

        # Hidden -> Input
        transposeWeightHiddenToOutput = Matrix.transpose(self.weightsHiddenToOutput)
        hiddenError = Matrix.multiply(transposeWeightHiddenToOutput, outputError)
        derivateHidden = Matrix.matrixMap(hidden, dsigmoid)
        inputTranspose = Matrix.transpose(input)

        hiddenGradient = Matrix.hadamard(derivateHidden, hiddenError)
        hiddenGradient = Matrix.escalarMult(hiddenGradient, self.learningRate)

        self.biasInputToHidden = Matrix.add(self.biasInputToHidden, hiddenGradient)
        
        deltaWeightsInputForHidden = Matrix.multiply(hiddenGradient, inputTranspose)
        self.weightsInputToHidden = Matrix.add(self.weightsInputToHidden, deltaWeightsInputForHidden)