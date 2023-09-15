window.addEventListener('load', solve);

function solve() {
    const nextBtn = document.getElementById('next-btn')
    const infoResContainer = document.querySelector('#info-reservations .info-list')
    const confirmResContainer = document.querySelector('#confirm-reservations .confirm-list')
    const completeContainer = document.getElementById('verification')

    const inputs = {
        firstName: document.getElementById('first-name'),
        lastName: document.getElementById('last-name'),
        dateIn: document.getElementById('date-in'),
        dateOut: document.getElementById('date-out'),
        countPeople: document.getElementById('people-count')
    }

    nextBtn.addEventListener('click', nextHandler)

    let currentRes = {}

    function nextHandler(event) {
        event.preventDefault()
        let allAreFilled = Object.values(inputs).every((el) => el.value !== '')
        let dateInArr = inputs.dateIn.value.split('-')
        let dateOutArr = inputs.dateOut.value.split('-')
        let dateAreCorrect = false
        if (Number(dateInArr[0]) <= Number(dateOutArr[0])) {
            if (Number(dateInArr[1]) < Number(dateOutArr[1])) {
                dateAreCorrect = true
            }

            else if(Number(dateInArr[1]) === Number(dateOutArr[1])) {
                if (Number(dateInArr[2]) < Number(dateOutArr[2])) {
                    dateAreCorrect = true
                }
            }
        }

        if (!allAreFilled || !dateAreCorrect) {
            return
        }
        let [firstName, lastName, dateIn, dateOut, countPeople] = Object.values(inputs).map((el) => el.value)
        currentRes = { firstName,lastName, dateIn, dateOut, countPeople }
        let li = createHtmlElement('li', null, infoResContainer, ['reservation-content'])
        let article = createHtmlElement('article', null, li)
        createHtmlElement('h3', `Name: ${firstName} ${lastName}`, article)
        createHtmlElement('p', `From date: ${dateIn}`, article)
        createHtmlElement('p', `To date: ${dateOut}`, article)
        createHtmlElement('p', `For ${countPeople} people`, article)
        let editBtn = createHtmlElement('button', 'Edit', li, ['edit-btn'])
        let continueBtn = createHtmlElement('button', 'Continue', li, ['continue-btn'])

        Object.values(inputs).map((el) => el.value = '')
        nextBtn.disabled = true
        
        editBtn.addEventListener('click', editHandler)
        continueBtn.addEventListener('click', continueHandler)
    }

    function editHandler() {
        if (this.textContent === 'Edit') {
          for (let data in currentRes) {
            inputs[data].value = currentRes[data]
          }
          nextBtn.disabled = false
          this.parentElement.remove()
        }

        else if(this.textContent === 'Confirm') {
          nextBtn.disabled = false
          completeContainer.classList.add('reservation-confirmed')
          completeContainer.textContent = 'Confirmed'
          this.parentElement.remove()
        }

    }

    function continueHandler() {
      if (this.textContent === 'Continue') {
        let currentEl = this.parentElement
        let editBtn = document.getElementsByClassName('edit-btn')[0]
        let continueBtn = document.getElementsByClassName('continue-btn')[0]
        editBtn.textContent = 'Confirm'
        editBtn.classList.remove('edit-btn')
        editBtn.classList.add('confirm-btn')
        continueBtn.textContent = 'Cancel'
        continueBtn.classList.remove('continue-btn')
        continueBtn.classList.add('cancel-btn')

        confirmResContainer.appendChild(currentEl)
      }

      else if(this.textContent === 'Cancel') {
        nextBtn.disabled = false
        completeContainer.classList.add('reservation-cancelled')
        completeContainer.textContent = 'Cancelled'
        this.parentElement.remove()
      }

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