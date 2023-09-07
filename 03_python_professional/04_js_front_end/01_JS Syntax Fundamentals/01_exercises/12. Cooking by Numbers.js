function solve(num, ...Operators){
    let currentResult = Number(num)
    for (op of Operators){
        if (op === 'chop'){
            currentResult /= 2
        } else if(op === 'dice'){
            currentResult = Math.sqrt(Number(currentResult))
        } else if(op === 'spice'){
            currentResult += 1
        } else if(op === 'bake'){
            currentResult *= 3
        } else if(op === 'fillet'){
            currentResult *= 0.8
        }
        console.log(currentResult)
    }
}

// solve('32', 'chop', 'chop', 'chop', 'chop', 'chop')
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')