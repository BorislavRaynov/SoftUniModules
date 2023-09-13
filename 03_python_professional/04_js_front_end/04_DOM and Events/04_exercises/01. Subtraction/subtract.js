function subtract() {
    const fstNum = document.getElementById('firstNumber')
    const sndNum = document.getElementById('secondNumber')
    const result = document.getElementById('result')
    let numOne = Number(fstNum.value)
    let numTwo = Number(sndNum.value)
    let sum = numOne - numTwo
    result.textContent = sum
}