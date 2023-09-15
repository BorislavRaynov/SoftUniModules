window.addEventListener("load", solve);

function solve() {
  const form = document.getElementsByTagName('form')[0]
  const publishBtn = document.getElementById('publish')
  const tBody = document.getElementById('table-body')
  const ul = document.getElementById('cars-list')
  const profit = document.getElementById('profit')

  const allInputs = {
    make: document.getElementById('make'),
    model: document.getElementById('model'),
    year: document.getElementById('year'),
    fuel: document.getElementById('fuel'),
    originalCost: document.getElementById('original-cost'),
    sellingPrice: document.getElementById('selling-price')
  }

  let currentCar = {}
  let totalProfit = 0

  publishBtn.addEventListener('click', publishHandler)

  function publishHandler(event) {
    event.preventDefault()
    let data = Object.values(allInputs)
    let allAreFilled = data.every((item) => item.value !== '')
    if (!allAreFilled) {
      return
    }
    
    if (Number(allInputs.originalCost.value) > Number(allInputs.sellingPrice.value)){
      return
    }

    let [ make, model, year, fuel, originalCost, sellingPrice ] = data.map((el) => el.value)
    currentCar = {make, model, year, fuel, originalCost, sellingPrice}
    let tr = createHtmlElement('tr', '', tBody, ['row'])
    createHtmlElement('td', make, tr)
    createHtmlElement('td', model, tr)
    createHtmlElement('td', year, tr)
    createHtmlElement('td', fuel, tr)
    createHtmlElement('td', originalCost, tr)
    createHtmlElement('td', sellingPrice, tr)
    let tdBtn = createHtmlElement('td', '', tr)
    let editBtn = createHtmlElement('button', 'Edit', tdBtn, ['action-btn', 'edit'])
    let sellBtn = createHtmlElement('button', 'Sell', tdBtn, ['action-btn', 'sell'])

    editBtn.addEventListener('click', editHandler)
    sellBtn.addEventListener('click', sellHandler)

    Object.values(allInputs).map((el) => el.value = '')
  }

  function editHandler() {
    for (let el in allInputs) {
      allInputs[el].value = currentCar[el]
    }

    this.parentNode.parentNode.remove()
  }

  function sellHandler() {
    let currentCarEl = this.parentNode.parentNode
    let diff = Number(currentCarEl.querySelector('td:nth-child(6)').textContent) - Number(currentCarEl.querySelector('td:nth-child(5)').textContent)
    let li = createHtmlElement('li', '', ul, ['each-list'])
    createHtmlElement('span', `${currentCarEl.querySelector('td:nth-child(1)').textContent} ${currentCarEl.querySelector('td:nth-child(2)').textContent}`, li)
    createHtmlElement('span', `${currentCarEl.querySelector('td:nth-child(3)').textContent}`, li)
    createHtmlElement('span', `${diff}`, li)
    totalProfit += diff
    profit.textContent = totalProfit.toFixed(2).toString()
    currentCarEl.remove()
  }

  function createHtmlElement(type, content, parentNode, classes, id, attributes) {
    const htmlElement = document.createElement(type);
  
    if (content && type !== "input") {
      htmlElement.textContent = content;
    }
  
    if (content && type === "input") {
      htmlElement.value = content;
    }
  
    if (classes) {
      htmlElement.classList.add(...classes);
    }
  
    if (id) {
      htmlElement.id = id;
    }
  
    if (attributes) {
      for (let key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }
  
    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }
  
    return htmlElement;
  }
}
