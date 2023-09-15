function solve() {
    const addBtn = document.getElementById('add')
    const resetBrn = document.getElementById('reset')
    const mailListWrapper = document.getElementById('list')
    const sentMailsWrapper = document.getElementsByClassName('sent-list')[0]
    const deletedMailsWrapper = document.getElementsByClassName('delete-list')[0]

    const inputs = {
        name: document.getElementById('recipientName'),
        title: document.getElementById('title'),
        message: document.getElementById('message')
    }

    addBtn.addEventListener('click', addHandler)
    resetBrn.addEventListener('click', resetHandler)

    function addHandler(event) {
        event.preventDefault()
        let allAreFilled = Object.values(inputs).every((el) => el.value !== '')
        if (!allAreFilled) {
            return
        }

        let [ name, title, message ] = Object.values(inputs).map((el) => el.value)
        let li = createHtmlElement('li', null, mailListWrapper)
        createHtmlElement('h4', `Title: ${title}`, li)
        createHtmlElement('h4', `Recipient Name: ${name}`, li)
        createHtmlElement('span', message, li)
        let btnDivWrapper = createHtmlElement('div', null, li, null, 'list-action')
        let sendBtn = createHtmlElement('button', 'Send', btnDivWrapper, null, 'send', {type: 'submit'})
        let deleteBtn = createHtmlElement('button', 'Delete', btnDivWrapper, null, 'delete', {type: 'submit'})

        Object.values(inputs).map((el) => el.value = '')

        sendBtn.addEventListener('click', sendHandler)
        deleteBtn.addEventListener('click', deleteHandler)

    }

    function resetHandler() {
        Object.values(inputs).map((el) => el.value = '')
    }

    function sendHandler() {
        let currentEl = this.parentNode.parentNode
        let currentLi = createHtmlElement('li')
        let firstSpan = currentEl.getElementsByTagName('h4')[1].textContent.replace('Recipient Name', 'To')
        let secondSpan = currentEl.getElementsByTagName('h4')[0].textContent
        createHtmlElement('span', firstSpan, currentLi)
        createHtmlElement('span', secondSpan, currentLi)
        let btnWrapper = createHtmlElement('div', null, currentLi, ['btn'])
        let deleteSndBtn = createHtmlElement('button', 'Delete', btnWrapper, ['delete'], null, {type: 'submit'})
        sentMailsWrapper.appendChild(currentLi)
        currentEl.remove()

        deleteSndBtn.addEventListener('click', sndDeleteHandler)
    }

    function sndDeleteHandler() {
        currentEl = this.parentNode.parentNode
        deletedMailsWrapper.appendChild(currentEl)
        this.parentNode.remove()
    }

    function deleteHandler() {
        currentEl = this.parentNode.parentNode
        let li = createHtmlElement('li')
        let firstSpan = currentEl.getElementsByTagName('h4')[1].textContent.replace('Recipient Name', 'To')
        let secondSpan = currentEl.getElementsByTagName('h4')[0].textContent
        createHtmlElement('span', firstSpan, li)
        createHtmlElement('span', secondSpan, li)
        deletedMailsWrapper.appendChild(li)
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