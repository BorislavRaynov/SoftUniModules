
function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'
    const loadBtn = document.getElementById('load-board-btn')
    const addBtn = document.getElementById('create-task-btn')
    const titleEl = document.getElementById('title')
    const descriptionEl = document.getElementById('description')
    const toDoWrapper = document.querySelector('#todo-section .task-list')
    const inProgressWrapper = document.querySelector('#in-progress-section .task-list')
    const codeReviewWrapper = document.querySelector('#code-review-section .task-list')
    const doneWrapper = document.querySelector('#done-section .task-list')

    loadBtn.addEventListener('click', loader)
    addBtn.addEventListener('click', addHandler)

    async function loader(event) {
        event?.preventDefault()
        toDoWrapper.innerHTML = ''
        inProgressWrapper.innerHTML = ''
        codeReviewWrapper.innerHTML = ''
        doneWrapper.innerHTML = ''

        let response = await fetch(BASE_URL)
        let data = await response.json()
        data = Object.values(data)
        console.log(data)
        for (let { title, description, status, id } of data) {
            if (status === 'ToDo') {
                let li = createHtmlElement('li', '', toDoWrapper, ['task'], id)
                createHtmlElement('h3', title, li)
                createHtmlElement('p', description, li)
                let currentBtn = createHtmlElement('button', 'Move to in Progress', li)
                currentBtn.addEventListener('click', moveHandler)
            }

            else if (status === 'In Progress') {
                let li = createHtmlElement('li', '', inProgressWrapper, ['task'], id)
                createHtmlElement('h3', title, li)
                createHtmlElement('p', description, li)
                let currentBtn = createHtmlElement('button', 'Move to Code Review', li)
                currentBtn.addEventListener('click', moveHandler)
            }

            else if (status === 'Code Review') {
                let li = createHtmlElement('li', '', codeReviewWrapper, ['task'], id)
                createHtmlElement('h3', title, li)
                createHtmlElement('p', description, li)
                let currentBtn = createHtmlElement('button', 'Move to Done', li)
                currentBtn.addEventListener('click', moveHandler)
            }

            else if (status === 'Done') {
                let li = createHtmlElement('li', '', doneWrapper, ['task'], id)
                createHtmlElement('h3', title, li)
                createHtmlElement('p', description, li)
                let currentBtn = createHtmlElement('button', 'Close', li)
                currentBtn.addEventListener('click', closeHandler)
            }
        }
    }

    async function moveHandler(e) {
        let currentTask = this.parentNode
        let currentId = currentTask.id
        let status = currentTask.parentNode.getElementsByTagName('h1')[0].textContent
        let headers = {
            method: 'PATCH'
            // body: 
        }
    }

    async function closeHandler() {
        pass
    }

    async function addHandler() {
        let title = titleEl.value
        let description = descriptionEl.value
        let status = 'ToDo'
        if (title !== '' && description !== '') {
            let headers = {
                method: 'POST',
                body: JSON.stringify({ title, description, status })
            }

            let response = await fetch(BASE_URL, headers)
            if (response.ok) {
                loader()
                titleEl.value = ''
                descriptionEl.value = ''
            }
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