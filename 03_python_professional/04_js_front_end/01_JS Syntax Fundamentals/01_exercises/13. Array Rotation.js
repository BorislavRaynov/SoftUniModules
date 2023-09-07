function solve(arr, num){
    currentArr = arr
    for (let i=0; i<num; i++){
        currentArr.push(currentArr.shift(currentArr[i]))
    }
    console.log(currentArr.join(' '))
}   


solve([32, 21, 61, 1], 4)