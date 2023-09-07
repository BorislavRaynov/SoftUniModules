function solve(text) {

    let result
    if (typeof(text) === 'number') {
        currentResult = Math.pow(text, 2) * Math.PI
        result = currentResult.toFixed(2)
    }

    else {
        result = `We can not calculate the circle area, because we receive a ${typeof(text)}.`
    }

    console.log(result)
}

solve('afasd')