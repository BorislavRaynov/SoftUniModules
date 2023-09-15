function resolve([initialNum, ...data]) {
    initialNum = Number(initialNum)
    let pieces = data.splice(0, initialNum)
    let commands = data.splice(0, data.length - 1)
    let allPieces = {}

    function findPiece(string) {
        if (Object.keys(allPieces).includes(string)) {
            return string
        }
        else {
            return false
        }
    }

    for (let p of pieces) {
        let [ piece, composer, key ] = p.split('|')
        allPieces[piece] = { composer, key }

    }
    for (let com of commands) {
        let currentData = com.split('|')
        currentCommand = currentData[0]
        if (currentCommand === 'Add') {
            let [ currentPiece, composer, key ] = [currentData[1], currentData[2], currentData[3]]
            if (findPiece(currentPiece)) {
                console.log(`${currentPiece} is already in the collection!`)
            }
            else {
                allPieces[currentPiece] = { composer, key } 
                console.log(`${currentPiece} by ${composer} in ${key} added to the collection!`)
            }
        }

        else if (currentCommand === 'Remove') {
            let currentPiece = findPiece(currentData[1])
            if (currentPiece) {
                delete allPieces[currentPiece]
                console.log(`Successfully removed ${currentData[1]}!`)
            }
            else {
                console.log(`Invalid operation! ${currentData[1]} does not exist in the collection.`)
            }
        }
        else if (currentCommand === 'ChangeKey') {
            let [ currentPiece, newKey ] = [ currentData[1], currentData[2] ]
            if (findPiece(currentPiece)) {
                allPieces[currentPiece].key = newKey
                console.log(`Changed the key of ${currentPiece} to ${newKey}!`)
            }
            else {
                console.log(`Invalid operation! ${currentPiece} does not exist in the collection.`)
            }
        }
    }

    for (let piece in allPieces) {
        console.log(`${piece} -> Composer: ${allPieces[piece].composer}, Key: ${allPieces[piece].key}`)
    }
}

resolve([
    '4',
    'Eine kleine Nachtmusik|Mozart|G Major',
    'La Campanella|Liszt|G# Minor',
    'The Marriage of Figaro|Mozart|G Major',
    'Hungarian Dance No.5|Brahms|G Minor',
    'Add|Spring|Vivaldi|E Major',
    'Remove|The Marriage of Figaro',
    'Remove|Turkish March',
    'ChangeKey|Spring|C Major',
    'Add|Nocturne|Chopin|C# Minor',
    'Stop'
  ]  
  )