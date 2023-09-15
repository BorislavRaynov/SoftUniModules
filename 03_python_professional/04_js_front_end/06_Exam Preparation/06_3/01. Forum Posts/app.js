window.addEventListener("load", solve);

function solve() {
  const publishBtn = document.getElementById('publish-btn')
  const reviewWrapper = document.getElementById('review-list')
  const publishedWrapper = document.getElementById('published-list')
  const clearBtn = document.getElementById('clear-btn')

  const inputs = {
    title: document.getElementById('post-title'),
    category: document.getElementById('post-category'),
    content: document.getElementById('post-content')
  }

  publishBtn.addEventListener('click', publishHandler)
  clearBtn.addEventListener('click', clearHandler)

  let currentPost = {}

  function publishHandler() {
    let allAreFilled = Object.values(inputs).every((el) => el.value !== '')
    if (!allAreFilled) {
      return
    }
    let [ title, category, content ] = Object.values(inputs).map((el) => el.value)
    currentPost = { title, category, content }
    let li = createHtmlElement('li', null, reviewWrapper, ['rpost'])
    let article = createHtmlElement('article', null, li)
    createHtmlElement('h4', title, article)
    createHtmlElement('p', `Category: ${category}`, article)
    createHtmlElement('p', `Content: ${content}`, article)
    let editBtn = createHtmlElement('button', 'Edit', li, ['action-btn', 'edit'])
    let approveBtn = createHtmlElement('button', 'Approve', li, ['action-btn', 'approve'])

    editBtn.addEventListener('click', editHandler)
    approveBtn.addEventListener('click', approveHandler)
    Object.values(inputs).map((el) => el.value = '')
  }

  function editHandler() {
    for (let data in currentPost) {
      inputs[data].value = currentPost[data]
    }
    this.parentNode.remove()
  }

  function approveHandler() {
    let currentEl = this.parentNode
    currentEl.querySelector('.edit').remove()
    currentEl.querySelector('.approve').remove()
    publishedWrapper.appendChild(currentEl)
  }

  function clearHandler() {
    publishedWrapper.innerHTML = ''
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
