function solve(word, text){
    let textSplited = text.split(' ')
    let hasFound = false
    for (el of textSplited){
        if (el.toLowerCase() === word){
            hasFound = true
            console.log(word)
            break;
        }
    }
    if (hasFound === false){
        console.log(`${word} not found!`)
    }
}


solve('javascript', 'JavaScript is the best programming language')
solve('python', 'JavaScript is the best programming language')
