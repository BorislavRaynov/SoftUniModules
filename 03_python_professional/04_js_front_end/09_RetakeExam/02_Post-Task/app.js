window.addEventListener("load", solve);

function solve() {
    const publishBtn = document.getElementById('publish-btn')
    const ulWrapper = document.getElementById('review-list')
    const publishedWrapper = document.getElementById('published-list')
    const inputs = {
        title: document.getElementById('task-title'),
        category: document.getElementById('task-category'),
        content: document.getElementById('task-content')
    }

    publishBtn.addEventListener('click', publishHandler)

    function publishHandler() {
        let allAreFilled = Object.values(inputs).every((el) => el.value !== '')

        if (!allAreFilled) {
            return
        }

        let [ title, category, content ] = Object.values(inputs).map((el) => el.value)
        let li = createHtmlElement('li', null, ulWrapper, ['rpost'])
        let article = createHtmlElement('article', null, li)
        createHtmlElement('h4', title, article)
        createHtmlElement('p', `Category: ${category}`, article)
        createHtmlElement('p', `Content: ${content}`, article)
        let editBtn = createHtmlElement('button', 'Edit', li, ['action-btn', 'edit'])
        let postBtn = createHtmlElement('button', 'Post', li, ['action-btn', 'post'])

        editBtn.addEventListener('click', editHandler)
        postBtn.addEventListener('click', postHandler)

        Object.values(inputs).map((el) => el.value = '')
    }

    function editHandler() {
        let currentEl = this.parentNode
        let title = currentEl.querySelector('article :nth-child(1)').textContent
        let category = currentEl.querySelector('article :nth-child(2)').textContent.split(': ')[1]
        let content = currentEl.querySelector('article :nth-child(3)').textContent.split(': ')[1]
        let data = { title, category, content }
        for (let el in inputs) {
            inputs[el].value = data[el]
        }

        currentEl.remove()
    }

    function postHandler() {
        let currentEl = this.parentNode
        publishedWrapper.appendChild(currentEl)
        let eBtn = currentEl.querySelector('.edit')
        let pBtn = currentEl.querySelector('.post')
        eBtn.remove()
        pBtn.remove()
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