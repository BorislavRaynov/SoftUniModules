function toggle() {
    let currentTextBtn = document.getElementsByClassName('button')[0]
    console.log(currentTextBtn)
    let targetEl = document.getElementById('extra')
    if (currentTextBtn.textContent === 'More') {
        targetEl.style.display = 'block'
        currentTextBtn.textContent = 'Less'
    } else {
        targetEl.style.display = 'none'
        currentTextBtn.textContent = 'More'
    }
}