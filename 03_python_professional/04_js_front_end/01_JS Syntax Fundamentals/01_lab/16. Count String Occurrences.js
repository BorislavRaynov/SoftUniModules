function solve(text, sWord) {
    let words = text.split(' ')
    result = 0
    for (word of words){
        if(word === sWord) {
            result ++
        }
    }
    console.log(result)
}


solve('This is a word and it also is a sentence', 'is')
solve('softuni is great place for learning new programming languages', 'softuni')