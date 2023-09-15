window.addEventListener('load', solve);

function solve() {
    const nextBtn = document.getElementById('next-btn')
    const ulContainer = document.querySelector('.ticket-info-list')
    const confirmUl = document.querySelector('.confirm-ticket')
    const form = document.querySelector('form')
    const mainDiv = document.getElementById('main')
    const body = document.getElementById('body')

    const inputDomEl = {
      firstName: document.getElementById('first-name'),
      lastName: document.getElementById('last-name'),
      countPeople: document.getElementById('people-count'),
      fromDate: document.getElementById('from-date'),
      countDays: document.getElementById('days-count')
    }

    let currentTicket = {}

    nextBtn.addEventListener('click', nextHandler)

    function nextHandler(event) {
        event.preventDefault()
        let inputValues = Object.values(inputDomEl)
        let allAreFilled = inputValues.every((data) => data.value !== '')
        if (!allAreFilled) {
          return
        }
        let [ firstName, lastName, countPeople, fromDate, countDays ] = Object.values(inputDomEl).map((input) => input.value)
        currentTicket = {firstName, lastName, countPeople, fromDate, countDays}
        let li = createHtmlElement('li', '', ulContainer, ['ticket'])
        let article = createHtmlElement('article', '', li)
        createHtmlElement('h3', `Name: ${firstName} ${lastName}`, article)
        createHtmlElement('p', `From date: ${fromDate}`, article)
        createHtmlElement('p', `For ${countDays} days`, article)
        createHtmlElement('p', `For ${countPeople} people`, article)
        let editBtn = createHtmlElement('button', 'Edit', li, ['edit-btn'])
        let continueBtn = createHtmlElement('button', 'Continue', li, ['continue-btn'])

        editBtn.addEventListener('click', editHandler)
        continueBtn.addEventListener('click', continueHandler)
        
        form.reset()
        this.disabled = true
    }

    function editHandler() {
      this.parentNode.remove()
      for (let key in currentTicket) {
        inputDomEl[key].value = currentTicket[key]
      }
      nextBtn.disabled = false
    }

    function continueHandler() {
        let ticket = this.parentNode

        let editBtn = ticket.querySelector('.edit-btn')
        let continueBtn = ticket.querySelector('.continue-btn')
        let confirmBtn = createHtmlElement('button', 'Confirm', ticket, ['confirm-btn'])
        let cancelBtn = createHtmlElement('button', 'Cancel', ticket, ['cancel-btn'])
        confirmBtn.addEventListener('click', confirmHandler)
        cancelBtn.addEventListener('click', cancelHandler)
        confirmUl.appendChild(ticket)
        
        editBtn.remove()
        continueBtn.remove()
    }

    function confirmHandler() {
      mainDiv.remove()
      createHtmlElement('h1', 'Thank you, have a nice day!', body, '', 'thank-you')
      let backBtn = createHtmlElement('button', 'Back', body, '', 'back-btn')

      backBtn.addEventListener('click', () => {
        window.location.reload()
      })
    }

    function cancelHandler() {
      this.parentNode.remove()
      nextBtn.disabled = false
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