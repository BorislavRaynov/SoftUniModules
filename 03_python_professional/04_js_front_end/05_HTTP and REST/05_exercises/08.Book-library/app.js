function attachEvents() {
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/books'
  const submitBtn = document.querySelector('#form button')
  const inputTitleEl = document.querySelector('input[name = "title"]')
  const inputAuthorEl = document.querySelector('input[name = "author"]')
  const tBody = document.getElementsByTagName('tbody')[0]
  const loadBtn = document.getElementById('loadBooks')
  const formHeader = document.querySelector('#form h3')
  let allBooks = {}
  let editBookId = null

  submitBtn.addEventListener('click', submitHandler)
  loadBtn.addEventListener('click', loadHandler)

  function loadHandler() {
    tBody.innerHTML = ''
    fetch(BASE_URL)
      .then((res) => res.json())
      .then((data) => {
        allBooks = data
        for (let info in data) {
          let book = data[info]
          let tr = document.createElement('tr')
          let authorTd = document.createElement('td')
          let nameTd = document.createElement('td')
          let btnTd = document.createElement('td')
          let editBtn = document.createElement('button')
          let deleteBtn = document.createElement('button')
          editBtn.textContent = 'Edit'
          deleteBtn.textContent = 'Delete'
          authorTd.textContent = book.author
          nameTd.textContent = book.title

          deleteBtn.addEventListener('click', deleteHandler)
          editBtn.addEventListener('click', () => {
            editBookId = info
            formHeader.textContent = 'EditFORM'
            submitBtn.textContent = 'Save'
            inputAuthorEl.value = book.author
            inputTitleEl.value = book.title
          })

          btnTd.appendChild(editBtn)
          btnTd.appendChild(deleteBtn)
          tr.appendChild(nameTd)
          tr.appendChild(authorTd)
          tr.appendChild(btnTd)
          tBody.appendChild(tr)


         }
      })
      .catch((err) => console.error(err))
  }

  function submitHandler() {
    let author = inputAuthorEl.value
    let title = inputTitleEl.value
    let httpCreateHeaders = {
      body: JSON.stringify({author, title})
    }
    let url = BASE_URL
    if (author && title) {
      if (submitBtn.textContent === 'Submit'){
        httpCreateHeaders.method = 'POST'
      }

      if (submitBtn.textContent === 'Save') {
        httpCreateHeaders.method = 'PUT'
        url += `/${editBookId}`
        formHeader.textContent = 'FORM'
        submitBtn.textContent = 'Submit'
      }
      fetch(url, httpCreateHeaders)   
      loadHandler()
      inputAuthorEl.value = ''
      inputTitleEl.value = ''
    }
  }


  function deleteHandler() {
    pass
  }

}

attachEvents();