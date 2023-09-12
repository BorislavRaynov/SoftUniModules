function createDict(data) {
    let finalList = {}
    for (let el of data) {
        let parsed = JSON.parse(el)
        let entries = Object.entries(parsed)
        for (let info of entries) {
            finalList[info[0]] = info[1]
        }

    }
    let finalEntries = Object.entries(finalList)
    finalEntries.sort((a,b) => a[0].localeCompare(b[0]));
    for (let i of finalEntries) {
        console.log(`Term: ${i[0]} => Definition: ${i[1]}`)
    } 
}


createDict([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}',
    '{"Coffee":"A hot drink"}'
    ]
    )