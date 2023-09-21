function solve() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'
    const loadBtn = document.getElementById('load-course')
    const addBtn = document.getElementById('add-course')
    const editBtn = document.getElementById('edit-course')
    const coursesWrapper = document.getElementById('list')

    addBtn.addEventListener('click', addHandler)

    const inputs = {
      title: document.getElementById('course-name'),
      type: document.getElementById('course-type'),
      description: document.getElementById('description'),
      teacher: document.getElementById('teacher-name')
    }

    loadBtn.addEventListener('click', loader)
    editBtn.addEventListener('click', editHandler)

    let allCourses = {}
    let idToModify = null

    async function loader(event) {
        event?.preventDefault()
        coursesWrapper.innerHTML = ''

        let response = await fetch(BASE_URL)
        let data = await response.json()
        data = Object.values(data)

        for (let { title, type, description, teacher, _id } of data) {
            allCourses[_id] = { title, type, description, teacher }
            let div = createHtmlElement('div', null, coursesWrapper, ['container'], _id)
            createHtmlElement('h2', title, div)
            createHtmlElement('h3', teacher, div)
            createHtmlElement('h3', type, div)
            createHtmlElement('h4', description, div)
            let editCourseBtn = createHtmlElement('button', 'Edit Course', div, ['edit-btn'])
            let finishBtn = createHtmlElement('button', 'Finish Course', div, ['finish-btn'])

            editCourseBtn.addEventListener('click', editCourseHandler)
            finishBtn.addEventListener('click', finishHandler)
        }
    }

    async function addHandler(event) {
        event.preventDefault()

        let allAreFilled = Object.values(inputs).every((el) => el.value !== '')

        if(!allAreFilled) {
            return
        }

        let [ title, type, description, teacher ] = Object.values(inputs).map((el) => el.value)

        let httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ title, type, description, teacher })
        }

        let response = await fetch(BASE_URL, httpHeaders)
        if (response.ok) {
            loader()
            Object.values(inputs).map((el) => el.value = '')
        }
    }

    function editCourseHandler() {
      let currentId = this.parentNode.id
      idToModify = currentId
      for (let info in allCourses[currentId]) {
        inputs[info].value = allCourses[currentId][info]
      }

      editBtn.disabled = false
      addBtn.disabled = true

      this.parentNode.remove()
    }

    async function editHandler() {
      let [ title, type, description, teacher ] = Object.values(inputs).map((el) => el.value)
      let httpHeaders = {
        method: 'PUT',
        body: JSON.stringify({ title, type, description, teacher })
      }

      let response = await fetch(`${BASE_URL}${idToModify}`, httpHeaders)
      if (response.ok) {
        loader()
        editBtn.disabled = true
        addBtn.disabled = false
      }
    }

    async function finishHandler() {
      let currentId = this.parentNode.id
      let httpHeaders = {
        method: 'DELETE'
      }

      let response = await fetch(`${BASE_URL}${currentId}`, httpHeaders)
      if (response.ok) {
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

solve()