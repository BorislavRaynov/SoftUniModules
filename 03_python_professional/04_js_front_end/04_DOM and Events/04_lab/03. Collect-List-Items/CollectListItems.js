function extractText() {
    const text = document.getElementsByTagName('li')
    let textToDisplay = document.getElementById('result')
    let result = ''
    for (let li of text) {
        result += li.textContent + '\n'
    }
    textToDisplay.textContent = result
}