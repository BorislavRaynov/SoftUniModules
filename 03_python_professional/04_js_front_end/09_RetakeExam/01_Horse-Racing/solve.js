function solve(data) {
    let horses = data.shift().split('|')
    data.pop()
    for (let info of data) {
        let elements = info.split(' ')
        let command = elements.shift()
        if (command === 'Retake') {
            overTakingHorse = elements[0]
            overTakenHorse = elements[1]
            let overTakingPosition = Number(horses.indexOf(overTakingHorse))
            let overTakenPosition = Number(horses.indexOf(overTakenHorse))
            if (overTakingPosition < overTakenPosition) {
                horses[overTakenPosition] = overTakingHorse
                horses[overTakingPosition] = overTakenHorse
                console.log(`${overTakingHorse} retakes ${overTakenHorse}.`)
            }
        }

        else if (command === 'Trouble') {
            let horseName = elements[0]
            let index = Number(horses.indexOf(horseName))
            if (index > 0) {
                let otherHorseIndex = index - 1
                let otherName = horses[index - 1]
                horses[otherHorseIndex] = horseName
                horses[index] = otherName
                console.log(`Trouble for ${horseName} - drops one position.`) 
            }
        }

        else if (command === 'Rage') {
            let horseName = elements[0]
            let currentHorsePosition = Number(horses.indexOf(horseName))
            if (currentHorsePosition === horses.length - 2) {
                
                let otherHorseName = horses[currentHorsePosition + 1]
                horses[currentHorsePosition + 1] = horseName
                horses[currentHorsePosition] = otherHorseName
            }
            else if (currentHorsePosition < horses.length - 2) {
                let theOneBefore = horses[currentHorsePosition + 1]
                let otherHorseName = horses[currentHorsePosition + 2]
                horses[currentHorsePosition + 2] = horseName
                horses[currentHorsePosition + 1] = otherHorseName
                horses[currentHorsePosition] = theOneBefore
            }
            console.log(`${horseName} rages 2 positions ahead.`)
        }

        if (command === 'Miracle') {
            let horseName = horses[0]
            horses.push(horses.shift())
            console.log(`What a miracle - ${horseName} becomes first.`)
        }

    }

    console.log(horses.join('->'))
    console.log(`The winner is: ${horses[horses.length - 1]}`)
}


solve(
    (['Bella|Alexia|Sugar',
    'Retake Alexia Sugar',
    'Rage Bella',
    'Trouble Bella',
    'Finish'])
)