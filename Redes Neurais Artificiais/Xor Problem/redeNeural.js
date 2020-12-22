function sigmoid(x)
{
    return 1 / ( 1 + Math.exp(-x) )
}

function dsigmoid(x)
{
    return x * (1-x)
}

class RedeNeural
{
    constructor(inputNodes, hiddenNodes, outputNodes) 
    {
        this.iNodes = inputNodes
        this.hNodes = hiddenNodes
        this.oNodes = outputNodes

        this.biasInputForHidden = new Matriz(this.hNodes, 1)
        this.biasHiddenForOutput = new Matriz(this.oNodes, 1)

        this.biasInputForHidden.randomize()
        this.biasHiddenForOutput.randomize()

        this.weightInputForHidden = new Matriz(this.hNodes, this.iNodes)
        this.weightHiddenForOutput = new Matriz(this.oNodes, this.hNodes)

        this.weightInputForHidden.randomize()
        this.weightHiddenForOutput.randomize()

        this.learningRate = 0.1
    }

    // feedforward(arrInput)
    // {
    //     //  ### Input for Hidden ###  //

    //     let input = Matriz.arrayToMatrix(arrInput)
    //     let hidden = Matriz.multiply(this.weightInputForHidden, input)
    //     hidden = Matriz.add(hidden, this.biasInputForHidden)
    //     hidden.map(sigmoid)

    //     //  ### Input for Hidden ###  //

        
    //     //  ### Hidden for Output ###  //

    //     let output = Matriz.multiply(this.weightHiddenForOutput, hidden)
    //     output = Matriz.add(output, this.biasHiddenForOutput)
    //     output.map(sigmoid)
    //     output.print()

    //     //  ### Hidden for Output ###  //

    // }

    training(arrInput, target)
    {
        // Feedforward

        let input = Matriz.arrayToMatrix(arrInput)
        let hidden = Matriz.multiply(this.weightInputForHidden, input)
        hidden = Matriz.add(hidden, this.biasInputForHidden)
        hidden.map(sigmoid)
        let output = Matriz.multiply(this.weightHiddenForOutput, hidden)
        output = Matriz.add(output, this.biasHiddenForOutput)
        output.map(sigmoid)

        // Backpropagation
        
        // Output -> Hidden
        let expected = Matriz.arrayToMatrix(target)
        let outputError = Matriz.subtract(expected, output)
        let derivateOutput = Matriz.map(output, dsigmoid)
        let hiddenTranspose = Matriz.transpose(hidden)
        
        let outputGradient = Matriz.hadamard(derivateOutput, outputError)
        outputGradient = Matriz.escalarMultiply(outputGradient, this.learningRate)

        // bias adjust
        this.biasHiddenForOutput = Matriz.add(this.biasHiddenForOutput, outputGradient)

        let deltaWeightsHiddenForOutput = Matriz.multiply(outputGradient, hiddenTranspose)
        this.weightHiddenForOutput = Matriz.add(this.weightHiddenForOutput, deltaWeightsHiddenForOutput)
        

        // Hidden -> Input
        let transposeWeightHO = Matriz.transpose(this.weightHiddenForOutput)
        let hiddenError = Matriz.multiply(transposeWeightHO, outputError)
        let derivateHidden = Matriz.map(hidden, dsigmoid)
        let inputTranspose = Matriz.transpose(input)

        let hiddenGradient = Matriz.hadamard(derivateHidden, hiddenError)
        hiddenGradient = Matriz.escalarMultiply(hiddenGradient, this.learningRate)

        // bias adjust
        this.biasInputForHidden = Matriz.add(this.biasInputForHidden, hiddenGradient)

        let deltaWeightsInputForHidden = Matriz.multiply(hiddenGradient, inputTranspose)
        this.weightInputForHidden = Matriz.add(this.weightInputForHidden, deltaWeightsInputForHidden)
    }

    predict(arrInput)
    {
        let input = Matriz.arrayToMatrix(arrInput)
        let hidden = Matriz.multiply(this.weightInputForHidden, input)
        hidden = Matriz.add(hidden, this.biasInputForHidden)
        hidden.map(sigmoid)

        let output = Matriz.multiply(this.weightHiddenForOutput, hidden)
        output = Matriz.add(output, this.biasHiddenForOutput)
        output.map(sigmoid)
        output = Matriz.matrizToArray(output)

        return output
    }

}