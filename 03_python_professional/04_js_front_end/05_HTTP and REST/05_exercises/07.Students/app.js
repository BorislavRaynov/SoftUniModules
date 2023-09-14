function attachEvents() {
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/students'
  const submitBtn = document.getElementById('submit')
  const inputFNameEl = document.querySelector('input[name = "firstName"]')
  const inputLNameEl = document.querySelector('input[name = "lastName"]')
  const fNumberEl = document.querySelector('input[name = "facultyNumber"]')
  const gradeEl = document.querySelector('input[name = "grade"]')
  const tBody = document.getElementsByTagName('tbody')[0]

  submitBtn.addEventListener('click', submitHandler)

  loadStudents()

  async function loadStudents() {
    try {
      let response = await fetch(BASE_URL)
      let students = await response.json()
      students = Object.values(students)
      tBody.innerHTML = ''
      for (let student of students) {
        let tr = document.createElement('tr')
        let fNameTd = document.createElement('td')
        let lNameTd = document.createElement('td')
        let fNumberTd = document.createElement('td')
        let gradeTd = document.createElement('td')
        fNameTd.textContent = student.firstName
        lNameTd.textContent = student.lastName
        fNumberTd.textContent = student.facultyNumber
        gradeTd.textContent = student.grade
        tr.appendChild(fNameTd)
        tr.appendChild(lNameTd)
        tr.appendChild(fNumberTd)
        tr.appendChild(gradeTd)
        tBody.appendChild(tr)
      }
    }
    catch(err) {
      console.error(err)
    }
  }

  async function submitHandler() {
    let firstName = inputFNameEl.value
    let lastName = inputLNameEl.value
    let facultyNumber = fNumberEl.value
    let grade = gradeEl.value
    let httpCreateHeaders = {
      method: 'POST',
      body: JSON.stringify({ firstName, lastName, facultyNumber, grade })
    }

    try {
      await fetch(BASE_URL, httpCreateHeaders)
    }
    catch(err) {
      console.error(err)
    }
    loadStudents()
    inputFNameEl.value = ''
    inputLNameEl.value = ''
    fNumberEl.value = ''
    gradeEl.value = ''
  }

}

attachEvents();