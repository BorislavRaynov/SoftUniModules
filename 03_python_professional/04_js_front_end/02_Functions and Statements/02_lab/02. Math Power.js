function raiseNum(num, power){
    let result = 1
    for (let i = 1; i <= power; i++){
        result *= num 
    }
    console.log(result)
}

raiseNum(2,8)