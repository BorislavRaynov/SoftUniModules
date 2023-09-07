function solve(num1, num2, num3) {
    let maxNum;

    if (num1>num2 && num1>num3) {
        maxNum = num1
    }

    else if (num2>num1 && num2>num3) {
        maxNum = num2
    }

    else if (num3>num2 && num3>num1) {
        maxNum = num3
    }

    console.log(`The largest number is ${maxNum}.`)
}

solve(-3, -5, -22.5)

