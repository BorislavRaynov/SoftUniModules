
function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'

    const inputs = {
        title: document.getElementById('title'),
        description: document.getElementById('description')
    }

    const buttons = {
        loadBtn: document.getElementById('load-board-btn'),
        createBtn: document.getElementById('create-task-btn')
    }

    const boards = {
        'ToDo': {element: document.querySelector('#todo-section .task-list'), btnTxt: 'Move to In Progress'},
        'In Progress': {element: document.querySelector('#in-progress-section .task-list'), btnTxt: 'Move to Code Review'},
        'Code Review': {element: document.querySelector('#code-review-section .task-list'), btnTxt: 'Move to Done'},
        'Done': {element: document.querySelector('#done-section .task-list'), btnTxt: 'Close'}
    }

    buttons.loadBtn.addEventListener('click', loader)
    buttons.createBtn.addEventListener('click', addHandler)

    async function loader(event) {
        event?.preventDefault()
        for (let data in boards) {
            boards[data].element.innerHTML = ''
        }
        let response = await fetch(BASE_URL)
        let data = await response.json()
        data = Object.values(data)
        for (let { title, description, status, _id } of data) {
            let li = createHtmlElement('li', null, boards[status].element, ['task'], _id)
            createHtmlElement('h3', title, li)
            createHtmlElement('p', description, li)
            let btn = createHtmlElement('button', boards[status].btnTxt, li)

            btn.addEventListener('click', actionHandler)
        }
    }

    async function actionHandler() {
        let currentElId = this.parentNode.id
        let headers = {
            method: 'DELETE'
        }

        if (this.textContent !== 'Close') {
            let currentMainParent = this.parentNode.parentNode.parentNode
            let nextMainParent = currentMainParent.nextElementSibling
            let status = nextMainParent.querySelector('h1').textContent
            headers = {
                method: 'PATCH',
                body: JSON.stringify({ status })
            }
        }

        let response = await fetch(`${BASE_URL}${currentElId}`, headers)
            if (response.ok) {
                loader()
            }

    }

    async function addHandler() {
        let [ title, description ] = Object.values(inputs).map((el) => el.value)
        let status = 'ToDo'
        let headers = {
            method: 'POST',
            body: JSON.stringify({ title, description, status })
        }

        let response = await fetch(BASE_URL, headers)
        if (response.ok) {
            Object.values(inputs).map((el) => el.value = '')
            loader()
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
attachEvents();