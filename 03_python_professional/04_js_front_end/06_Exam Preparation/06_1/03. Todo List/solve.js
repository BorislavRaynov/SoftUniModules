function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'
    const listWrapper = document.getElementById('todo-list')
    const loadBtn = document.getElementById('load-button')
    const inputTitleEl = document.getElementById('title')
    const addBtn = document.getElementById('add-button')

    loadBtn.addEventListener('click', loadItems)
    addBtn.addEventListener('click', addHandler)

    async function loadItems(event) {
        listWrapper.innerHTML = ''
        event?.preventDefault()
        let data = await fetch(BASE_URL)
        let info = await data.json()
        info = Object.values(info)
        for (let { name, _id } of info) {
            let li = createHtmlElement('li', '', '', '', _id)
            createHtmlElement('span', name, li)
            let removeBtn = createHtmlElement('button', 'Remove', li)
            let editBtn = createHtmlElement('button', 'Edit', li)

            removeBtn.addEventListener('click', removeHandler)
            editBtn.addEventListener('click', editHandler)

            listWrapper.appendChild(li)
        }
    }

    async function addHandler() {
        let name = inputTitleEl.value
        httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ name })
        }

        let response = await fetch(BASE_URL, httpHeaders)
        if (response.ok) {
            loadItems()
            inputTitleEl.value = ''
        }
    }

    async function editHandler(e) {
        if (this.textContent === 'Edit') {
            let currentSpan = this.parentNode.querySelector('span')
            let newText = currentSpan.textContent
            let inputField = document.createElement('input')
            inputField.value = newText
            this.parentNode.replaceChild(inputField, currentSpan)
            this.textContent = 'Submit'
        }

        else {
            let inputEl = this.parentNode.querySelector('input')
            let newName = inputEl.value
            httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({ name: newName })
            }

            let response = await fetch(`${BASE_URL}${this.parentNode.id}`, httpHeaders)
            if (response.ok) {
                loadItems()
                this.textContent === 'Edit'
            }
        }

    }

    async function removeHandler(e) {
        let httpHeaders = {
            method: 'DELETE'
        }
        let response = await fetch(`${BASE_URL}${this.parentNode.id}`, httpHeaders)
        if (response.ok) {
            loadItems()
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
