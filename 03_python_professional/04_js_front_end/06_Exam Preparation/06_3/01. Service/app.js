window.addEventListener('load', solve);

function solve() {
    const sendBtn = document.querySelector('#right button')
    const receivedOrders = document.getElementById('received-orders')
    const completedOrders = document.getElementById('completed-orders')
    const clearBtn = document.querySelector('.clear-btn')

    const inputs = {
        type: document.getElementById('type-product'),
        description: document.getElementById('description'),
        name: document.getElementById('client-name'),
        phone: document.getElementById('client-phone')
    }

    sendBtn.addEventListener('click', sendHandler)
    clearBtn.addEventListener('click', clearHandler)

    function sendHandler(event) {
        event.preventDefault()
        let allAreFilled = Object.values(inputs).every((el) => el.value !== '')

        if (!allAreFilled) {
            return
        }

        let [ type, description, name, phone ] = Object.values(inputs).map((el) => el.value)
        let div = createHtmlElement('div', null, receivedOrders, ['container'])
        createHtmlElement('h2', `Product type for repair: ${type}`, div)
        createHtmlElement('h3', `Client information: ${name}, ${phone}`, div)
        createHtmlElement('h4', `Description of the problem: ${description}`, div)
        let startBtn = createHtmlElement('button', 'Start repair', div, ['start-btn'])
        let finishBtn = createHtmlElement('button', 'Finish repair', div, ['finish-btn'], null, {disabled: true})

        startBtn.addEventListener('click', startHandler)
        finishBtn.addEventListener('click', finishHandler)

        Object.values(inputs).map((el) => el.value = '')
    }

    function startHandler() {
        this.disabled = true
        this.nextSibling.disabled = false
    }

    function finishHandler() {
        let currentEl = this.parentNode
        this.parentNode.querySelector('.start-btn').remove()
        this.parentNode.querySelector('.finish-btn').remove()
        completedOrders.appendChild(currentEl)
    }

    function clearHandler() {
        let elements = Array.from(this.parentNode.querySelectorAll('.container'))
        for (let el of elements) {
            el.remove()
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