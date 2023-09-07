function solve(words, text){
    let wrodsArr = words.split(', ')
    let textArr = text.split(' ')
    let result = []
    for (el of textArr){
        if (el.includes('*')){
            for (wrd of wrodsArr){
                if (el.length === wrd.length){
                    result.push(wrd)
                }
            }
        }
        else {
            result.push(el)
        }
    }
    console.log(result.join(' '))
}
    



solve('great', 'softuni is ***** place for learning new programming languages')

solve('great, learning', 'softuni is ***** place for ******** new programming languages')