function resolve() {
    const BASE_URL = 'http://localhost:3030/jsonstore/grocery/'
    const tBody = document.getElementById("tbody")
    const loadBtn = document.getElementById('load-product')
    const addBtn = document.getElementById('add-product')
    const updateBtn = document.getElementById('update-product')
    const allInputEls = Array.from(document.getElementsByTagName('input'))
    let itemToUpdate = null

    loadBtn.addEventListener('click', loadingProducts)
    addBtn.addEventListener('click', addHandler)
    updateBtn.addEventListener('click', finalUpdateHandler)

    async function loadingProducts(event) {
        event?.preventDefault()
        tBody.innerHTML = ''
        let response = await fetch(BASE_URL)
        let info = await response.json()
        info = Object.values(info)
        for (let { product, count, price, _id } of info) {
            let tr = createHtmlElement('tr', '', tBody, _id)
            createHtmlElement('td', product, tr, '', ['name'])
            createHtmlElement('td', count, tr, '', ['count-product'])
            createHtmlElement('td', price, tr, '', ['product-price'])
            let productBtnWrapper = createHtmlElement('td', '', tr, '', ['btn'])
            let productUpdateBtn = createHtmlElement('button', 'Update', productBtnWrapper, '', ['update'])
            let productDeleteBtn = createHtmlElement('button', 'Delete', productBtnWrapper, '', ['delete'])

            productUpdateBtn.addEventListener('click', updateHandler)
            productDeleteBtn.addEventListener('click', deleteHandler)
        }
        
    }

    async function addHandler(event) {
        event.preventDefault()
        let [ product, count, price ] = allInputEls.map((el) => el.value)
        httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ product, count, price })
        }

        let response = await fetch(BASE_URL, httpHeaders)
        if (response.ok) {
            loadingProducts()
            allInputEls.map((el) => el.value = '')
        }
        
    }


    async function deleteHandler() {
        let currentItemId = this.parentNode.parentNode.id
        httpDelHeaders = {
            method: 'DELETE'
        }
        let response = await fetch(`${BASE_URL}${currentItemId}`, httpDelHeaders)
        if (response.ok) {
            loadingProducts()
        }
    }

    async function updateHandler(e) {
        let currentName = document.getElementById('product')
        let currentCount = document.getElementById('count')
        let currentPrice = document.getElementById('price')

        currentName.value = this.parentNode.parentNode.getElementsByTagName('td')[0].textContent
        currentCount.value = this.parentNode.parentNode.getElementsByTagName('td')[1].textContent
        currentPrice.value = this.parentNode.parentNode.getElementsByTagName('td')[2].textContent

        itemToUpdate = this.parentNode.parentNode.id
        updateBtn.disabled = false
        addBtn.disabled = true
    }

    async function finalUpdateHandler() {
        let [ product, count, price ] = allInputEls.map((el) => el.value)
        httpUpdateHeaders = {
            method: 'PATCH',
            body: JSON.stringify({ product, count, price })
        }

        let response = await fetch(`${BASE_URL}${itemToUpdate}`, httpUpdateHeaders)
        if (response.ok) {
            allInputEls.map((el) => el.value = '')
            loadingProducts()
            updateBtn.disabled = true
            addBtn.disabled = false
        }
    }

    function createHtmlElement(type, content, parentNode, id, classes, attributes) {
        const htmlElement = document.createElement(type);
      
        if (content && type !== "input") {
          htmlElement.textContent = content;
        }
      
        if (content && type === "input") {
          htmlElement.value = content;
        }
      
        if (id) {
          htmlElement.id = id;
        }
      
        if (classes) {
          htmlElement.classList.add(...classes);
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


resolve()
