var training = true

function setup(){
    
    neural = new RedeNeural(2, 3, 1)
    
    dataset = 
    {
        inputs: 
        [
            [1, 1],
            [1, 0],
            [0, 1],
            [0, 0]
        ],
        outputs:
        [
                [0],
                [1],
                [1],
                [0]
        ]
    }    
}

function draw(){

    if(training)
    {
        for(let i = 0; i < 10000; i++)
        {
            var index = floor(random(4))
            neural.training(dataset.inputs[index], dataset.outputs[index])
        }
        if (neural.predict([0, 0])[0] < 0.01 && neural.predict([1, 0])[0] > 0.99)
        {
            training = false
            console.log('treinada')
        } else {
            console.log('training...')
        }
        
    }

}

function xor(bit_, bit__)
{
    operation = (arr) => {
        return arr[0] != arr[1] ? 1:0
    }
    let arr = [bit_, bit__]
    correctAnwser = operation(arr)
    
    neuralNetwordAnwser = neural.predict(arr)

    console.log(`Resposta correta: ${correctAnwser}`)
    console.log(`Resposta da rede: ${neuralNetwordAnwser}`)
}