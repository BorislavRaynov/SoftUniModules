function sumTable() {
    const firstTable = document.querySelector('table')
    const elements = Array.from(document.querySelectorAll('td:nth-child(even)'))
    let finalResult = elements.pop()
    let sum = 0
    for (let el of elements) {
        sum += Number(el.textContent)
    }
    finalResult.textContent = sum
}