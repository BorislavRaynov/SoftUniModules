window.addEventListener("load", solve);

function solve() {
  const sideWrapper = document.getElementById('in-progress')
  const submitBtn = document.getElementById('form-btn')
  const counter = document.getElementById('progress-count')
  const finishedWrapper = document.getElementById('finished')
  const clearBtn = document.getElementById('clear-btn')
  
  const inputs = {
    firstName: document.getElementById('first-name'),
    lastName: document.getElementById('last-name'),
    age: document.getElementById('age'),
    gender: document.getElementById('genderSelect'),
    description: document.getElementById('task')
  }

  submitBtn.addEventListener('click', submitHandler)
  clearBtn.addEventListener('click', clearHandler)

  let currentCount = 0
  let currentDish = {}

  function submitHandler(event) {
    event.preventDefault()
    let allAreFilled = Object.values(inputs).every((el) => el.value !== '')
    if (!allAreFilled) {
      return
    }

    currentCount += 1
    let [ firstName, lastName, age, gender, description ] = Object.values(inputs).map((el) => el.value)
    currentDish = { firstName, lastName, age, gender, description }
    let li = createHtmlElement('li', null, sideWrapper, ['each-line'])
    let article = createHtmlElement('article', null, li)
    createHtmlElement('h4', `${firstName} ${lastName}`, article)
    createHtmlElement('p', `${gender}, ${age}`, article)
    createHtmlElement('p', `Dish description: ${description}`, article)
    let editBtn = createHtmlElement('button', 'Edit', li, ['edit-btn'])
    let completeBtn = createHtmlElement('button', 'Complete', li, ['complete-btn'])

    editBtn.addEventListener('click', editHandler)
    completeBtn.addEventListener('click', completeHandler)

    Object.values(inputs).map((el) => el.value = '')
    counter.textContent = currentCount
  }

  function editHandler() {
    currentCount -= 1
    this.parentNode.remove()
    for (let data in currentDish) {
      inputs[data].value = currentDish[data]
    }
    counter.textContent = currentCount
  }

  function completeHandler() {
    currentCount -= 1
    let el = this.parentNode
    el.getElementsByClassName('edit-btn')[0].remove()
    el.getElementsByClassName('complete-btn')[0].remove()
    finishedWrapper.appendChild(el)
    counter.textContent = currentCount
  }

  function clearHandler() {
    finishedWrapper.innerHTML = ''
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
