window.addEventListener('load', solve);

function solve() {

    const createBtn = document.getElementById('create-task-btn')
    const mainDeleteBtn = document.getElementById('delete-task-btn')
    const taskWrapper = document.getElementById('tasks-section')
    const sprintPoints = document.getElementById('total-sprint-points')
    const idStoreEl = document.getElementById('task-id')

    const inputs = {
        title: document.getElementById('title'),
        description: document.getElementById('description'),
        label: document.getElementById('label'),
        points: document.getElementById('points'),
        assignee: document.getElementById('assignee')
    }

    const labelClassesIcons = {
        'Feature': {additionalClass: 'feature', icon: '&#8865'},
        'Low Priority Bug': {additionalClass: 'low-priority', icon: '&#9737'},
        'High Priority Bug': {additionalClass: 'high-priority', icon: '&#9888'}
    }

    createBtn.addEventListener('click', createHandler)
    mainDeleteBtn.addEventListener('click', mainDeleteHandler)

    let articleId = 0
    let totalPoints = 0
    let allSprints = {}

    function createHandler() {
        let allAreFilled = Object.values(inputs).every((el) => el.value !== '')

        if (!allAreFilled) {
            return
        }

        articleId += 1
        let [ title, description, label, points, assignee ] = Object.values(inputs).map((el) => el.value)
        let article = createHtmlElement('article', null, taskWrapper, ['task-card'], `task-${articleId}`)
        allSprints[`task-${articleId}`] = { title, description, label, points, assignee }
        let currentIcon = labelClassesIcons[label].icon
        let currentAddClass = labelClassesIcons[label].additionalClass
        let divLabel = createHtmlElement('div', null, article, ['task-card-label', currentAddClass])
        divLabel.innerHTML = `${label} ${currentIcon}`
        createHtmlElement('h3', title, article, ['task-card-title'])
        createHtmlElement('p', description, article, ['task-card-description'])
        createHtmlElement('div', `Estimated at ${points} pts`, article, ['task-card-points'])
        totalPoints += Number(points)
        sprintPoints.textContent = `Total Points ${totalPoints}pts`
        createHtmlElement('div', `Assigned to: ${assignee}`, article, ['task-card-assignee'])
        let btnWrapper = createHtmlElement('div', null, article, ['task-card-actions'])
        let subDeleteBtn = createHtmlElement('button', 'Delete', btnWrapper)

        subDeleteBtn.addEventListener('click', subDelHandler)

        Object.values(inputs).map((el) => el.value = '')
    }

    function subDelHandler() {
        let currentEl = this.parentNode.parentNode
        idStoreEl.value = currentEl.id
        for (let data in inputs) {
            inputs[data].value = allSprints[currentEl.id][data]
        }

        Object.values(inputs).map((el) => el.disabled = true)
        mainDeleteBtn.disabled = false
        createBtn.disabled = true
    }

    function mainDeleteHandler () {
        let currentId = idStoreEl.value
        totalPoints -= Number(allSprints[currentId].points)
        let elToRemove = document.getElementById(currentId)

        taskWrapper.removeChild(elToRemove)

        sprintPoints.textContent = `Total Points ${totalPoints}pts`
        Object.values(inputs).map((el) => el.value = '')
        Object.values(inputs).map((el) => el.disabled = false)
        mainDeleteBtn.disabled = true
        createBtn.disabled = false
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