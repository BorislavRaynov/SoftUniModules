function solve(text){
    let textArr = text.split(' ')
    let foundWords = []
    for (wrd of textArr){
        if (wrd.startsWith('#')){
            wrdSplited = wrd.replace('#', '')
            if (/^[a-zA-Z]/.test(wrdSplited.trim())) {
                foundWords.push(wrdSplited)
            }
        }
    }
    console.log(foundWords.join('\n'))
}


solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
solve('The symbol # is known #variously in English-speaking #regions as the #number sign')