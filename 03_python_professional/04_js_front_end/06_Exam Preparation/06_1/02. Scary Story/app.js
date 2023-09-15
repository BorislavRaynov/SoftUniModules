window.addEventListener("load", solve);

function solve() {
  const dataInputs = Array.from(document.querySelectorAll('.inner-wrap input'))
  const selectEl = Array.from(document.getElementById('genre').children)
  const publishBtn = document.getElementById('form-btn')
  const previewEl = document.getElementById('preview-list')
  const storyEl = document.getElementsByTagName('textarea')[0]
  const main = document.getElementById('main')

  publishBtn.addEventListener('click', publishHandler)

  let currentStory = {}

  function publishHandler() {
    let inputDataLength = dataInputs.filter((el) => el.value === '').length
    let selectedItem = selectEl.filter((el) => el.selected === true).length
    let story = storyEl.value
    if (inputDataLength === 0 && selectedItem > 0 && story !== ''){
      let [ fstName, lstName, age, title ] = dataInputs.map((el) => el.value)
      let genreEl = selectEl.filter((el) => el.selected === true)[0]
      let genre = genreEl.value
      
      currentStory = { fstName, lstName, age, title, genreEl, story }

      let li = createHtmlElement('li', '', previewEl, '', ['story-info'])
      let article = createHtmlElement('article', '', li)
      createHtmlElement('h4', `Name: ${fstName} ${lstName}`, article)
      createHtmlElement('p', `Age: ${age}`, article)
      createHtmlElement('p', `Title: ${title}`, article)
      createHtmlElement('p', `Genre: ${genre}`, article)
      createHtmlElement('p', story, article)
      let saveBtn = createHtmlElement('button', 'Save Story', li, '', ['save-btn'])
      let editBtn = createHtmlElement('button', 'Edit Story', li, '', ['edit-btn'])
      let delBtn = createHtmlElement('button', 'Delete Story', li, '', ['delete-btn'])

      saveBtn.addEventListener('click',  saveHandler)
      editBtn.addEventListener('click', editHandler)
      delBtn.addEventListener('click', delHandler)

      publishBtn.disabled = true
      dataInputs.map((el) => el.value = '')
      storyEl.value = ''
    }

    function editHandler() {
      document.getElementById('first-name').value = currentStory.fstName
      document.getElementById('last-name').value = currentStory.lstName
      document.getElementById('age').value = currentStory.age
      document.getElementById('story-title').value = currentStory.title
      currentStory.genreEl.selected = true
      storyEl.value = currentStory.story
      let storyBtns = Array.from(document.querySelectorAll('article button'))
      storyBtns.map((el) => el.disabled = true)
      publishBtn.disabled = false
      delHandler()
      
    }

    function delHandler() {
      let currentEl = document.getElementsByClassName('story-info')[0]
      previewEl.removeChild(currentEl)
      publishBtn.disabled = false
    }

    function saveHandler() {
      main.innerHTML = ''
      createHtmlElement('h1', 'Your scary story is saved!', main)
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