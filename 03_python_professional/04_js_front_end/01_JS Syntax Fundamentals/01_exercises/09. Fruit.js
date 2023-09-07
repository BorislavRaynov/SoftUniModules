function solve(fruit, weight, price){
    weightInKg = weight / 1000
    let result = weightInKg * price
    console.log(`I need $${result.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`)
}

solve('apple', 1563, 2.35)