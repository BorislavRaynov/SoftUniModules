function addItem() {
    const dataTextElement = document.getElementById('newItemText')
    const dataValueElement = document.getElementById('newItemValue')
    const menu = document.getElementById('menu')
    let newOption = document.createElement('option')
    newOption.textContent = dataTextElement.value
    newOption.value = dataValueElement.value
    menu.appendChild(newOption)
    dataTextElement.value = ''
    dataValueElement.value = ''
}