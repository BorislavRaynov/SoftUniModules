function solve(num){
    let numArr = String(num).split('')
    let sum = 0
    for (n of numArr){
        sum += Number(n)
    }
    console.log(sum)
}


solve(97561)
