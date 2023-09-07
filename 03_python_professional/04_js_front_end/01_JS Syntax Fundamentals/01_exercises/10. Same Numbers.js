function solve(num) {
  let arr = String(num).split("");
    let searchedNum = arr[0]
    let counter = 0
    let sum = 0
    for (n of arr){
        if (n === searchedNum)
            counter++
        sum += Number(n)
    }
    let theSame = 'false'
    if (counter === arr.length){
        theSame = 'true'
    }

    console.log(theSame)
    console.log(sum)
}


solve(1234)
