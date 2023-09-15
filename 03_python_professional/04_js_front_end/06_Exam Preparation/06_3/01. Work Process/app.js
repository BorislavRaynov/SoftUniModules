function solve() {
    const hireBtn = document.getElementById('add-worker')
    const tBody = document.querySelector('#tbody')
    const salaryWrapper = document.getElementById('sum')
    const inputs = {
        fstName: document.getElementById('fname'),
        lstName: document.getElementById('lname'),
        email: document.getElementById('email'),
        dateOfBirth: document.getElementById('birth'),
        position: document.getElementById('position'),
        salary: document.getElementById('salary')
    }

    hireBtn.addEventListener('click', hireHandler)

    let allWorkers = {}

    let sum = 0
    let id = 0

    function hireHandler(event) {
        event.preventDefault()
        let allAreFilled = Object.values(inputs).every((el) => el.value !== '')

        if (!allAreFilled) {
            return
        }

        let [ fstName, lstName, email, dateOfBirth, position, salary ] = Object.values(inputs).map((el) => el.value)
        id += 1
        allWorkers[id] = { fstName, lstName, email, dateOfBirth, position, salary }
        sum += Number(salary)
        salaryWrapper.textContent = sum.toFixed(2)
        let tr = createHtmlElement('tr', null, tBody, null, id)
        createHtmlElement('td', fstName, tr)
        createHtmlElement('td', lstName, tr)
        createHtmlElement('td', email, tr)
        createHtmlElement('td', dateOfBirth, tr)
        createHtmlElement('td', position, tr)
        createHtmlElement('td', salary, tr)
        let tdBtn = createHtmlElement('td', null, tr)
        let firedBtn = createHtmlElement('button', 'Fired', tdBtn, ['fired'])
        let editBtn = createHtmlElement('button', 'Edit', tdBtn, ['edit'])
        Object.values(inputs).map((el) => el.value = '')
        
        editBtn.addEventListener('click', editHandler)
        firedBtn.addEventListener('click', fireHandler)


    }

    function editHandler() {
        currentEl = this.parentNode.parentNode
        currentId = currentEl.id
        for (let data in allWorkers[currentId]) {
            inputs[data].value = allWorkers[currentId][data]
        }
        sum -= Number(allWorkers[currentId]['salary'])
        salaryWrapper.textContent = sum.toFixed(2)
        currentEl.remove()
    }

    function fireHandler() {
        currentEl = this.parentNode.parentNode
        currentId = currentEl.id
        sum -= Number(allWorkers[currentId]['salary'])
        salaryWrapper.textContent = sum.toFixed(2)
        currentEl.remove()
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
solve()