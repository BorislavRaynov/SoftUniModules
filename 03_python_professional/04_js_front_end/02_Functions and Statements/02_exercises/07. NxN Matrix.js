function printMatrix(num){
    for (let i = 0; i < num; i++){
        let currentRow = []
        for (let i = 0; i < num; i++){
            currentRow.push(num)
        }
        console.log(currentRow.join(' '))
    }
}

printMatrix(7)
