function colorize() {
    const trs = document.querySelectorAll('tr:nth-child(even)')
    for (let el of trs) {
        el.style.background = 'Teal'
    }
}