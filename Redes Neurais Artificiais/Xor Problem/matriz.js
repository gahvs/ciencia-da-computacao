class Matriz {
    constructor(rows, cols) {
        this.rows = rows
        this.cols = cols

        this.matriz = []
        for (let r = 0; r < rows; r++) {
            let arr = []
            for (let c = 0; c < cols; c++) {
                arr.push(0)
            }
            this.matriz.push(arr)
        }
    }

    static matrizToArray(A)
    { 
        let arr = []
        A.map((elm, i, j) => {
            arr.push(elm)
        })
        return arr
    }

    static arrayToMatrix(arr)
    {   
        let matriz = new Matriz(arr.length, 1)
        matriz.map((e, i, j) =>{
            return arr[i]
        })
        return matriz
    }

    print()
    {
        console.table(this.matriz)
    }

    randomize() 
    {
        this.map((e, i, j) =>{
            return Math.random() * 2 - 1 
        })
    }

    static transpose(A)
    {   
        let matriz = new Matriz(A.cols, A.rows)
        matriz.map((e, i, j) =>{
            return A.matriz[j][i]
        })
        return matriz
    }

    static map(A, func) {

        let resultado = new Matriz(A.rows, A.cols)

        resultado.matriz = A.matriz.map((arr, i) => {
            return arr.map((e, j) => {
                return func(e, i, j)
            })
        })
        return resultado
    }

    map(func)
    {
        this.matriz = this.matriz.map((arr, i) => {
            return arr.map((e, j) => {
                return func(e, i, j)
            })
        })
        return this
    }

    static add(A, B)
    {
        let resultado = new Matriz(A.rows, A.cols)
        resultado.map((e, row, col) => {
            return A.matriz[row][col] + B.matriz[row][col]
        })

        return resultado
    }

    static subtract(A, B) {
        let resultado = new Matriz(A.rows, A.cols)
        resultado.map((e, row, col) => {
            return A.matriz[row][col] - B.matriz[row][col]
        })

        return resultado
    }

    static escalarMultiply(A, escalar) {
        let resultado = new Matriz(A.rows, A.cols)
        resultado.map((e, row, col) => {
            return A.matriz[row][col] * escalar
        })
        return resultado
    }

    static hadamard(A, B) {
        let resultado = new Matriz(A.rows, A.cols)
        resultado.map((e, row, col) => {
            return A.matriz[row][col] * B.matriz[row][col]
        })
        return resultado
    }

    static multiply(A, B)
    {
        var resultado = new Matriz(A.rows, B.cols);

        resultado.map((e, i, j) => {
            let sum = 0
            for (let k = 0; k < A.cols; k++) {
                let elm1 = A.matriz[i][k];
                let elm2 = B.matriz[k][j];
                sum += elm1 * elm2;
            }
            return sum;
        })

        return resultado;
    }
}
